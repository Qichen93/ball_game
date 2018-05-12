import  sys
import  pygame
import  math
import  time

from random          import choice
from random          import randint
from ball            import Ball
from rectangle_block import Rectangle_block
from circle_block    import Circle_block
from shotline        import Shotline
from game_functions  import *

def run_game():
    pygame.init()
    pygame.display.set_caption("Ball Game")
    bg_color        = (230,230,230)
    screen_width    = 400
    screen_height   = 640
    screen          = pygame.display.set_mode((screen_width,screen_height))
    shotline        = Shotline(screen,(screen_width/2,0))
    block_list      = []
    ball_list       = []
    frame_cnt       = 0
    
    for i in range(0,5):
        block_class_type = choice([(Circle_block,2),(Rectangle_block,1)])
        block_list.append(block_class_type[0](screen,(randint(0,screen_width),randint(0,screen_height)),int(70/block_class_type[1]),20,color=(randint(0,255),randint(0,255),randint(0,255))))

    
    #测试期间初始化小球不应该与方块重合，直接将重合小球消除
    
    for block in block_list:
        for ball in ball_list:
            if block.hit_check(ball.ball_pos_get()) :
                ball_list.remove(ball)
    
    while True:
        start_time = time.time()
        #必须要获取输入，否则会卡死
        event_process(shotline)
        shot_ball(screen,shotline,ball_list)
        screen.fill(bg_color)
        for ball in ball_list :
            if ball.ball_demo(screen_width,screen_height) :
                ball_list.remove(ball)
                continue
            # 如果与小球发生碰撞
            for block in block_list:
                if block.hit_check(ball.ball_pos_get()) :
                    point = block.intersect_point_get(ball.rad,ball.ball_pos_get())
                    ball.velocity_reflect(point[2])
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
