import pygame
import sys
import snake
def intro():
    pygame.init()  # initializing the constructor
    res = (800, 600)  # screen resolution
    screen = pygame.display.set_mode(res)  # opens up a window
    white = (255, 255, 255)
    aqua = (0, 225, 225)
    black = (0, 0, 0)
    width = screen.get_width()  # stores the width of the screen into a variable
    height = screen.get_height()  # stores the height of the screen into a variable
    smallfont = pygame.font.SysFont('Corbel', 35)  # defining a font
    text = smallfont.render('START', True, black)  # rendering a text written in this font
    screen.fill(aqua)
    mouse = pygame.mouse.get_pos()  # stores the (x,y) coordinates of the cursor
    screen.blit(text, (width / 2, height / 2))  # superimposing the text onto our button
    pygame.display.update(snake.gameLoop())  # updates the frames of the game

    def gameMain():
            while True:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                    if ev.type == pygame.MOUSEBUTTONDOWN:  # checks if a mouse is clicked
                        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40: #if the mouse is clicked on the button the game is terminated
                            gameLoop()
    gameMain()
    intro()
