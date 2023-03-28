class Personne:
    def __init__(self, firstName: str, name: str):
        self.name = name
        self.firstName = firstName
    
    def sePresenter(self):
        print("Bonjour, je m'appelle", self.firstName, self.name, "et j'ai ecrit :")