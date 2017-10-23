
# -*- coding: utf-8 -*-
# 编译器Python3.6 64bit
# 相关包：pyautocad,comtypes,numpy
# (因为numpy的数据类型无bug，可能跟comtypes的内部数据类型转换有关)
from pyautocad import Autocad,APoint,aDouble,aShort,aInt,ACAD
import numpy as np
from math import *

acad=Autocad(create_if_not_exists=True)

#对于autocad中的lwpolyline
def job1():
    '''绕中心点逆时针旋转45度，绘制的线用红色表示
    '''
    try:
        acad.doc.SelectionSets.Item('SS1').Delete()
    except Exception:
        print('Delete selection failed')

    selection=acad.doc.SelectionSets.Add('SS1')
    acad.prompt('选择一条多义线')
    selection.SelectOnScreen(aShort([0]),['lwpolyline'])
    if selection.Count==1:
        entity=selection.Item(np.int(0))
    else:
        print("选择的多义线多于一条")
        return
    coor=entity.Coordinates #tuple
    newcoor=transform(rotate(radians(45),*center(coor)),coor)
    entity.Coordinates=aDouble(newcoor)
    entity.Color=ACAD.acRed
    acad.doc.Regen(1)

def job2():
    '''选取最长的对角线，以对角线的某一点为原点，沿该对角线伸长1.5倍
    绘制的线用蓝色表示
    '''
    try:
        acad.doc.SelectionSets.Item('SS1').Delete()
    except Exception:
        print('Delete selection failed')

    selection=acad.doc.SelectionSets.Add('SS1')
    acad.prompt('选择一条多义线')
    selection.SelectOnScreen(aShort([0]),['lwpolyline'])
    if selection.Count==1:
        entity=selection.Item(np.int(0))
    else:
        print("选择的多义线多于一条")
        return
    coor=entity.Coordinates #tuple77
    vectorcoor=longestDiagonalLine(coor)     
    basePnt=vectorcoor[0:2]
    endPnt=vectorcoor[2:4]
    angle=acad.doc.Utility.AngleFromXAxis(APoint(*basePnt),APoint(*endPnt))
    negbasePnt=[-x for x in basePnt]
    mat1=multi(move(*negbasePnt),rotate(-angle))
    mat2=scale(1.5)
    mat3=multi(rotate(angle),move(*basePnt))
    mat=multi(mat1,mat2,mat3)
    newcoor=transform(mat,coor)
    entity.Coordinates=aDouble(newcoor)
    entity.Color=ACAD.acBlue
    acad.doc.Regen(1)

def job3():
    '''以该多边形的外包矩形的左下角为原点，实现沿着x方向的错切变换
    '''
    try:
        acad.doc.SelectionSets.Item('SS1').Delete()
    except Exception:
        print('Delete selection failed')

    selection=acad.doc.SelectionSets.Add('SS1')
    acad.prompt('选择一条多义线')
    selection.SelectOnScreen(aShort([0]),['lwpolyline'])
    if selection.Count==1:
        entity=selection.Item(np.int(0))
    else:
        print("选择的多义线多于一条")
        return
    coor=entity.Coordinates
    # minPnt=np.float_([0,0,0])
    # maxPnt=np.float_([0,0])
    # pBox=entity.GetBoundingBox
    # minx=pBox()[0][0]
    # miny=pBox()[0][1]
    # maxx=pBox()[1][0]
    # maxy=pBox()[1][1]
    retval=GetBoundingBox(entity)
    mat=multi(move(-retval[0],-retval[1]),shear(1),move(retval[0],retval[1]))
    newcoor=transform(mat,coor)
    entity.Coordinates=aDouble(newcoor)
    entity.Color=ACAD.acYellow
    acad.doc.Regen(1)
        
def transform(matrix:list,coor:list):
    '''transform a list of coor via transformation matrix

    00 01 02    i
    10 11 12  * i+1
    0   0   1     1
    只算前两行
    '''
    newcoor=[]
    for i in range(0,len(coor),2):
        x=matrix[0][0]*coor[i]+matrix[0][1]*coor[i+1]+matrix[0][2]
        y=matrix[1][0]*coor[i]+matrix[1][1]*coor[i+1]+matrix[1][2]
        newcoor.append(x)
        newcoor.append(y)
    return newcoor

def multi(mat1,mat2,mat3=None):
    '''mat2*mat1

    只算前两行
    '''
    if not mat3:
        mat=[[0,0,0],[0,0,0],[0,0,1]]
        for i in range(2):
            for j in range(3):
                for u in range(3):
                    mat[i][j]+=mat2[i][u]*mat1[u][j]
        return mat
    else:
        return multi(multi(mat1,mat2),mat3)

def rotate(theta,x=0,y=0):
    '''return rotate matrix,theta as radians
    '''
    if x==0 and y==0:
        matrix=[[cos(theta),-sin(theta),0],
        [sin(theta),cos(theta),0],
        [0,0,1]]
        return matrix
    else:
        matrix=multi(move(-x,-y),rotate(theta),move(x,y))
    return matrix

def move(dx,dy=0):
    matrix=[[1,0,dx],
            [0,1,dy],
            [0,0,1]]
    return matrix

def scale(sx=1,sy=1):
    matrix=[[sx,0,0],
            [0,sy,0],
            [0,0,1]]
    return matrix

def shear(tanx=0,tany=0):
    matrix=[[1,tanx,0],
            [tany,1,0],
            [0,0,1]]
    return matrix

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
    return matrix

def center(coor):
    '''得到几何中心
    '''
    coorx=coor[::2]
    coory=coor[1::2]
    return sum(coorx)/len(coorx),sum(coory)/len(coory)

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def longestDiagonalLine(coor):
    '''得到最长对角线起点和终点的坐标
    '''
    coorx=coor[::2]
    coory=coor[1::2]
    diagonal=[]
    length=len(coorx)
    for j in range(2,length//2+1):
        for i in range(length):
            s=distance(coorx[i],coory[i],coorx[i+j-length],coory[i+j-length])
            diagonal.append((i,i+j-length,s))   
    diagonal.sort(key=lambda x:x[2])
    longest=diagonal.pop()
    return coorx[longest[0]],coory[longest[0]],coorx[longest[1]],coory[longest[1]]

def GetBoundingBox(entity):
    '''得到boundingbox仅限于lwpolyline
    '''
    coor=entity.Coordinates
    coorx=coor[::2]
    coory=coor[1::2]
    minx,maxx=min(coorx),max(coorx)
    miny,maxy=min(coory),max(coory)
    return minx,miny,maxx,maxy

def test():
    '''test
    '''
    coor=[1,0,1,1,0,2,-1,1,-1,0]
    vectorcoor=longestDiagonalLine(coor)        
    angle=acad.doc.Utility.AngleFromXAxis(APoint(*vectorcoor[0:2]),APoint(*vectorcoor[2:4]))
    print(angle)
    # a1=[[1,2,3],[4,5,6],[0,0,1]]
    # a2=[[1,2,3],[4,5,6],[7,8,9]]
    # coor=transform(a1,[1,2])
    # print(coor)

if __name__=="__main__":
    #job1()
    #job2()
    job3()