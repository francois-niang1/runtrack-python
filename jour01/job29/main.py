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