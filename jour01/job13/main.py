# Initialiser un tableau vide pour y stocker les données
numbers = []

# Demander à l'utilisateur d'entrer 5 nombres entiers
for i in range(5):
    number = int(input("Entrez un nombre entier : "))
    numbers.append(number)

# Trier les nombres par ordre croissant
numbers.sort()

# Afficher les nombres triés
print("Les nombres triés par ordre croissant sont : ")
for number in numbers:
    print(number)