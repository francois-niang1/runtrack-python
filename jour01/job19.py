def draw_rectangle(width, height):

    # Afficher les lignes intermédiaires avec des '|' à gauche et à droite
    for i in range(height):
        if i == 0 or i == height-1:
            print("|" + "-" * (width - 2) + "|")

        else:
            print("|" + " " * (width - 2) + "|")
    

draw_rectangle(10, 3)