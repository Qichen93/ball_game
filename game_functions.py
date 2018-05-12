import math
import velocity
import pygame
from ball import Ball
from random import choice
from random import randint
from ball import Ball
from rectangle_block import Rectangle_block
from circle_block import Circle_block
from shotline import Shotline
from game_functions import *
time_cnt = 0
ball_num = 0

def shot_ball(screen,shotline,ball_list):
    global time_cnt
    global ball_num
    if ball_num == 0 :
        return
    time_cnt += 1
    if time_cnt > 5 :
        ball_num -=1
        time_cnt = 0 
        radians=shotline.get_angle()
        base_point = shotline.get_base_point()
        ball_list.append(Ball(screen,amp=8,rad =radians,pos=base_point,color=(randint(0,255),randint(0,255),randint(0,255))))

def event_process(shotline):
    global ball_num 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: #键被按下
                if event.key == pygame.K_LEFT:
                    shotline.angle_inc()
                elif event.key == pygame.K_RIGHT:
                    shotline.angle_dec()
                elif event.key == pygame.K_UP:
                    pass 
                elif event.key == pygame.K_DOWN:
                    ball_num = 5
            elif event.type == pygame.KEYUP:
                pass
        