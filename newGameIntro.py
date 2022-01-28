import pygame
import sys
pygame.init()
res = (1280, 720)
screen = pygame.display.set_mode(res)
pygame.display.set_caption('2D Snake Game')

#colour rgb values
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

width = screen.get_width()
height=screen.get_height()
smallfont = pygame.font.SysFont('Corbel', 35)
font=pygame.font.SysFont('Corbel', 35)
text = smallfont.render('Start', True, color)

#strings for rules
rules_l1= str("Welcome To 2D Snake Game")
rules_l2=str("Rules:")
rules3=str("Don't go to the edge of the Screen")
rules4=str("Collect food to increase score and make your snake grow")
rules5=str("Don't hit yourself")


while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                import snake
    screen.fill((60, 25, 60))
    mouse = pygame.mouse.get_pos()
    if width/2<= mouse[0] <= 620+140 and height/2<= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [585, height/2, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [585, height / 2, 140, 40])
    screen.blit(text, (620,height/2))
    pygame.display.update()
