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
    ''' 发射小球 '''
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

def draw_guide(game_controller,screen):
    ''' 绘制得分等用户界面 '''
    str_size = 30
    my_font = pygame.font.SysFont('arial',str_size)
    screen.blit(my_font.render('score : '+str(game_controller.score), True, (0,0,0)), (game_controller.screen_width-200, 0))
    screen.blit(my_font.render('balls : '+str(game_controller.ball_num), True, (0,0,0)), (game_controller.screen_width-200, str_size*1.5))

def game_logic_ctrl(game_controller):
    ''' 用于实现游戏逻辑的函数 '''
    game_controller.ball_num = 3+int(math.sqrt(game_controller.score)) 
    
    
def event_process(game_controller,shotline):
    ''' 用于处理鼠标与按键的输入函数 '''
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
                    if game_controller.shot_ready == True :
                        ball_num = game_controller.ball_num
            elif event.type == pygame.KEYUP:
                pass

def block_gen(game_controller,block_list): 
    if game_controller.add_block == True:
        game_controller.add_block = False
        #print('enter block_gen')
    else :
        return 
    #print('block_gen')
        
    ''' 控制障碍块的生成函数 '''
    # 读取参数
    max_num         = game_controller.line_block_num_max    # 每行最多的方块数
    screen_width    = game_controller.screen_width          # 屏幕宽度
    screen_height   = game_controller.screen_height         # 屏幕高度
    line_heigth     = game_controller.line_heigth           # 每行的高度
    block_size      = game_controller.block_size            # 方块的体积
    ball_num        = game_controller.ball_num
    block_radius    = int(block_size/2)
    screen          = game_controller.screen
    # 随机生成下一行要生成的块数
    block_num       = randint(1,max_num) 
    
    # 根据窗口宽计算每个方块平均占有的宽度
    average_width   = int(screen_width / block_num)
    
    # 再添加新的方块前要把之前残留的方块全部上移
    for block in block_list :
        block.move((0,-line_heigth))
    
    # 通过以上操作把每行分解为 宽度为 average_width 高度为 line_heigth，且个数为block_num的块
    # 新添加的方块需要在这些区域中，而下面的计算将会随机的将方块的几何中心放置在方块中（且必须
    # 保证方块完全在可行区域内）
    
    pos_list = [(x*average_width+randint(block_radius,average_width-block_radius),screen_height-randint(block_radius,line_heigth-block_radius)) for x in range(0,block_num)]
    
    for pos in pos_list :
        color=(randint(0,255),randint(0,255),randint(0,255))
        block_num = randint(int(ball_num*0.8),int(ball_num*1.5))
        block_class_type = choice([Circle_block,Rectangle_block])
        block_list.append(block_class_type(screen,pos,block_size,block_num,color))

def failure_check(gc):
    ''' 用于检测是否有方块达到顶端，若达到最顶端则游戏结束 '''
    for block in gc.block_list :
        y_val = block.get_pos()[1]
        if y_val < gc.screen_height-gc.dieline * gc.line_heigth :
            draw_failure_console(gc)
    
def draw_failure_console(gc):
    ''' 绘制失败窗口 '''
    str_size = 60
    my_font = pygame.font.SysFont('arial',str_size)
    gc.screen.blit(my_font.render(' Game Over !', True, (0,0,0)), (50, 200))
    gc.screen.blit(my_font.render('Your Score : '+str(gc.score), True, (0,0,0)), (50, 300))
    
    
    
    
def check_send_ready(game_controller,ball_list):
    ''' 
        检测是否可以发射子弹:
            若len(ball_list)==0代表之前发射的子弹全部
        从界面中消失，可以准备下一次发射
    '''
    if len(ball_list) == 0 :
        if not game_controller.shot_ready : 
            game_controller.add_block = True 
        game_controller.shot_ready = True
    else :
        game_controller.shot_ready = False
        
    #print(game_controller.shot_ready)
     