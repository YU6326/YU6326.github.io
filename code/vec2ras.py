from pyautocad import Autocad,APoint
from pyptlist import Polyline,move
from math import floor,ceil,sqrt
import time

acad=Autocad(create_if_not_exists=True)

def Line2Ras():
    ss=acad.get_selection('请选择一条直线')
    if ss.count==1:
        entity=ss.Item(0)
        p1=APoint(entity.StartPoint)
        p2=APoint(entity.EndPoint)
        lst=[p1,p2]
        ptl=Polyline(lst)
        DrawGrid(ptl)
        n=acad.doc.Utility.GetInteger("请选择画线算法\n1.数值微分法 2.中点Bresenham算法")
        if n==1:
            vlist=ptl.DDA()
        elif n==2:
            vlist=ptl.Bresenham()
        for v in vlist:
            acad.model.AddCircle(v,0.5)
    else:
        acad.prompt('选择的对象不是一个，请重新选择')


def DrawGrid(ptl):
    minpo,maxpo=ptl.GetBoundingBox()
    start=APoint(floor(minpo.x-1),floor(minpo.y-1))
    end=APoint(ceil(maxpo.x+1),ceil(maxpo.y+1))
    col=start.x
    while col<=end.x:
        acad.model.AddLine(APoint(col,start.y),APoint(col,end.y))
        col+=1
    row=start.y
    while row<=end.y:
        acad.model.AddLine(APoint(start.x,row),APoint(end.x,row))
        row+=1



def Circle2Ras():
    ss=acad.get_selection('请选择一个圆')
    if ss.count==1:
        entity=ss.Item(0)
        p1=APoint(entity.Center)
        r=entity.Radius
        lst=[p1-r,p1+r]
        ptl=Polyline(lst)
        DrawGrid(ptl)
        n=acad.doc.Utility.GetInteger("请选择画圆算法\n1.简单方程法 2.中点Bresenham算法")
        if n==1:
            vlist=SimpleCirc(p1,r)
        elif n==2:
            vlist=BresenhamCirc(p1,r)
        for v in vlist:
            acad.model.AddCircle(v,0.5)
    else:
        acad.prompt('选择的对象不是一个，请重新选择')

def SimpleCirc(cen,r):
    sup=r/sqrt(2)
    x=0
    vertex=[]
    while x<sup:
        seed=APoint(x,sqrt(r*r-x*x))
        seed2=APoint(seed.y,seed.x)
        seed3=APoint(seed.x,-seed.y)
        seed4=APoint(seed.y,-seed.x)
        vertex+=[seed,seed2,seed3,seed4,-seed,-seed2,-seed3,-seed4]
        x+=1
    vertex=move(cen.x,cen.y).transform(*vertex)
    vertexround=[]
    for item in vertex:
        vertexround.append(APoint(round(item.x),round(item.y)))
    return vertexround
        

def BresenhamCirc(cen,r):
    sup=r/sqrt(2)
    x=0
    y=sqrt(r*r-x*x)
    d=1-r
    vertex=[]
    while x<sup:
        seed=APoint(round(x),round(y)) #开始不round成整点，因为如果圆心坐标不是整数后面不好办
        seed2=APoint(seed.y,seed.x)
        seed3=APoint(seed.x,-seed.y)
        seed4=APoint(seed.y,-seed.x)
        vertex+=[seed,seed2,seed3,seed4,-seed,-seed2,-seed3,-seed4]
        if d<=0:
            d+=2*x+3
        else:
            d+=2*(x-y)+5
            y-=1
        x+=1
    vertex=move(cen.x,cen.y).transform(*vertex)
    vertexround=[]
    for item in vertex:
        vertexround.append(APoint(round(item.x),round(item.y)))
    return vertexround
    
def FillCircle(cen,r):
    bottom=cen.y-r
    top=cen.y+r
    vertex=[]
    for y in range(ceil(bottom),ceil(top)):
        ry=sqrt(r*r-(y-cen.y)**2)
        x1=cen.x-ry
        x2=cen.x+ry
        for x in range(ceil(x1),ceil(x2)):
            vertex.append(APoint(x,y))
    return vertex

def PolyCircle2Ras():
    n=acad.doc.Utility.GetInteger("请选择\n1.圆边界扫描转换2.圆面域扫描转换3.多边形边界扫描转换4.多边形面域扫描转换\n")
    time.sleep(0.2)
    if n==1:
        m=acad.doc.Utility.GetInteger("请选择\n1.简单方程法2.中点Bresenham法\n")
        ss=acad.get_selection("请选择一个圆")
        entity=ss.Item(0)
        p1=entity.Center
        r=entity.Radius
        lst=[p1-r,p1+r]
        ptl=Polyline(lst)
        DrawGrid(ptl)
        if m==1:
            vlist=SimpleCirc(p1,r)
        elif m==2:
            vlist=BresenhamCirc(p1,r)
    elif n==2:
        ss=acad.get_selection("请选择一个圆")
        entity=ss.Item(0)
        p1=APoint(entity.Center)
        r=entity.Radius
        lst=[p1-r,p1+r]
        ptl=Polyline(lst)
        DrawGrid(ptl)
        vlist=FillCircle(p1,r)
    elif n==3 or n==4:
        ss=acad.get_selection("请选择一个多边形")
        entity=ss.Item(0)
        closed=entity.Closed
        plist=entity.Coordinates
        ptl=Polyline(plist)
        DrawGrid(ptl)
        if n==3:
            vlist=ptl.Bresenham(closed)
        elif n==4:
            if closed:
                vlist=ptl.FillPolygon()
            else:
                acad.prompt("该多义线没有闭合，无法填充")
    for v in vlist:
        acad.model.AddCircle(v,0.5)
    

if __name__=="__main__":
    PolyCircle2Ras()