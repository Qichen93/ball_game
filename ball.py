from velocity import Velocity
import math
import pygame

class Ball(Velocity):
    def __init__(self,screen,amp=0,rad=0,angle=0,pos=(0,0),radius=10,width=0,max_speed = 20,color=(0,0,0)):
        Velocity.__init__(self,amp,rad,angle,max_speed)
        self.ball_color = color
        self.ball_acc   = Velocity(0.1,angle=90) # 小球加速度
        self.centerx    = pos[0]
        self.centery    = pos[1]
        self.radius     = radius
        self.width      = width
        self.screen     = screen

        
    def draw_ball(self):
        '''
        该函数在屏幕上绘制球体
        circle(...)
        circle(Surface, color, pos, radius, width=0) -> Rect
        draw a circle around a point
        '''
        pygame.draw.circle(self.screen,self.ball_color,(int(self.centerx),int(self.centery)),self.radius,self.width)
    
    def ball_pos_set(self,pos):
        ''' 配置小球的位置 '''
        self.centerx = pos[0]
        self.centery = pos[1]
        
    def ball_pos_get(self) :
        ''' 获得小球当前位置 '''
        return (self.centerx,self.centery)
    
    def ball_pos_update(self):
        ''' 该函数将会更新小球的位置 
            每一帧均会根据预先设定加速度计算新的速度值
            并求解新的位置所在
        '''
        # 在之前速度的基础上添加加速度
        self.velocity_vector_add(self.ball_acc)
        # 获取速度的x，y分量
        x_v,y_v = self.velocity_decompose()
        # 在当前坐标的基础上，添加坐标的增量
        self.centerx+=x_v
        self.centery+=y_v
        #print('小球坐标为{{{},{}}}'.format(self.centerx,self.centery))

    def ball_demo(self,screen_width,screen_height):
        self.draw_ball()
        x_pos = self.ball_pos_get()[0]
        y_pos = self.ball_pos_get()[1] 
        if x_pos<0 or x_pos>screen_width :
            self.velocity_reflect(math.radians(0))
            if x_pos < 0 :
                self.ball_pos_set((-x_pos,y_pos))
            else :
                self.ball_pos_set((screen_width-(x_pos-screen_width),y_pos))
                self.velocity_loss(1)
        if y_pos<0 or y_pos>screen_height :
            self.velocity_reflect(math.radians(270))
            if y_pos<0 :
                self.ball_pos_set((x_pos,-y_pos))
            else :
                self.ball_pos_set((x_pos,screen_height-(y_pos-screen_height)))
                self.velocity_loss(1)
        self.ball_pos_update()
        