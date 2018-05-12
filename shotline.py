import math
import pygame
class Shotline():
    def __init__(self,screen,pos,**kwargs) :
        '''
        由于圆形采用方程组进行求解当输入曲线为 rad = 90°，斜率无穷，难以计算，所以通过在
        ShotLine中配置使输入的角度不可以刚好为90°，rad初始值不管怎么加减都不应该直接等于90°
        '''
        self.screen     = screen                                                                               # 显示界面
        self.pos        = pos                                                                                  # 瞄准线的基准圆心
        self.x_base     = pos[0]                                                                               # 基准圆心x坐标
        self.y_base     = pos[1]                                                                               # 基准圆心y坐标
        self.rad        = math.radians(90.1)if kwargs.get('rad')       == None else kwargs.get('rad')          # 瞄准线角度
        self.length     = 20                if kwargs.get('length')    == None else kwargs.get('length')          # 每两个圆圆心间距
        self.pn         = 7                 if kwargs.get('pn')        == None else kwargs.get('pn')           # 组成瞄准线的圆形点数
        self.color      = (0,0,0)           if kwargs.get('color')     == None else kwargs.get('color')
        self.radius     = 5                 if kwargs.get('radius')    == None else kwargs.get('radius')       # 圆圈半径
        self.angle_max  = math.radians(170.1)if kwargs.get('angle_max') == None else kwargs.get('angle_max') 
        self.angle_min  = math.radians(10.1)if kwargs.get('angle_min') == None else kwargs.get('angle_min')   
        self.angle_div  = math.radians(5)   if kwargs.get('angle_div') == None else kwargs.get('angle_div') 
        self.point_list = []                                                                                    # 存储各个圆心坐标的列表
    
    def __point_gen(self):
        ''' 该函数用于生成瞄准线上的各个圆圈的圆心 '''
        x_div = self.length * math.cos( self.rad )
        y_div = self.length * math.sin( self.rad )
        self.point_list = [(int(self.x_base+x*x_div),int(self.y_base+x*y_div)) for x in range(0,self.pn) ]
        #print('瞄准线圆心队列为{}'.format(self.point_list))

    def get_base_point(self):
        ''' 该函数返回此对象的基础点  '''
        return (self.x_base,self.y_base)
    
    def set_angle(self,val):
        ''' 
            用于设置瞄准线角度的函数，当输入角度范围 
            不在预先设定的最大最小值之间则设置为边界
            值
        '''
        if ( val < self.angle_min or val > self.angle_max ):
            print('设置角度超出范围')
            #raise ValueError
        
        if ( val < self.angle_min ) :
            self.rad = self.angle_min
        elif ( val > self.angle_max ) :
            self.rad = self.angle_max 
        else :
            self.rad = val 
            
    def get_angle(self):
        ''' 用于获取角度值 '''
        return self.rad
    
    def angle_inc(self):
        ''' 瞄准线角度自增 '''
        self.rad += self.angle_div 
        self.rad  = self.rad if self.rad < self.angle_max else self.angle_max 
    
    def angle_dec(self):
        ''' 瞄准线角度自减 '''
        self.rad -= self.angle_div
        self.rad  = self.rad if self.rad > self.angle_min else self.angle_min 
        
    def draw_shotline(self):
        ''' 在屏幕上绘制瞄准线 '''
        self.__point_gen()
        for p in self.point_list :
            pygame.draw.circle(self.screen,self.color,p,self.radius,0);
        