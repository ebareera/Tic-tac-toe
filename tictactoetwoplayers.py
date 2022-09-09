def drawscreen():
    screen = pygame.display.set_mode((300,330))
    pygame.display.set_caption ('Tic-Tac-Toe')
    screen.fill ((0, 0, 0))
    pygame.draw.line (screen, (250,250,250), (100, 0), (100, 300), 4)
    pygame.draw.line (screen, (250,250,250), (200, 0), (200, 300), 4)
    pygame.draw.line (screen, (250,250,250), (0, 100), (300, 100), 4)
    pygame.draw.line (screen, (250,250,250), (0, 200), (300, 200), 4)
    pygame.display.flip()
    stop = False
    xo = 'x'
    occupied = [['','',''],['','',''],['','','']]
    winner = None
    message = xo + "'s turn  "
    font = pygame.font.SysFont("consolas", 24)
    newscreensurf = font.render("New Game?", 1, (250,0,0), (250,250,250))
    screen.blit(newscreensurf,(170,300))
    return screen,stop,xo,occupied,winner,message,font
    
def drawxo(xo,centrepos):
    if xo is 'x':
        pygame.draw.line(screen, (250,250,250), (centrepos[0]-30,centrepos[1]-30), (centrepos[0]+30,centrepos[1]+30), 5)
        pygame.draw.line(screen, (250,250,250), (centrepos[0]+30,centrepos[1]-30), (centrepos[0]-30,centrepos[1]+30), 5)
        xo = 'o'
    else:
        pygame.draw.circle(screen, (250,250,250), centrepos, 35, 5)
        xo = 'x'
    return xo
def winnercheck(occupied):
    if occupied[0][0]==occupied[0][1]==occupied[0][2] and occupied[0][0] is not '':
        winner = occupied[0][0]
        pygame.draw.line(screen, (250,0,0), (5,50), (295,50), 10)
    elif occupied[1][0] == occupied[1][1] == occupied[1][2] and occupied[1][0] is not '':
        winner = occupied[1][0]
        pygame.draw.line(screen, (250,0,0), (5,150), (295,150), 10)
    elif occupied[2][0] == occupied[2][1] == occupied[2][2] and occupied[2][0] is not '':
        winner = occupied[2][0]
        pygame.draw.line(screen, (250,0,0), (5,250), (295,250), 10)
    elif occupied[0][0] == occupied[1][0] == occupied[2][0] and occupied[0][0] is not '':
        winner = occupied[0][0]
        pygame.draw.line(screen, (250,0,0), (50,5), (50,295), 10)
    elif occupied[0][1] == occupied[1][1] == occupied[2][1] and occupied[0][1] is not '':
        winner = occupied[0][1]
        pygame.draw.line(screen, (250,0,0), (150,5), (150,295), 10)
    elif occupied[0][2] == occupied[1][2] == occupied[2][2] and occupied[0][2] is not '':
        winner = occupied[0][2]
        pygame.draw.line(screen, (250,0,0), (250,5), (250,295), 10)
    elif occupied[0][0] == occupied[1][1] == occupied[2][2] and occupied[0][0] is not '':
        winner = occupied[0][0]
        pygame.draw.line(screen, (250,0,0), (5,5), (295,295), 10)
    elif occupied[0][2] == occupied[1][1] == occupied[2][0] and occupied[0][2] is not '':
        winner = occupied[0][2]
        pygame.draw.line(screen, (250,0,0), (295,5), (5,295), 10)
    else:
        winner = None
    return winner

import pygame
pygame.init()
screen,stop,xo,occupied,winner,message,font = drawscreen()

while not stop:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            stop = True
        elif event.type is pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX < 100:
                col = 0
            elif mouseX < 200:
                col = 1
            else:
                col = 2

            if mouseY < 100:
                row = 0
            elif mouseY < 200:
                row = 1
            elif mouseY < 300:
                row = 2
            elif mouseX > 170:
                screen,stop,xo,occupied,winner,message,font = drawscreen()
                continue
            if occupied[row][col] is '' and winner is None:
                occupied [row][col] = xo
                centrepos = ((col * 100 + 50),(row * 100 + 50))
                xo = drawxo(xo,centrepos)
                message = xo + "'s turn  "
                winner = winnercheck(occupied)

            if len(''.join(occupied[0]+occupied[1]+occupied[2])) is 9 and winner is None:
                message = "Draw!     "
            if winner is not None:
                message = winner + " won     "
                
        messagesurf = font.render(message, 1, (0, 0, 0),(250,250,250))
        screen.blit(messagesurf, (10, 300))
        pygame.display.flip()
        
pygame.quit()
