import socket
import threading
import tkinter as tk
from tkinter import ttk

def receive_client_messages(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        chat_box.insert(tk.END, f"Client: {data.decode('utf-8')}\n", 'client_message')

def send_message(event=None):
    message = input_field.get()
    if message:
        client_connection.sendall(message.encode('utf-8'))
        chat_box.insert(tk.END, f"Server: {message}\n", 'server_message')
        input_field.delete(0, tk.END)

def start_server():
    global server_socket, client_connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 65432))
    server_socket.listen(5)
    chat_box.insert(tk.END, "Server is listening...\n")
    conn, addr = server_socket.accept()
    chat_box.insert(tk.END, f"Connected by {addr}\n")
    client_connection = conn
    thread_client = threading.Thread(target=receive_client_messages, args=(conn,))
    thread_client.start()

# Interface graphique avec couleurs de texte différentes pour le serveur
server_window = tk.Tk()
server_window.title("Server")
server_window.configure(bg="#333")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=6, relief="flat", background="#444", foreground="#fff", font=('Helvetica', 10), borderwidth=0)
style.map("TButton", background=[('pressed', '#555'), ('active', '#666')])

chat_box = tk.Text(server_window, height=20, width=50, bg="#333", fg="#fff", insertbackground="#fff", selectbackground="#666")
chat_box.tag_config('client_message', foreground='cyan')
chat_box.tag_config('server_message', foreground='red')
chat_box.pack()

input_field = ttk.Entry(server_window, width=50, font=('Helvetica', 10), style="TButton")
input_field.pack()
input_field.bind("<Return>", send_message)

send_button = ttk.Button(server_window, text="Send", style="TButton", command=send_message)
send_button.pack()

start_button = ttk.Button(server_window, text="Start Server", style="TButton", command=start_server)
start_button.pack()

server_window.mainloop()
