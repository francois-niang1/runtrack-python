import pygame

# Initialiser Pygame
pygame.init()

# Définir la taille de la fenêtre
size = (600, 600)

# Créer la fenêtre
screen = pygame.display.set_mode(size)

# Nommer la fenêtre
pygame.display.set_caption("TicTacToe1337")

# Définir les couleurs
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Définir la police
font = pygame.font.Font(None, 50)

# Définir le jeu
game_board = [['', '', ''], ['', '', ''], ['', '', '']]
player = 'X'
winner = None
draw = False

# Boucle de jeu
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not winner and not draw:
            # Récupérer la position de la souris
            pos = pygame.mouse.get_pos()
            x = pos[0] // 200
            y = pos[1] // 200
            # Vérifier si la case est vide
            if game_board[y][x] == '':
                game_board[y][x] = player
                # Vérifier s'il y a un gagnant ou un match nul
                for i in range(3):
                    if game_board[i][0] == game_board[i][1] == game_board[i][2] != '':
                        winner = game_board[i][0]
                    elif game_board[0][i] == game_board[1][i] == game_board[2][i] != '':
                        winner = game_board[0][i]
                if game_board[0][0] == game_board[1][1] == game_board[2][2] != '':
                    winner = game_board[0][0]
                elif game_board[0][2] == game_board[1][1] == game_board[2][0] != '':
                    winner = game_board[0][2]
                if not winner:
                    draw = all(game_board[i][j] != '' for i in range(3) for j in range(3))
                # Changer de joueur
                player = 'O' if player == 'X' else 'X'

    pygame.display.flip()

    # Dessiner le fond
    screen.fill(white)

    # Dessiner le jeu
    for i in range(3):
        for j in range(3):
            rect = pygame.Rect(j * 200, i * 200, 200, 200)
            pygame.draw.rect(screen, black, rect, 3)
            text = font.render(game_board[i][j], True, black)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)
        

    # Afficher le gagnant ou le match nul
    if winner:
        text = font.render(f'{winner} a gagné!', True, red)
        text_rect = text.get_rect(center=(300, 550))
        screen.blit(text, text_rect)
    elif draw:
        text = font.render('Match nul!', True, blue)
        text_rect = text.get_rect(center=(300, 550))
        screen.blit(text, text_rect)

# Rafraîchir l'affichage
pygame.display.flip()
