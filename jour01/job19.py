def draw_rectangle(width, height):
    # Afficher les lignes intermédiaires avec des '|' à gauche et à droite
    for i in range(height):
        print("|" + "-" * (width - 2) + "|")
        
    # Afficher la première ligne du rectangle avec des '-'
    print("-" * width)


    # Afficher la dernière ligne du rectangle avec des '-'
    print("-" * width)

draw_rectangle(10, 3)