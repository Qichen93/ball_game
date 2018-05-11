import math
import pygame
import time
from block import Block
class Circle_block(Block):
    def __init__(self,screen,pos,size,num,color=(0,0,0)):
        Block.__init__(self,screen,pos,size,num,color)
        self.param_init()
    
    def param_init(self):
        self.radius = self.size
        self.pos    = (self.centerx,self.centery)
        
    def draw_block(self):
        ''' 将图形绘制在屏幕上 
            绘制圆形函数
            circle(...)
            circle(Surface, color, pos, radius, width=0) -> Rect
            draw a circle around a point
        '''  
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,0)
        # 绘制num数到圆形上
        self.draw_num()    
    
    def intersect_point_get(self,rad,pos,show_intersect_point= False):
        '''
            用于检测碰撞点
            圆方程     ：(x-a)^2 +(y-b)^2 = r^2
            直线方程   ：y=kx+c
            1. (x-a)^2 + (kx+c-b)^2 = r^2 设 c-b = d
            2. x^2 -2ax + a^2 + (k^2)*(x^2) +2kdx + d^2 = r^2
            3. (k^2+1)*x^2+(2kd-2a)*x +(a^2 + (c-b)^2 - r^2) = 0 
            4. c1*x^2 + c2*x + c3 = 0  
               c1 = (k^2+1) ; c2 = (2kd-2a) ; c3 = (a^2+(c-b)^2-r^2)
            ----------------------------------------------------------
            2018-5-11 : 修复上一版本坐标计算错误，上一版本x与对应的y值
                        组合错误。
                        添加参数show_intersect_point,设置为True后可以观
                        看每次碰撞时的小球，圆形与入射曲线细节图，每幅
                        图持续时间1s。
        '''
        a = self.centerx
        b = self.centery
        r = self.radius
        # 计算方程 y = kx + c
        # 直线斜率等于tan值
        k = math.tan(rad)
        # y=kx+c 求c 需使用 c = y - k*x
        c = pos[1] - k * pos[0] 
        #print('小球轨迹入射曲线为：y = {0:.3f}x + {1:.3f}'.format(a,b))
        
        # c1*x^2 + c2*x + c3 = 0
        c1 = (k**2+1)
        c2 = 2*(k*(c-b)-a)
        c3 = ( a**2 + (c-b)**2 - r**2 )
        #print ('c1={},c2={},c3={}'.format(c1,c2,c3))
        #
        delta = c2**2 - 4*c1*c3 
        if delta < 0 :
            return (0,0,0)
        delta_sqrt = math.sqrt( delta )
        x1 = ( -c2 + delta_sqrt ) / ( 2 * c1 )
        x2 = ( -c2 - delta_sqrt ) / ( 2 * c1 )
        
        # 两个x值每个x都对应这两个y要选择正确的y作为交点，需要根据直线斜率来判断究竟是哪个交点
        # y = (+/-)sqrt(r^2-(x-a)^2) + b
        y1_1 = math.sqrt((self.radius**2 - (x1-a)**2)) + b
        y1_2 = -math.sqrt((self.radius**2 - (x1-a)**2)) + b
        y2_1 = math.sqrt((self.radius**2 - (x2-a)**2)) + b
        y2_2 = -math.sqrt((self.radius**2 - (x2-a)**2)) + b
        
        # 若 k>=0 先小后大反之先达后小 
        #point_list = [(x2,y1_2),(x1,y2_1)] if k>=0 else [(x2,y1_1),(x1,y2_2)]
        #print('直线与圆形交点为{}',point_list)
        
        # 根据pos与四个点的距离来判断，将最近的点作为碰撞点
        point_list=[(x1,y1_1),(x1,y1_2),(x2,y2_2),(x2,y2_1)]
        point_list.sort(key=lambda p:(math.hypot((p[0]-pos[0]),(p[1]-pos[1]))))
        
        if show_intersect_point :
            for p in point_list :
                pygame.draw.circle(self.screen,[x^((1<<8)-1) for x in self.color],[int(x) for x in p],10,0)
                pygame.draw.circle(self.screen,self.color,self.pos,self.radius,1)
                pygame.draw.line(self.screen,self.color, pos, (pos[0]+math.cos(rad)*100,pos[1]+math.sin(rad)*100), 3)
                pygame.display.flip()
            time.sleep(1)
        # 若x_v>0小球入射由左至右，选择左侧交点，反之右侧

        intersect_point=list(point_list[0])
        # 由交点与圆心计算法线角度
        norm_rad = math.atan((self.centery-intersect_point[1])/(self.centerx-intersect_point[0]))
        # 将交点沿反速度方向再移动半径长度，防止反射时误触发多次反射
        intersect_point[0]=intersect_point[0]-math.cos(rad)*self.radius
        intersect_point[1]=intersect_point[1]-math.sin(rad)*self.radius
        return (intersect_point[0],intersect_point[1],norm_rad)
        #return intersect_point
        
    
    def hit_check(self,pos):
        '''
            用于检测某物体是否与该方块发生碰撞
            检测是传入的点是否在半径内
            (x-a)**2 + (y-b)**2 <= r**2
        '''
        ishit=( ( pos[0] - self.centerx ) ** 2 + ( pos[1] - self.centery ) ** 2 <= self.radius ** 2 )
        if ishit and self.num >0 :
            self.num-=1
            #print('碰撞检测!')
        return ishit 
  
        