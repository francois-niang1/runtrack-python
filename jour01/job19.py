def draw_rectangle(width, height):

    # Afficher les lignes 
    for i in range(height):

# afficher les premier et derniere ligne 
        if i == 0 or i == height-1:
            print("|" + "-" * (width - 2) + "|")

# afficher les lignes intermediaires
        else:
            print("|" + " " * (width - 2) + "|")
    

draw_rectangle(10, 3)