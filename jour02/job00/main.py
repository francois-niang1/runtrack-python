class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print("Bonjour, je m'appelle", self.prenom, self.nom)

# Création d'une instance de la classe Personne
person1 = Personne("Niang", 'Francois')
person2 = Personne("sanchez", 'Kevin')
person3 = Personne("Wick", "John")

# Appel de la méthode SePresenter() de l'instance person1
person1.SePresenter()
person2.SePresenter()
person3.SePresenter()