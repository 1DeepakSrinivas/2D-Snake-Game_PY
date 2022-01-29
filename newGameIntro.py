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
rules_l1= smallfont.render("Welcome to 2D Snake Game",True,white)
rules_l2=smallfont.render("Rules:",True,white)
rules3=smallfont.render("⨀ Don't go outside the Screen",True,white)
rules5=smallfont.render("⨀ Don't collide into yourself",True,white)


while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN: # To register start button click
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                import snake
    screen.fill((60, 25, 60))
    mouse = pygame.mouse.get_pos()
    if width/2<= mouse[0] <= 620+140 and height/2<= mouse[1] <= height / 2 + 40: # to change colour of button when hovering
        pygame.draw.rect(screen, color_light, [585, height/2, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [585, height / 2, 140, 40])
    screen.blit(text, (620,height/2))
    screen.blit(rules_l1, (450, 100))
    screen.blit(rules_l2, (600, 200))
    screen.blit(rules3, (450, 250))
    screen.blit(rules5, (450, 300))
    pygame.display.update()
