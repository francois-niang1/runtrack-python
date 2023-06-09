from Auteur import Auteur
from Personne import Personne
from Client import Client
from Bibliothèque import Bibliothèque

# Creation d'auteur et leur oeuvres
moi = Auteur("Francois", "Niang", {"Naruto", "One Piece", "Jojo Bizarre adventure"})
Auteur1 = Auteur("Hugo", "Chabert", {"Mein kampf", "Fifa pour les nuls", "The last Dance"})
Auteur2 = Auteur("Victor", "Hugo", {"Les Misérables" , "Notre-Dame de Paris"})
Auteur3 = Auteur("Jules", "Vernes", {"Vingt mille lieues sous les mers", "Le Tour du monde en quatre-vingts jours"})
Auteur4 = Auteur("Albert", "Camus", {"L'etranger"})

# Creation des Catalogues
Manga = Bibliothèque('Manga')
Littérature = Bibliothèque('Littérature')
Documentation = Bibliothèque('Documentation')

# Je remplie les catalogues
    # Manga
Manga.acheterLivre(moi, "Jojo Bizarre adventure", 2)
Manga.acheterLivre(moi, "Naruto", 3)
Manga.acheterLivre(moi, "One Piece", 2)
print(" ")

    # Littérature
Littérature.acheterLivre(Auteur2, "Les Misérables", 5)
Littérature.acheterLivre(Auteur2, "Notre-Dame de Paris", 1)
Littérature.acheterLivre(Auteur3, "Vingt mille lieues sous les mers", 3)
Littérature.acheterLivre(Auteur3, "Le Tour du monde en quatre-vingts jours", 7)
Littérature.acheterLivre(Auteur4, "L'etranger", 1)
print(" ")

    # Documentation
Documentation.acheterLivre(Auteur1, "Mein kampf", 1)
Documentation.acheterLivre(Auteur1, "Fifa pour les nuls", 1)
Documentation.acheterLivre(Auteur1, "The last Dance", 1)
print(" ")

# Lister le contenue des catalogues
Manga.inventaire(Manga)
Littérature.inventaire(Littérature)
Documentation.inventaire(Documentation)

# creer les clients
client1 = Client("Sylla", "Ibrahim")
client2 = Client("Kine", "Thibault")
client3 = Client("Gras", "Matthieu")
client4 = Client("Armand", "Robin")
client5 = Client("Niang", "Djibril")

# Creer les locations
client1.louer(Manga, "One Piece")
client2.louer(Manga, "Jojo Bizarre adventure")
client2.louer(Documentation, "Mein kampf")
client3.louer(Documentation, "The last Dance")
client3.louer(Littérature, "Vingt mille lieues sous les mers")
client3.louer(Littérature, "L'etranger")
client4.louer(Manga, "Naruto")
client5.louer(Manga, "One Piece")

# afficher la possession des clients
print(f'{client1.name} {client1.firstName} a loué {client1.collection_livres}')
print(" ")
print(f'{client2.name} {client2.firstName} a loué {client2.collection_livres}')
print(" ")
print(f'{client3.name} {client3.firstName} a loué {client3.collection_livres}')
print(" ")
print(f'{client4.name} {client4.firstName} a loué {client4.collection_livres}')
print(" ")
print(f'{client5.name} {client5.firstName} a loué {client5.collection_livres}')
print(" ")

# Afficher le contenue des catalogue
print(f'Dans le catalogue {Manga.nom} il reste {Manga.catalogue}')
print(" ")
print(f'Dans le catalogue {Littérature.nom} il reste {Littérature.catalogue}')
print(" ")
print(f'Dans le catalogue {Documentation.nom} il reste {Documentation.catalogue}')

# rendre les livres loués (décommenter pour tester)
Manga.rendreLivres(client1)
Manga.rendreLivres(client2)
Manga.rendreLivres(client4)
Manga.rendreLivres(client5)

Documentation.rendreLivres(client2)
Documentation.rendreLivres(client3)

Littérature.rendreLivres(client3)
