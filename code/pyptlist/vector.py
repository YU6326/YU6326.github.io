from pyautocad import APoint,distance
from math import *
import pyptlist.main

"""
有平面解析几何的基本功能
基本元素
点:APoint
向量:Vector，与直线的功能类似
"""

class Vector(APoint):
    """
    线：有方向
    """
    def __new__(cls,p1:APoint,p2:APoint=None):
        if p1==p2 or p1==APoint(0,0) and p2==None:
            raise ValueError("直线长度为0")
        if p2:
            return super().__new__(cls,p2-p1)
        else:
            return super().__new__(cls,p1)
    def __init__(self,p1,p2=None):
        if p2:
            self.begin=p1
            self.end=p2
        else:
            self.begin=APoint(0,0)
            self.end=p1
        self.A=self[1]
        self.B=-self[0]
        self.C=self.end[0]*self.begin[1]-self.begin[0]*self.end[1]
    
    def __eq__(self,obj):
        return self==obj

    @property
    def norm(self):
        return distance(self,APoint(0,0,0))

    def angle(self,*vecli):#返回0到2pi之间的夹角或极角
        if not vecli:
            t=atan2(self.y,self.x)
            if t<0:
                t+=2*pi
            return t
        else:
            thetalist=[]
            for vec in vecli:
                t=atan2(vec.y,vec.x)-atan2(self.y,self.x)
                if t<0:
                    t=t+2*pi
                thetalist.append(t)
            # if len(vecli)==1:
            #     return thetalist[0]
            return tuple(thetalist)

    @property
    def direction(self):#返回3个方向余弦,直线的方向向量
        return self/self.norm
    
    def distance_to(self,po:APoint):
        return abs(po.x*self.A+po.y*self.B+self.C)/sqrt(self.A**2+self.B**2)

    def distance_to_line(self,vec):
        if self.direction==vec.direction or self.direction==-vec.direction:
            return abs(self.C-vec.C)/sqrt(self.A**2+self.B**2)
        else:
            raise ValueError("Two lines are not parallel")

    def perpendicular(self,po:APoint):
        if self.Contains(po):
            return po
        else:
            proj=self.proj(po)
            return APoint(proj*self.direction.x,proj*self.direction*y)+self.begin
    
    def proj(self,po):
        """
        返回投影纯量
        po:APoint/Vector
        """
        if type(po)==APoint:
            vec=Vector(self.begin,po)
        elif type(po)==Vector:
            vec=po
        return self.dot(vec)/self.norm
    
    def proj_vec(self,po):
        """
        po:(APoint,Vector)
        返回投影向量
        """
        proj=self.proj(po)
        return proj*self.direction

    
    def dot(self,vec):
        """
        vec:Vector
        """
        return self[0]*vec[0]+self[1]*vec[1]+self[2]*vec[2]

    def normal(self):#返回平面直线的单位法向量
        return APoint(-v2,v1)/self.norm

            
    def Contains(self,po:APoint):
        """
        在直线
        左延长线：1
        起点：2
        线段上不含端点：3
        终点：4
        右延长线：5
        不在直线上：0
        """
        if po==self.begin:
            return 2
        elif po==self.end:
            return 4
        vec=Vector(self.begin,po)
        if vec.direction==self.direction:
            if abs(vec.x)<abs(self.x):
                return 3
            else:
                return 5
        elif vec.direction==-self.direction:
            return 1
        else:
            return 0
    
    def side(self,po:APoint):
        """
        左：-1，直线上：0，右：1
        """
        t=self.A*po.x+self.B*po.y+self.C
        if t>0:
            return 1
        elif t<0:
            return -1
        else:
            return 0
    
    def intersect(self,other):
        """
        other:Vector
        返回交点坐标
        """
        if self.direction==other.direction or self.direction==-other.direction:
            raise ValueError("无交点")
        else:
            D=self.A*other.B-self.B*other.A
            D1=-(self.C*other.B-self.B*other.C)
            D2=-(self.A*other.C-self.C*other.A)
            return APoint(D1/D,D2/D)
    
    def divide(self,lamb):
        """
        定比分点：
        AP=lamb*PB
        """
        return (self.begin+lamb*self.end)/(1+lamb)

    def measure(self,length):
        """
        L为到1点的代数长
        """
        return APoint(self.begin.x+self.direction[0]*length,
                    self.begin.y+self.direction[1]*length)
    
    def dist_intersect(self,r1,r2,tagRight=True):
        """
        返回右方/左方交汇点坐标
        """
        t=r1+r2-self.norm
        if t<0:
            return None
        elif t==0:
            return self.divide(1)
        else:
            h=(self.norm**2+r1**2-r2**2)/(2*self.norm)
            L=sqrt(r1**2-h**2)
            if tagRight==False:
                L=-L
            ang=self.angle()-pi/2
            return self.begin+pyptlist.main.rotate(ang).transform(APoint(L,h))

    
if __name__=="__main__":
    p1=APoint(1,0)
    p2=APoint(0,2)
    p3=APoint(-1,0)
    vec1=Vector(p2,p1)
    vec2=Vector(p2,p3)
    apo=vec1.intersect(vec2)



    
    
            

