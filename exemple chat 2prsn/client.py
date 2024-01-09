import socket
import threading
import tkinter as tk
from tkinter import ttk

def receive_server_messages(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        chat_box.insert(tk.END, f"Server: {data.decode('utf-8')}\n", 'server_message')

def send_message(event=None):
    message = input_field.get()
    if message:
        client_socket.sendall(message.encode('utf-8'))
        chat_box.insert(tk.END, f"Client: {message}\n", 'client_message')
        input_field.delete(0, tk.END)

def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 65432))
    chat_box.insert(tk.END, "Connected to server...\n")
    thread_server = threading.Thread(target=receive_server_messages, args=(client_socket,))
    thread_server.start()

# Interface graphique avec couleurs de texte différentes pour le client
client_window = tk.Tk()
client_window.title("Client")
client_window.configure(bg="#333")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=6, relief="flat", background="#444", foreground="#fff", font=('Helvetica', 10), borderwidth=0)
style.map("TButton", background=[('pressed', '#555'), ('active', '#666')])

chat_box = tk.Text(client_window, height=20, width=50, bg="#333", fg="#fff", insertbackground="#fff", selectbackground="#666")
chat_box.tag_config('client_message', foreground='cyan')
chat_box.tag_config('server_message', foreground='red')
chat_box.pack()

input_field = ttk.Entry(client_window, width=50, font=('Helvetica', 10), style="TButton")
input_field.pack()
input_field.bind("<Return>", send_message)

send_button = ttk.Button(client_window, text="Send", style="TButton", command=send_message)
send_button.pack()

connect_button = ttk.Button(client_window, text="Connect to Server", style="TButton", command=start_client)
connect_button.pack()

client_window.mainloop()
