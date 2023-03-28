from Livre import Livre 
from Personne import Personne 

class Auteur(Personne):

    oeuvres: list = []

    def __init__(self, firstName: str, name: str, oeuvres: list = []):
        super().__init__(firstName, name)
        self.oeuvres = oeuvres
    
    def ecrireUnLivre(self, titre: str):
        self.oeuvres.append(Livre(titre, self))
    
    def listerOeuvres(self):
        for livre in self.oeuvres:
            print(livre.print)
