
import pygame
import time
import random
 
snake_snelheid = 10
 
window_x = 720
window_y = 480
 
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
pygame.init()
 
pygame.display.set_caption('SNAKE')
game_window = pygame.display.set_mode((window_x, window_y))
 
fps = pygame.time.Clock()
 
snake_positie = [100, 50]
 
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

fruit_locatie = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 

richting = 'RIGHT'
verander_richting = richting
 

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
 
 
while True:
     
  
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                verander_richting = 'UP'
            if event.key == pygame.K_DOWN:
                verander_richting = 'DOWN'
            if event.key == pygame.K_LEFT:
                verander_richting = 'LEFT'
            if event.key == pygame.K_RIGHT:
                verander_richting = 'RIGHT'
 
    if verander_richting == 'UP' and richting != 'DOWN':
        richting = 'UP'
    if verander_richting == 'DOWN' and richting != 'UP':
        richting = 'DOWN'
    if verander_richting == 'LEFT' and richting != 'RIGHT':
        richting = 'LEFT'
    if verander_richting == 'RIGHT' and richting != 'LEFT':
        richting = 'RIGHT'
 
    if richting == 'UP':
        snake_positie[1] -= 10
    if richting == 'DOWN':
        snake_positie[1] += 10
    if richting == 'LEFT':
        snake_positie[0] -= 10
    if richting == 'RIGHT':
        snake_positie[0] += 10
 
   
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))

 
    if snake_positie[0] < 0 or snake_positie[0] > window_x-10:
        game_over()
    if snake_positie[1] < 0 or snake_positie[1] > window_y-10:
        game_over()
 
    for block in snake_body[1:]:
        if snake_positie[0] == block[0] and snake_positie[1] == block[1]:
            game_over()
 
 
    pygame.display.update()
 
    fps.tick(snake_snelheid)