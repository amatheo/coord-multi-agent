import socket
import time

# Configuration de l'hôte et du port
HOST = '127.0.0.1'  # Adresse du serveur
PORT = 65432        # Port du serveur

# Création de la socket client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connexion au serveur
    while True:
        s.sendall("Bonjour, serveur!".encode('utf-8'))  # Envoi d'un message
        data = s.recv(1024)             # Réception de la réponse

        print("Réponse du serveur:", data.decode('utf-8'))
        time.sleep(1)  # Pause d'une seconde
