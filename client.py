import socket
import pickle  # Pour sérialiser/désérialiser des objets Python
from acheteur import AgentAcheteur
from offre import Offre

# Configuration de l'hôte et du port
HOST = '127.0.0.1'
PORT = 65432

# Classes supplémentaires pour gérer différents types de réponses
class RefusOffre:
    pass

class Negociation:
    def __init__(self, details):
        self.details = details

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        agentAcheteur = AgentAcheteur(100, 10, [1, 2, 3, 4, 5])
        
        while True:
            # Recevoir un objet Offre du serveur
            data = s.recv(1024)
            if not data:
                break
            offre = pickle.loads(data)  # Désérialisation
            print(f"Offre reçue: {offre.prix}")

            # Décider de la réponse
            if agentAcheteur.evaluer_offre(offre):
                print("Offre acceptée.")
                s.sendall(pickle.dumps(offre))  # Réponse avec l'objet Offre accepté
                break
            elif offre.prix > agentAcheteur.budget:
                print("Offre refusée.")
                s.sendall(pickle.dumps(RefusOffre()))  # Réponse avec RefusOffre
            else:
                print("Demande de négociation.")
                s.sendall(pickle.dumps(Negociation("Proposez une réduction de 10%")))  # Réponse avec Negociation

if __name__ == "__main__":
    main()
