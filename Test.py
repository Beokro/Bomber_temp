from Player import Player

player_up1 = 'img/n_up1.png'
player_up2 = 'img/n_up2.png'
player_up3 = 'img/n_up3.png'
player_up4 = 'img/n_up4.png'
player_down1 = 'img/n_down1.png'
player_down2 = 'img/n_down2.png'
player_down3 = 'img/n_down3.png'
player_down4 = 'img/n_down4.png'
player_left1 = 'img/n_left1.png'
player_left2 = 'img/n_left2.png'
player_left3 = 'img/n_left3.png'
player_left4 = 'img/n_left4.png'
player_right1 = 'img/n_right1.png'
player_right2 = 'img/n_right2.png'
player_right3 = 'img/n_right3.png'
player_right4 = 'img/n_right4.png'

bomb_image = 'img/bomb.png'
burst_iamge = 'img/burst.png'
back_ground_name = 'img/Background02.jpg'

import pygame
from pygame.locals import *
from sys import exit
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1024,698),0,32)

background = pygame.image.load(back_ground_name).convert()
bomb = pygame.image.load(bomb_image).convert_alpha()
bomb = pygame.transform.scale(bomb, (32,32))
burst = pygame.image.load(burst_iamge).convert_alpha()
burst = pygame.transform.scale(burst,(64,59))


player_images = [player_up1,player_up2,player_up3,player_up4,
                 player_down1,player_down2,player_down3,player_down4,
                 player_left1,player_left2,player_left3,player_left4,
                 player_right1,player_right2,player_right3,player_right4]

p = Player(player_images,50,10,20,1,1)


bomb_x = 0
bomb_y = 10
bomb_placed = False
count_down = 300
burst_happened = False
burst_x = 0
burst_y = 10
burst_count_down = 100
total_time = 0.05
current_time = 0.0
while True:    
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    current_time+=time_passed_seconds

    if(current_time>=total_time):
        current_time = 0.0
    else:
        continue
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type!=USEREVENT +1:
            continue
    

    screen.blit(background, (0,0))

    pressed_Key = pygame.key.get_pressed()

    p.Action(screen,pressed_Key,0.1)
    
        
    pygame.display.update()


print "import success"
