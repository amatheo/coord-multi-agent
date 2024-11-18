class AgentAcheteur:
    def __init__(self, budget, date_limite, preferences):
        self.budget = budget
        self.date_limite = date_limite
        self.preferences = preferences
        self.coalition = None

    def evaluer_offre(self, offre):
        return offre.prix <= self.budget  # Critère simplifié d'acceptation de l'offre
