from main import PointSet
from pyautocad import distance,APoint


class Polygon(PointSet):
    """
    可以理解为闭合多边形
    元素是APoint点元组
    属性有L,Center,Topleft,Topright,Bottomleft,Bottomright
    常用方法有：GetBoundingBox()等
    """
    def GetEdgeLength(self):
        edgelist=[]
        for i in range(-self.L,0):
            edgelist.append((distance(self[i],self[i+1])))
        return edgelist

    def GetAverageEdgeLength(self):
        el=self.GetEdgeLength()
        return sum(el)/self.L

    def GetEdgeCenter(self):
        edgecenter=[]
        for i in range(-self.L,0):
            xm=(self[i].x+self[i+1].x)/2
            ym=(self[i].y+self[i+1].y)/2
            edgecenter.append(APoint(xm,ym))
        return edgecenter
    def DirectedArea(self):
        return self.GetDirectionArea()[1]

    def Area(self):
        """得到面积"""
        return  abs(self.GetDirectionArea()[1])

    def Direction(self):
        """得到方向(True逆时针 False顺时针)"""
        return self.GetDirectionArea()[0]

    def GetDirectionArea(self):
        """得到方向(True逆时针 False顺时针)和有向面积directedarea"""
        darea=0
        edgelist = []
        for i in range(-self.L, 0):
            darea += self[i].x * self[i + 1].y - self[i].y * self[i + 1].x
        direction=True
        if darea < 0:
            direction=False
        return direction,darea/2

    def GetLongestDiagonalLine(self):
        """
        得到最长对角线起点和终点的坐标,长度
        """
        diagonal = []
        length = self.L
        for j in range(2, length // 2 + 1):
            for i in range(length):
                s = distance(self[i], self[i + j - length])
                diagonal.append((i, i + j - length, s))
        diagonal.sort(key=lambda x: x[2])
        longest = diagonal.pop()
        return self[longest[0]],self[longest[1]],longest[2]

    def Contains(self,po:APoint):
        """
        在多边形内返回true，在多边形外返回false，在多边形上返回值随机。
        """
        oddNodes=False
        x=po.x
        y=po.y
        for i in range(0,self.L):
            if self[i].y<y and self[i-1].y>=y or self[i-1].y<y and self[i].y>=y:
                try:
                    slope=(self[i-1].x-self[i].x)/(self[i-1].y-self[i].y)
                except ZeroDivisionError:
                    slope=float("inf")
                if self[i].x+slope*(y-self[i].y)<x:
                    oddNodes=not oddNodes
        return oddNodes
