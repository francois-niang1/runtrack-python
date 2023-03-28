from Auteur import Auteur

class Bibliothèque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        if titre in auteur.oeuvres:
            if titre in self.catalogue:
                self.catalogue[titre] += quantite
            else:
                self.catalogue[titre] = quantite
            print(f"{quantite} exemplaire(s) du livre \"{titre}\" de l'auteur {auteur.firstName} ont été ajouté(s) au catalogue de la bibliothèque.")
        else:
            print(f"Le livre \"{titre}\" n'existe pas dans l'oeuvre de l'auteur {auteur.firstName}. Aucun exemplaire n'a été ajouté au catalogue de la bibliothèque.")

    def inventaire(self, bibliotheque):
        print(" ")
        print (f"Il y a dans le catalogue {bibliotheque.nom} :" )
        for titre, quantite in self.catalogue.items():
            print(f"{titre} : {quantite}")

    def rendreLivres(self, client):
        for titre, quantite in client.collection_livres.items():
            if titre in self.catalogue:
                self.catalogue[titre] += quantite
            else:
                self.catalogue[titre] = quantite
        client.collection_livres.clear()
        print(f"{client.name} {client.firstName} a rendu tous ses livres du catalogue")