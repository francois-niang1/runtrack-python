# Demander à l'utilisateur de saisir une chaîne de caractères
chaine_de_caractère = input("Veuillez saisir une chaîne de caractères : ")

# Écrire la chaîne dans un fichier "output.txt"
with open("output.txt", "w") as file:
    file.write(chaine_de_caractère)

# Afficher un message de confirmation
print(f"La chaîne '{chaine_de_caractère}' a été écrite dans le fichier 'output.txt'.")