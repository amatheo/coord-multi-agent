from offre import Offre


class AgentFournisseur:
    def __init__(self, prix_initial, variation_max, max_iterations):
        self.prix = prix_initial
        self.variation_max = variation_max
        self.max_iterations = max_iterations

    def proposer_offre(self, iteration):
        # Ajuster le prix de manière compétitive
        if iteration < self.max_iterations:
            self.prix *= 1 - self.variation_max
        return Offre(self.prix)