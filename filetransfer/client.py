import socket               # Importer le module socket
from tkinter import filedialog

s = socket.socket()         # Créer un objet socket
host = socket.gethostname() # Obtenir le nom de la machine locale
port = 55556                 # Réserver un port pour le service

def openFile():
    # Ouvrir la boîte de dialogue pour sélectionner un fichier
    filepath = filedialog.askopenfilename(initialdir="Bureau",
                                          title="Ouvrir le fichier",
                                          filetypes=(("Image", "*.png"),
                                                     ("Tous les fichiers", "*.*")))
    return filepath

s.connect((host, port))     # Se connecter au serveur distant
f = open(openFile(), 'rb')  # Ouvrir le fichier en mode lecture binaire

print('Envoi en cours...')
l = f.read(1024)            # Lire les premiers 1024 octets du fichier
while l:
    print('Envoi en cours...')
    s.send(l)               # Envoyer les données lues au serveur
    l = f.read(1024)        # Lire les 1024 octets suivants
f.close()                   # Fermer le fichier après l'envoi

print("Envoi terminé")

s.shutdown(socket.SHUT_WR)  # Fermer l'écriture côté client
print(s.recv(1024).decode("utf8"))  # Recevoir la réponse du serveur et l'afficher

s.close()                   # Fermer la connexion socket côté client
