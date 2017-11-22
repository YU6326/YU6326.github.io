"""
    pyptlist.main
    ~~~~~~~~~~~~~~~    

    :copyright: (c) 2017 by YU Zhouwei
    :license: MIT
"""

from pyautocad import Autocad,APoint,distance,aDouble
import array
from math import *
import sys
import numpy as np
from pyptlist.vector import *



def MoveDupAPoint(ptl):
    """
    将APoint组成的列表去重,且保持顺序
    """
    # 不能用list(set()),因为作为键的只能是值对象，引用对象not hashable
    # 不能用in 判断是否在里面，因为pyautocad包里面没有写此方法
    ptl2=[ptl[0]]
    for i in range(1,len(ptl)):
        for item in ptl2:
            if ptl[i]==item:
                break
        else:ptl2.append(ptl[i])
    return ptl2




class PointSet(tuple):
    def __new__(cls,coor,tagMoveDup=False):
        """用得到的多义线坐标表生成该点表"""
        if isinstance(coor,(list,tuple,array.array)):
            mylist=[]
            if isinstance(coor[0],(float,int)):#如果是直接的坐标表，即x0,y0,x1,y1
                for i in range(0,len(coor),2):
                    mylist.append(APoint(coor[i],coor[i+1]))
                if tagMoveDup:#去除重复元素
                    mylist=MoveDupAPoint(mylist)
                return super(PointSet,cls).__new__(cls,mylist)
            elif len(coor[0])==3:#已经是APoint数组了
                mylist=coor
                if tagMoveDup:#去除重复元素
                    mylist=MoveDupAPoint(mylist)
                return super(PointSet,cls).__new__(cls,mylist)

    def __init__(self,coor,tagMoveDup=False):
        self.L=len(self)
    
    def GetBoundingBox(self):
        """
        返回左下角点和右上角点的坐标
        """
        coorx=[]
        coory=[]
        for item in self:
            coorx.append(item[0])
            coory.append(item[1])
        return APoint(min(coorx),min(coory)),APoint(max(coorx),max(coory))
    
    @property
    def Center(self):
        cenx=0
        ceny=0
        for item in self:
            cenx+=item.x
            ceny+=item.y
        cenx,ceny=cenx/self.L,ceny/self.L
        return APoint(cenx,ceny)
    
    @property
    def Topleft(self):
        min0,max0=self.GetBoundingBox()
        return APoint(min0[0],max0[1])

    @property
    def Bottomleft(self):
        return self.GetBoundingBox()[0]
    
    @property
    def Topright(self):
        return self.GetBoundingBox()[1]

    @property    
    def Bottomright(self):
        min0, max0 = self.GetBoundingBox()
        return APoint(min0[1], max0[0])
    
    def distance_to(self,apoint:APoint):
        lenlist=[]
        for item in self:
            lenlist.append(distance(item, apoint))
        return lenlist

    def Transform(self,matrix):
        """transform a list of coor via transformation matrix

            00 01 02    i
            10 11 12  * i+1
            0   0   1     1
            只算前两行
        """
        newcoor=[]
        for i in range(0, self.L):
            x = matrix[0][0] * self[i].x + matrix[0][1] * self[i].y + matrix[0][2]
            y = matrix[1][0] * self[i].x + matrix[1][1] * self[i].y + matrix[1][2]
            newcoor.append(APoint(x,y))
        return newcoor
        
    def GetTopLeftIndex(self):
        """返回离左上角最近点的索引"""
        lenlist = self.distance_to(self.Topleft)
        index0 = lenlist.index(min(lenlist))
        return index0

    def MBR(self):
        """
        Minimum Bounding Rectangle
        """
        bbox=self.GetBoundingBox()
        ptl=[bbox[0],APoint(bbox[0].x,bbox[1].y),bbox[1],APoint(bbox[1].x,bbox[0].y)]
        ptl=toLightWeightPolyline(ptl)
        return ptl

    def MER(self):
        """
        Minimum Enclosing Rectangle
        """
        rad=0
        bboxlist=[]
        while rad<2*pi:
            newcoor=PointSet(self.Transform(rotate(rad)))
            bboxlist.append([newcoor.GetBoundingBox(),rad])
            rad+=0.01
        def areabbox(boundingbox):
            return (boundingbox[1].x-boundingbox[0].x)*(boundingbox[1].y-boundingbox[0].y)

        bboxmin=min(bboxlist,key=lambda item:areabbox(item[0]))
        bbox=bboxmin[0]
        ptl=[bbox[0],APoint(bbox[0].x,bbox[1].y),bbox[1],APoint(bbox[1].x,bbox[0].y)]
        ptl=PointSet(ptl)
        ptl=ptl.Transform(rotate(-bboxmin[1]))
        return toLightWeightPolyline(ptl)

    def __findinitial(self):
        bbox=self.GetBoundingBox()
        bottom=[]
        for i in range(0,self.L):
            if self[i].y==bbox[0].y:
                bottom.append(i)
        return min(bottom,key=lambda i:self[i].x)

    def GrahamScan(self):
        vertex=[self.__findinitial()]
        lst=list(range(self.L))
        lst.remove(vertex[0]) #剩余点序
        anglelist=dict(zip(lst,[Vector(self[vertex[0]],self[i]).angle() for i in lst])) #剩余点序的angle
        lst.sort(key=lambda i:anglelist[i]) #将剩余点序按angle的从小到大排列
        filterlist=[[lst[0]]] #将angle相同的剩余点序归类
        for i in range(1,len(lst)):
            if anglelist[lst[i]]==anglelist[lst[i-1]]:
                filterlist[-1].append(lst[i])
            else:
                filterlist.append([lst[i]])
        lst=[]
        for item in filterlist:#每类中只有一个元素即取该元素，每类中有多个元素取到p0最远的元素
            if len(item)==1:
                lst.append(item[0])
            else:
                t=max(item,key=lambda i:distance(self[i],self[vertex[0]]))
                lst.append(t)
        vertex.append(lst[0])
        vertex.append(lst[1])
        for i in range(2,len(lst)):
            while Vector(self[vertex[-2]],self[vertex[-1]]).side(self[lst[i]])!=-1:
                vertex.pop()
            vertex.append(lst[i])
        map1=map(lambda i:self[i],vertex)
        return toLightWeightPolyline(map1)
        

        
    def JarvisMarch(self):
        """
        包裹法(Jarvis步进法)
        """
        vertex=[]#储存凸包点的序号
        vertex.append(self.__findinitial())#第一个点为最下方的那个点
        for i in range(self.L):
            v=self.__findnext(vertex[-1])
            if v!=vertex[0]:
                vertex.append(v)
            else:
                break
        map1=map(lambda i:self[i],vertex)
        return toLightWeightPolyline(map1)

    def __findnext(self,start):
        for i in range(self.L):
            if i!=start:
              if self.__allinleft(start,i):
                  return i 

    def __allinleft(self,i:int,j:int):
        _A,_B,_C=0,0,0
        for k in range(self.L):
            if(k!=i and k!=j):
                _A=self[j].y-self[i].y
                _B=self[i].x-self[j].x
                _C=self[j].x*self[i].y-self[i].x*self[j].y
                if _A*self[k].x+_B*self[k].y+_C>0:
                    return False
        return True #如果有点在该直线上，也返回true


    def ConcaveHull(self,multiplier=1):
        r=self.__def_r()
        r=r*multiplier #测试搜索半径扩大
        vertex=[]#储存凹包点的序号
        centerli=[]
        vertex.append(self.__findinitial())
        for i in range(self.L*2):
            circ=self.__circ_index(vertex[-1],r)
            v,center=self.__rollnext(vertex,circ,r)
            centerli.append(center)
            if v!=vertex[0]:
                vertex.append(v)
            else:
                break
        map1=map(lambda i:self[i],vertex)
        return toLightWeightPolyline(map1),centerli,r/2

    def __rollnext(self,vertex,circ,r):
        """
        r为每个点的搜索半径
        """
        def __keyangle(i):
            vec1=Vector(self[vertex[-1]],self[vertex[-2]])
            vec2=Vector(self[vertex[-1]],self[i])
            return vec1.angle(vec2)
        alpha=r/2 #r为圆半径
        if len(vertex)==1:
            for i in circ:
                p1=self[vertex[-1]]
                p2=self[i]
                center=Vector(p1,p2).dist_intersect(alpha,alpha)#作圆
                for j in circ:#对circ中的其他点
                    if j!=i:
                        if distance(self[j],center)<alpha:
                            break
                else:
                    return i,center
            raise ValueError("没找到此圆")
        else:
            if len(circ)==2:
                if circ[0]==vertex[-2]:
                    return circ[1],center
                return circ[0],center
            else:
                circ.sort(key=__keyangle)#对圆中点排序
                p1=self[vertex[-1]]
                for i in circ:
                    if i!=vertex[-2]:
                        p2=self[i]
                        center=Vector(p1,p2).dist_intersect(alpha,alpha)
                        for j in circ:
                            if j!=i:
                                if distance(self[j],center)<alpha:
                                    break
                        else:
                            return i,center
            raise ValueError("未知错误")
    def __def_r(self):
        """
        定义搜索半径，保证每个搜索半径内至少有两个点
        """
        minlist=[]
        for item in self:
            lenlist=self.distance_to(item)
            lenlist.sort()
            min3=lenlist[3]
            minlist.append(min3)
        return max(minlist)

    def __circ_index(self,poi,r):
        """
        返回在以po为圆心，以r为半径内的点的序号，不含本身
        """
        ilist=[]
        d=0
        for i in range(0,self.L):
            d=distance(self[poi],self[i])
            if d<=r and d:
                ilist.append(i)
        return ilist

    # def __findnext2(self,vertex,circ:list):
    #     anglelist=[]
    #     if len(vertex)==1:
    #         for i in circ:
    #             vec=Vector(self[vertex[-1]],self[i])
    #             anglelist.append(vec.angle())
    #         return circ[anglelist.index(min(anglelist))]    
    #     else:
    #         circ.remove(vertex[-2])
    #         vec=Vector(self[vertex[-1]],self[vertex[-2]])
    #         veci=[Vector(self[vertex[-1]],self[i]) for i in circ]
    #         anglelist=vec.angle(*veci)
    #         return circ[anglelist.index(min(anglelist))]
        
class Polyline(PointSet):

#以下为Akima插值

    def Akima(self,tagclosed):
        thetalist = self.__calcutheta(tagclosed)
        pqlist = self.__calcuparam(thetalist, tagclosed)
        del thetalist
        coor = self.__addcoor(pqlist)
        return coor

    def __AddPoint(self,tagclosed,n):#n为补点的个数（1,2）
        ptlistplus = list(self)
        if n!=1 and n!=2:
            print("补点个数有误")
            sys.exit()
        if tagclosed:
            ptlistplus.insert(0, self[-1])
            if n==2:
                ptlistplus.insert(0, self[-2])
            ptlistplus += self[0:n]
        else:
            pta = (self[2] - 3 * self[1] + 3 * self[0])
            ptb = (self[1] - 3 * self[0] + 3 * pta)
            if n==2:
                ptlistplus = [ptb, pta] + ptlistplus
            elif n==1:
                ptlistplus.insert(0,pta)
            for i in range(n):
                ptlistplus.append(ptlistplus[-1] * 3 - ptlistplus[-2] * 3 + ptlistplus[-3])
        return ptlistplus

    def __calcutheta(self, tagclosed):
        '''akima [cos sin]
        '''
        thetalist = []
        n = self.L
        ptlistplus = self.__AddPoint(tagclosed,2)
        for i in range(2, n + 2):  # 对每个点算出
            ablist = []  # a先,b后
            for j in range(i - 2, i + 2):
                ablist.append(ptlistplus[j + 1] - ptlistplus[j])
            w2 = abs(ablist[2][0] * ablist[3][1] - ablist[3][0] * ablist[2][1])
            w3 = abs(ablist[0][0] * ablist[1][1] - ablist[1][0] * ablist[0][1])
            a0 = w2 * ablist[1][0] + w3 * ablist[2][0]
            b0 = w2 * ablist[1][1] + w3 * ablist[2][1]
            root = sqrt(a0 * a0 + b0 * b0)
            try:
                costheta = a0 / root
                sintheta = b0 / root
            except ZeroDivisionError:
                print('前后两个点重叠!')
                sys.exit()
            thetalist.append((costheta, sintheta))
        return thetalist

    def __calcuparam(self, thetalist, tagclosed):
        pqlist = []  # 排列方式[[p0 p1 p2 p3 q0 q1 q2 q3],...]
        for i in range(-len(self), tagclosed - 1):
            r = distance(self[i], self[i + 1])
            para = []
            para.append(self[i][0])
            para.append(r * thetalist[i][0])
            para.append(3 * (self[i + 1][0] - self[i][0]) - r * (thetalist[i + 1][0] + 2 * thetalist[i][0]))
            para.append(-2 * (self[i + 1][0] - self[i][0]) + r * (thetalist[i + 1][0] + thetalist[i][0]))
            para.append(self[i][1])
            para.append(r * thetalist[i][1])
            para.append(3 * (self[i + 1][1] - self[i][1]) - r * (thetalist[i + 1][1] + 2 * thetalist[i][1]))
            para.append(-2 * (self[i + 1][1] - self[i][1]) + r * (thetalist[i + 1][1] + thetalist[i][1]))
            pqlist.append(para)
        return pqlist

    def __addcoor(self,pqlist):
        coor = []
        for i in pqlist:
            z = 0.
            while z < 1:
                x = i[0] + i[1] * z + i[2] * z * z + i[3] * z * z * z
                y = i[4] + i[5] * z + i[6] * z * z + i[7] * z * z * z
                coor += [x, y]
                z += 0.05
        coor += [sum(i[0:4]), sum(i[4:8])]
        return coor

#以下为二次多项式加权平均法
    def Poly2interpolation(self,tagclosed):
        ptlistplus=self.__AddPoint(tagclosed,1)
        aflist=self.__calcupoly2(ptlistplus)
        coor=self.__addcoor2(ptlistplus,aflist,tagclosed)
        return coor

    def calcuS(self,n,ptlist=None):
        """
        计算n号点到0号点的累计弦长,如果ptlist为空，则计算self的累计弦长
        """
        sums=0
        if ptlist==None:
            ptlist=self
        if n<0:
            n=n+len(ptlist)
        for i in range(0,n):
            sums+=distance(ptlist[i],ptlist[i+1])
        return sums

    def __calcufirstS(self,ptlistplus):
        return distance(ptlistplus[0],ptlistplus[1])

    def __calcupoly2(self,ptlistplus):
        """
        算出每个点的抛物线
        :param ptlistplus:
        :return: abcdeflist
        """
        abcdeflist=[]
        for i in range(1,self.L+1):#i-1,i,i+1
            s1=self.calcuS(i-1,ptlistplus)
            s2=s1+distance(ptlistplus[i-1],ptlistplus[i])
            s3=s2+distance(ptlistplus[i],ptlistplus[i+1])
            mat1=np.mat([[1,s1,s1*s1],[1,s2,s2*s2],[1,s3,s3*s3]])
            matx=np.mat([[ptlistplus[i-1][0]],[ptlistplus[i][0]],[ptlistplus[i+1][0]]])
            maty=np.mat([[ptlistplus[i-1][1]],[ptlistplus[i][1]],[ptlistplus[i+1][1]]])
            inv=np.linalg.inv(mat1)
            matabc=np.dot(inv,matx)
            matabc=matabc.tolist()
            matabc=[a[0] for a in matabc]
            matdef=np.dot(inv,maty)
            matdef=matdef.tolist()
            matdef = [a[0] for a in matdef]
            abcdeflist.append(matabc+matdef)
        return  abcdeflist

    def __addcoor2(self,ptlistplus,aflist,tagclosed):
        coorlist=[]
        for i in range(-self.L,-1+tagclosed):
            deltas=distance(self[i],self[i+1])
            s=self.__calcufirstS(ptlistplus)+self.calcuS(i)
            scorrect=0#用于处理闭合曲线最后一边的弦长问题
            s2=s
            k=0
            for k in range(0,20):#用k控制s
                u=(s-s2)/deltas
                wl=(1-u)**2*(1+2*u)
                wr=u**2*(3-2*u)
                pl = APoint(aflist[i][0] + aflist[i][1] * s + aflist[i][2] * s * s,
                            aflist[i][3] + aflist[i][4] * s + aflist[i][5]*s*s)
                pr = APoint(aflist[i+1][0] + aflist[i+1][1] * s + aflist[i+1][2] * s * s,
                            aflist[i+1][3] + aflist[i+1][4] * s + aflist[i+1][5]*s*s)
                if i==-1:
                     pr = APoint(aflist[i+1][0] + aflist[i+1][1] * scorrect + aflist[i+1][2] * scorrect * scorrect,
                            aflist[i+1][3] + aflist[i+1][4] * scorrect + aflist[i+1][5]*scorrect*scorrect)
                coorlist.append((wl * pl+ wr * pr)[0])
                coorlist.append((wl * pl+ wr * pr)[1])
                s+=0.05*deltas
                scorrect+=0.05*deltas
        coorlist.append(ptlistplus[self.L+tagclosed][0])
        coorlist.append(ptlistplus[self.L+tagclosed][1])
        return coorlist






    


##########################################################################
#以下为矩阵

class Mat(tuple):
    def __new__(cls,mylst):
        """用得到的多义线坐标表生成该点表"""
        if isinstance(mylst,(list,tuple)):
            return super(Mat,cls).__new__(cls,mylst)
        raise Exception('No coordinates input')

    def __mul__(self, other):
        """
        warning:it calculate other*self
        只算前两行
        """
        if isinstance(other,Mat):
            mat0 = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
            for i in range(2):
                for j in range(3):
                    for u in range(3):
                        mat0[i][j] += other[i][u] * self[u][j]
            return Mat(mat0)
        else:
            return list.__mul__(self,other)

    def __add__(self, other):
        if isinstance(other,Mat):
            mat0 = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
            for i in range(2):
                for j in range(3):
                        mat0[i][j] = other[i][j] + self[i][j]
            return Mat(mat0)
        else:
            return list.__add__(self,other)
    
    def transform(self,*polist:APoint):
        polist2=[]
        for po in polist:
            x = self[0][0] * po.x +self[0][1] * po.y + self[0][2]
            y = self[1][0] * po.x + self[1][1] * po.y + self[1][2]
            polist2.append(APoint(x,y))
        if len(polist2)==1:
            return polist2[0]
        return tuple(polist2)



#########################################################################

def rotate(theta,x=0,y=0):
    '''return rotate matrix,theta as radians
    '''
    if x==0 and y==0:
        matrix=[[cos(theta),-sin(theta),0],
        [sin(theta),cos(theta),0],
        [0,0,1]]
        return Mat(matrix)
    else:
        matrix=move(-x,-y)*rotate(theta)*move(x,y)
    return Mat(matrix)

def move(dx,dy=0):
    matrix=[[1,0,dx],
            [0,1,dy],
            [0,0,1]]
    return Mat(matrix)

def scale(sx=1,sy=1):
    matrix=[[sx,0,0],
            [0,sy,0],
            [0,0,1]]
    return Mat(matrix)

def shear(tanx=0,tany=0):
    matrix=[[1,tanx,0],
            [tany,1,0],
            [0,0,1]]
    return Mat(matrix)

def reflect(lx,ly):
    '''(x,y)为过原点直线的方向向量
    '''
    if lx==1 and ly==0:
        matrix=[[1,0,0],
            [0,-1,0],
            [0,0,1]]
    elif lx==0 and ly==1:
        matrix=[[-1,0,0],
            [0,1,0],
            [0,0,1]]
    elif lx==0 and ly==0:
        matrix=[[-1,0,0],
            [0,-1,0],
            [0,0,1]]
    else:
        length=sqrt(lx*lx+ly*ly)
        lx,ly=lx/length,ly/length
        matrix=[[lx*lx-ly*ly,2*lx*ly,0],
                [2*lx*ly,ly*ly-lx*lx,0],
                [0,0,1]]
    return Mat(matrix)

def toPolyline(apointlist):
    pt=[]
    for item in apointlist:
        pt+=item[0:3]
    return aDouble(pt)

def toLightWeightPolyline(apointlist):
    pt=[]
    for item in apointlist:
        pt+=item[0:2]
    return aDouble(pt)
