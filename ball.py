from velocity import Velocity
import math
import pygame

class Ball(Velocity):
    def __init__(self,screen,amp=0,rad=0,angle=0,centerx=0,centery=0,radius=10,width=0,max_speed = 20,color=(0,0,0)):
        Velocity.__init__(self,amp,rad,angle,max_speed)
        self.ball_color = color
        self.ball_acc   = Velocity(0.2,angle=90) # 小球加速度
        self.centerx    = centerx
        self.centery    = centery
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
            #self.ball_pos_update()
            '''
                此处出现设计失误，原始程序在球体反弹过程中检测若球体坐标超出范围则直接将其
                对齐范围，且速度取反射后的速度，但是这样会造成一部分能量泄露，所以需要采用
                的标准方式是，当检测到球体坐标超出范围内，需要将其超出范围部分的位移关于边
                界进行对称，这样就可以避免能量丢失。
                在最大速度限制设置时，应该满足一定要求，或者不设，因为速度最大值可能导致一
                部分能量在速度到达最大值后丢失。
            '''
            if y_pos<0 :
                self.ball_pos_set((x_pos,-y_pos))
            else :
                self.ball_pos_set((x_pos,screen_height-(y_pos-screen_height)))
                self.velocity_loss(1)
                #print('当前小球速度为{{x_v={0[0]},y_v={0[1]}}}'.format(self.velocity_decompose()))
        self.ball_pos_update()
        