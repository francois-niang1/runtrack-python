# def listeArrondie(note):
#     return [note, note + 1 , note + 2]

# def Arrondie(note):
#     notes = listeArrondie(note)
#     if note < 40:
#         print ("l'étudiant a échoué le controle")
    
#     else:
#         for testNote in notes:
#             if testNote % 5 == 0:
#                 return testNote
#         return note

# note = input("Entrez une note : ")
# note = int(note)
# print('La note arrondie est : ' + str(Arrondie(note)) + '/100')


def skywalk(note):
    liste = []
    d = 0

    # Parcourir tous les elements de la liste
    for i in note :
        d = i

        # Cas de recalage
        if i < 40:
            liste.append('recalé')
        
        # Verifier si l'element est compris dans l'intervalle multiple de 5 - 3 et multiplede 5
        else :
            for j in range(12):
                # Condition d'arrondissement
                if i > 42 + 5 * j and i < 45 + 5 * j:
                    d = 40 + 5 * (j+1)
            liste.append(d)
    return liste

print(skywalk([51, 52, 53, 54, 55]))