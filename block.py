import math
import pygame
class Block():
    def __init__(self,screen,pos,size,num,color=(0,0,0)):
        self.screen = screen
        self.centerx= pos[0]
        self.centery= pos[1]
        self.size   = size 
        self.num    = num
        self.color  = color
        # 配置一些与该形状相关的参数
        self.param_init()
        #self.draw_block()
    
    def param_init(self):
        print('父类Block param_init 函数调用，未在子类被重写') 

    def draw_block(self):
        ''' 
            将图形绘制在屏幕上 
        '''  
        print('父类Block draw_block 函数调用，未在子类被重写') 
        
    def draw_num(self):
        ''' 
            使用 pygame.font 类
            中的render方法，用法如下：
            render(...)
            render(text, antialias, color, background=None) -> Surface
            draw text on a new Surface
            blit(...)
            blit(source, dest, area=None, special_flags = 0) -> Rect
            draw one image onto another
        '''
        str_size = 30
        num_str = str(self.num)
        str_x_pixel = str_size/2*len(num_str) # 求出字符串的像素宽
        str_y_pixel = str_size                # 求出字符串像素高
        (str_pos_x,str_pos_y) = (self.centerx-str_x_pixel/2,self.centery-str_y_pixel/2)
        my_font = pygame.font.SysFont('arial',str_size)
        self.screen.blit(my_font.render(str(self.num), True, (255,255,255)), (str_pos_x, str_pos_y))
    
    def intersect_point_get(self,rad,pos):
        '''
            用于检测碰撞点
        '''
        print('父类Block intersect_point_get 函数调用，未在子类被重写') 
        return (0,0,0)
        
    
    def hit_check(self,pos):
        '''
            用于检测某物体是否与该方块发生碰撞
        '''
        print('父类Block hit_check 函数调用，未在子类被重写')     
            
            


        