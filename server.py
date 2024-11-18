import socket
import pickle  # Pour sérialiser/désérialiser des objets Python
from offre import Negociation, Offre, RefusOffre
from vendeur import AgentFournisseur

# Configuration de l'hôte et du port
HOST = '127.0.0.1'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        agentFournisseur = AgentFournisseur(100, 0.1, 10)
        print("Serveur en attente de connexion...")

        conn, addr = s.accept()
        with conn:
            print(f"Connecté à {addr}")
            for iteration in range(agentFournisseur.max_iterations):
                # Générer une offre
                offre = agentFournisseur.proposer_offre(iteration)
                
                # Envoyer l'objet Offre au client
                conn.sendall(pickle.dumps(offre))  # Sérialisation avec pickle
                print(f"Offre envoyée: {offre.prix}")

                # Recevoir un objet du client
                data = conn.recv(1024)
                if not data:
                    break
                reponse = pickle.loads(data)  # Désérialisation avec pickle
                print(f"Réponse reçue du client: {type(reponse).__name__}")

                # Gérer différents types de réponses
                if isinstance(reponse, Offre):
                    print("Le client propose une contre-offre:", reponse.prix)
                elif isinstance(reponse, RefusOffre):
                    print("Le client a refusé l'offre.")
                elif isinstance(reponse, Negociation):
                    print("Le client demande une négociation:", reponse.details)
                
                if isinstance(reponse, Offre) and reponse.prix >= agentFournisseur.prix:
                    print("Offre acceptée par le serveur.")
                    break
            print("Fin des communications.")
            
if __name__ == "__main__":
    main()
