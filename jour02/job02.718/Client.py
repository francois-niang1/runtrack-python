from Personne import Personne

class Client(Personne):
    def __init__(self, firstName: str, name: str):
        super().__init__(firstName, name)
        self.collection_livres = {}

    def louer(self, bibliotheque, titre):
        if titre in bibliotheque.catalogue and bibliotheque.catalogue[titre] > 0:
            bibliotheque.catalogue[titre] -= 1
            if titre in self.collection_livres:
                self.collection_livres[titre] += 1
            else:
                self.collection_livres[titre] = 1
            print(f"{self.name} {self.firstName} a loué le livre {titre}")
        else:
            print(f"Le livre {titre} n'est pas disponible dans la bibliothèque")

