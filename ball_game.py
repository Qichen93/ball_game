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
def run_game():
    pygame.init()
    pygame.display.set_caption("Ball Game")
    bg_color = (230,230,230)
    screen_width = 860
    screen_height = 640
    screen   =  pygame.display.set_mode((screen_width,screen_height))
    
    block_list = []
    for i in range(0,12):
        block_class_type = choice([(Circle_block,2),(Rectangle_block,1)])
        #block_class_type = choice([(Circle_block,2)])
        block_list.append(block_class_type[0](screen,(randint(0,screen_width),randint(0,screen_height)),int(100/block_class_type[1]),20,color=(randint(0,255),randint(0,255),randint(0,255))))
    
    ball_list  = []

    for i in range(0,50):
        ball_list.append(Ball(screen,amp=randint(1,10),angle = randint(0,180),centerx=randint(0,screen_width),centery=randint(0,screen_height),color=(randint(0,255),randint(0,255),randint(0,255))))
    
    #测试期间初始化小球不应该与方块重合，直接将重合小球消除
    
    for block in block_list:
        for ball in ball_list:
            if block.hit_check(ball.ball_pos_get()) :
                ball_list.remove(ball)
    
    while True:
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
        pygame.display.flip()
        time.sleep(0.01)
        
run_game()
