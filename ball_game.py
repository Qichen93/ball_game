import sys
import pygame
import math
import time
from random import choice
from random import randint
from ball import Ball
#from block import Block
from rectangle_block import Rectangle_block
from circle_block import Circle_block
from shotline import Shotline

time_cnt = 0
ball_max = 20

def shot_ball(screen,shotline,ball_list):
    global time_cnt
    global ball_max
    if ball_max == 0 :
        return
    time_cnt += 1
    if time_cnt > 5 :
        ball_max -=1
        time_cnt = 0 
        radians=shotline.get_angle()
        base_point = shotline.get_base_point()
        ball_list.append(Ball(screen,amp=5,rad =radians,pos=base_point,color=(randint(0,255),randint(0,255),randint(0,255))))

def run_game():
    pygame.init()
    pygame.display.set_caption("Ball Game")
    bg_color = (230,230,230)
    screen_width = 860
    screen_height = 640
    screen   =  pygame.display.set_mode((screen_width,screen_height))
    shotline = Shotline(screen,(screen_width/2,0),rad=math.radians(100))
    block_list = []
    ball_list  = []
    frame_cnt  = 0
    
    for i in range(0,15):
        block_class_type = choice([(Circle_block,2),(Rectangle_block,1)])
        #block_class_type = choice([(Circle_block,2)])
        block_list.append(block_class_type[0](screen,(randint(0,screen_width),randint(0,screen_height)),int(100/block_class_type[1]),20,color=(randint(0,255),randint(0,255),randint(0,255))))

    #for i in range(0,30):
    #    ball_list.append(Ball(screen,amp=randint(1,10),angle = randint(0,180),centerx=randint(0,screen_width),centery=randint(0,screen_height),color=(randint(0,255),randint(0,255),randint(0,255))))
    
    
    #测试期间初始化小球不应该与方块重合，直接将重合小球消除
    
    for block in block_list:
        for ball in ball_list:
            if block.hit_check(ball.ball_pos_get()) :
                ball_list.remove(ball)
    
    while True:
        start_time = time.time()
        shot_ball(screen,shotline,ball_list)
        screen.fill(bg_color)
        for ball in ball_list :
            ball.ball_demo(screen_width,screen_height)
            # 如果与小球发生碰撞
            for block in block_list:
                if block.hit_check(ball.ball_pos_get()) :
                    point = block.intersect_point_get(ball.rad,ball.ball_pos_get())
                    #ball.ball_pos_set((point[0],point[1]))
                    ball.velocity_reflect(point[2])
                    #ball.ball_pos_update()
                    #ball.velocity_add(0.1)
        for block in block_list:   
            block.draw_block()
            if block.num <= 0 :
                block_list.remove(block)
        shotline.draw_shotline()
        pygame.display.flip()
        time.sleep(0.02)
        time_interval = time.time() - start_time
        frame_cnt += 1
        if frame_cnt > 100 :
            print('游戏帧率为{}Hz'.format(1/time_interval) )
            frame_cnt = 0 
run_game()
