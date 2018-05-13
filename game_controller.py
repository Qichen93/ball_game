import math
import pygame

class Game_controller():
    
    def __init__(self):
        self.ball_num           = 3
        self.score              = 0 
        self.bg_color           = (230,230,230)
        self.screen_width       = 500
        self.screen_height      = 800
        self.ball_num           = 3
        self.frame_rate_ctrl    = 100
        self.dieline            = 6             # 当有方块出现在该层时游戏结束
        self.line_block_num_max = 4             # 每行出现的最大块数
        self.block_size         = 70            # 方块或圆形的体积  
        self.line_heigth        = 120           # 每行方块的数据
        self.shot_ready         = True          # 已经准备就绪可以发射圆球
        self.add_block          = True          # 添加block
        self.screen             = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.block_list         = []
        self.ball_list          = []
        self.failed             = False         # 游戏是否失败