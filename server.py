import socket

# Configuration de l'hôte et du port
HOST = '127.0.0.1'  # Adresse localhost
PORT = 65432        # Port d'écoute

# Création de la socket serveur
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Liaison de la socket à l'adresse et au port
    s.listen()            # Mise en écoute de la socket
    print("Serveur en attente de connexion...")

    conn, addr = s.accept()  # Accepter la connexion entrante
    with conn:
        print(f"Connecté à {addr}")
        while True:
            data = conn.recv(1024)  # Réception des données
            if not data:
                break
            print("Message reçu du client:", data.decode('utf-8'))
            conn.sendall("Message reçu par le serveur".encode('utf-8')) # Envoi d'une réponse
