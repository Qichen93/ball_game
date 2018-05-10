import math

class Velocity():
    ''' 该类实现二维速度类 '''
    
    def __init__(self,amp=0,rad=0,angle=0,max_speed=10):
        # 速度模值
        self.amp = amp 
        # 速度角度(如果传入angle不为0则以angle作为角度，单位为度，若为0则以rad为角度，单位为弧度)
        self.rad = rad if angle == 0 else math.radians(angle) ;  
        
        self.max_speed = max_speed
    
    
    def __add__(self,other):
        ''' 运算符重载，直接加于该速度类中，不返回新的实体 '''
        # 获取当前速度的分解值，存储于x,y中
        x_v,y_v = self.velocity_decompose()
        # 获取另一运算速度类的x,y速度
        other_x_v,other_y_v =other.velocity_decompose()
        # 将速度向量求和，并计算新的模值与角度
        x_v += other_x_v 
        y_v += other_y_v
        return Velocity(math.hypot(y_v,x_v),math.atan2(y_v,x_v))
    
    def velocity_vector_add(self,other):
        '''该函数接受另外一个速度类并与该类相加'''
        # 获取当前速度的分解值，存储于x,y中
        x_v,y_v = self.velocity_decompose()
        # 获取另一运算速度类的x,y速度
        other_x_v,other_y_v =other.velocity_decompose()
        # 将速度向量求和，并计算新的模值与角度
        x_v += other_x_v 
        y_v += other_y_v
        # 最大速度受限制
        x_v  = x_v if math.fabs(x_v) < self.max_speed else math.copysign(self.max_speed,x_v)
        y_v  = y_v if math.fabs(y_v) < self.max_speed else math.copysign(self.max_speed,y_v)
        self.amp =math.hypot(y_v,x_v)
        self.rad =math.atan2(y_v,x_v)
        
        #print('速度值为{{{},{}}}'.format(x_v,y_v))
    
    def velocity_reflect(self,norm_vec_rad):
        ''' 该函数根据传入的法线向量角度反射该速度 '''
        # 求解角度关于某一角度的反射角度，可以先法线与输入角度的角度差，然后将法线加上该角度差再加pi即可
        # 需要注意的是最后结果要关于2pi取余
        #print('当前速度角度值为:{}°'.format(math.degrees(self.rad)))
        #print('输入法线角度为：{}°'.format(math.degrees(norm_vec_rad)))
        delta    = norm_vec_rad - self.rad
        new_rad  = ( delta + norm_vec_rad + math.pi ) % ( 2 * math.pi )
        self.rad = new_rad 
        #print('反射后的速度角度为:{}°'.format(math.degrees(new_rad)))
        self.velocity_loss(1)
        
        
    def velocity_decompose(self):
        ''' 该函数将函数由向量模式分解为x,y向量模式的形式 '''
        # 返回二维元组作为
        x_v = self.amp * math.cos(self.rad)
        y_v = self.amp * math.sin(self.rad)
        return (x_v,y_v) 
        
    def velocity_loss(self,ratio):
        ''' 该函数将会根据传入的比例对速度进行衰减 '''
        self.amp *= ratio
        
    def velocity_add(self,amp):
        ''' ''' 
        self.amp += amp
    
    def velocity_map(self,rad):
        ''' 该函数将速度值映射到rad方向，其余方向分量清0 '''
        self.rad = rad
        self.amp = self.amp*cos(self.rad-rad) 
        
        
#v1 = Velocity(1,0)
#v2 = Velocity(1,angle = 90)
#v3 = v1+v2 
#v1.velocity_reflect(math.radians(45))
#v2.velocity_reflect(math.radians(45))
