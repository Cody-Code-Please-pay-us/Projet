import socket               # Importe le module socket

s = socket.socket()         # Crée un objet socket
host = socket.gethostname() # Obtient le nom de la machine locale
port = 55556                 # Réserve un port pour le service.
s.bind((host, port))        # Lie le socket au port spécifié
f = open('torecv.png','wb') # Ouvre un fichier en mode écriture binaire pour écrire les données reçues

s.listen(5)                 # Commence à écouter les connexions entrantes (jusqu'à 5 en attente).
print ("Server Started")

while True:                 # Boucle infinie pour accepter les connexions entrantes en continu
    c, addr = s.accept()    # Accepte la connexion du client lorsque celle-ci arrive.
    print ('Got connection from'), addr  # Affiche l'adresse du client qui s'est connecté
    print ("Receiving...")

    l = c.recv(1024)        # Reçoit les premières données du client (jusqu'à 1024 octets à la fois)
    while (l):              # Boucle tant qu'il y a des données à recevoir
        print ("Receiving...")
        f.write(l)          # Écrit les données reçues dans le fichier
        l = c.recv(1024)    # Continue à recevoir les données par morceaux

    f.close()               # Ferme le fichier après avoir reçu toutes les données
    print ("Done Receiving")

    open('torecv.png')      # Cette ligne ne fait rien car elle ouvre le fichier mais ne fait rien avec

    c.send(bytes('Thank you for connecting !!','utf8'))  # Envoie un message de remerciement au client
    c.shutdown(1)           # Ferme la connexion côté serveur (permettant au client de savoir que le serveur a fini d'envoyer)

    break   # Sort de la boucle infinie après avoir traité une seule connexion 