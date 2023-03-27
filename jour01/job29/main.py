def listeArrondie(note):
    return [note, note + 1 , note + 2]

def Arrondie(note):
    notes = listeArrondie(note)
    if note < 40:
        print ("l'étudiant a échoué le controle")
    
    else:
        for testNote in notes:
            if testNote % 5 == 0:
                return testNote
        return note

note = input("Entrez une note : ")
note = int(note)
print('La note arrondie est : ' + str(Arrondie(note)) + '/100')
