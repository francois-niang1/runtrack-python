class Livre: 
    def __init__(self, titre: str, Auteur): 
        self.auteur = Auteur
        self.titre = titre

    @property
    def print(self):
        return self.titre
