
import pygame
import time
import random 

snake_snelheid = 10

window_x = 720
window_y = 480

zwart = pygame.Color(0, 0, 0)
wit = pygame.Color(255, 255, 255)
rood = pygame.Color(255, 0, 0)
groen = pygame.Color(0, 255, 0)
blauw = pygame.Color(0, 0, 255)

pygame.init()
window = pygame.display.set_mode((window_x,window_y)) #window grootte
pygame.display.update()
pygame.display.set_caption('SNOK') # window naam
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
 
frames = pygame.time.Clock() # fps

snake_positie = [100, 50]
 
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]

blokje_locatie = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True
 

richting = 'RIGHT'
verander_naar = richting

score = 0

def game_over():
   
    my_font = pygame.font.SysFont('times new roman', 50)
     
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    game_over_rect = game_over_surface.get_rect()
     
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    time.sleep(2)

pygame.quit()
quit()