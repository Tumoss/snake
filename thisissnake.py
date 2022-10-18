
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

pygame.quit()
quit()