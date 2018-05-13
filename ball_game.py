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
from game_controller import Game_controller

def run_game():
    pygame.init()
    pygame.display.set_caption("Ball Game")
    game_ctrl       = Game_controller()
    bg_color        = game_ctrl.bg_color     
    screen_width    = game_ctrl.screen_width 
    screen_height   = game_ctrl.screen_height
    screen          = game_ctrl.screen
    shotline        = Shotline(screen,(screen_width/2,0))
    game_ctrl       = Game_controller()
    block_list      = game_ctrl.block_list
    ball_list       = game_ctrl.ball_list
    frame_cnt       = 0
    
    #测试期间初始化小球不应该与方块重合，直接将重合小球消除
    
    while True:
        start_time = time.time()
        #必须要获取输入，否则会卡死
        event_process(game_ctrl,shotline)
        check_send_ready(game_ctrl,ball_list)
        block_gen(game_ctrl,block_list)
        shot_ball(screen,shotline,ball_list)
        screen.fill(bg_color)
        for ball in ball_list :
            if ball.ball_demo(screen_width,screen_height) :
                ball_list.remove(ball)
                continue
            # 如果与小球发生碰撞
            for block in block_list:
                if block.hit_check(ball.ball_pos_get()) :
                    game_ctrl.score += 1
                    point = block.intersect_point_get(ball.rad,ball.ball_pos_get())
                    ball.velocity_reflect(point[2])
        for block in block_list:   
            block.draw_block()
            if block.num <= 0 :
                block_list.remove(block)
        shotline.draw_shotline()
        draw_guide(game_ctrl,screen)
        game_logic_ctrl(game_ctrl)
        failure_check(game_ctrl)
        pygame.display.flip()
        time.sleep(1/game_ctrl.frame_rate_ctrl)
        time_interval = time.time() - start_time
        frame_cnt += 1
        if frame_cnt > 100 :
            print('游戏帧率为{}Hz'.format(1/time_interval) )
            frame_cnt = 0 
run_game()
