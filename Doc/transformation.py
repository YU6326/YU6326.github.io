
from pyautocad import Autocad,APoint,aDouble,aShort,aInt,ACAD
from math import *
import array
import comtypes.automation
acad=Autocad()

def job1():
    try:
        acad.doc.SelectionSets.Item('SS1').Delete()
    except Exception:
        print('Delete selection failed')

    selection=acad.doc.SelectionSets.Add('SS1')
    acad.prompt('选择一条多义线')
    selection.SelectOnScreen(aShort([0]),['lwpolyline'])
    if selection.Count==1:
        entity=selection.Item(0)
    else:
        print("选择的多义线多于一条")
        return
    coor=entity.Coordinates #tuple
    newcoor=transform(rotate(radians(45),*center(coor)),coor)
    entity.Coordinates=aDouble(newcoor)
    entity.Color=ACAD.acRed
    acad.doc.Regen(1)

def job2():
    try:
        acad.doc.SelectionSets.Item('SS1').Delete()
    except Exception:
        print('Delete selection failed')

    selection=acad.doc.SelectionSets.Add('SS1')
    acad.prompt('选择一条多义线')
    selection.SelectOnScreen(aShort([0]),['lwpolyline'])
    if selection.Count==1:
        entity=selection.Item(0)
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
    try:
        acad.doc.SelectionSets.Item('SS1').Delete()
    except Exception:
        print('Delete selection failed')

    selection=acad.doc.SelectionSets.Add('SS1')
    acad.prompt('选择一条多义线')
    selection.SelectOnScreen(aShort([0]),['lwpolyline'])
    if selection.Count==1:
        entity=selection.Item(0)
    else:
        print("选择的多义线多于一条")
        return
    coor=entity.Coordinates
    # minPnt=APoint(0)
    # maxPnt=[0]
    # minPnt1=array.array('Q',[])
    # maxPnt1=comtypes.automation.VARIANT()
    # u=entity.GetBoundingBox
    # minPnt1=()
    # maxPnt1=None
    # u=entity.GetBoundingBox
    # entity.GetBoundingBox(minPnt1,maxPnt1)#bug
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
    coorx=coor[::2]
    coory=coor[1::2]
    return sum(coorx)/len(coorx),sum(coory)/len(coory)

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def longestDiagonalLine(coor):
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
    coor=entity.Coordinates
    coorx=coor[::2]
    coory=coor[1::2]
    minx,maxx=min(coorx),max(coorx)
    miny,maxy=min(coory),max(coory)
    return minx,miny,maxx,maxy

def test():
    coor=[1,0,1,1,0,2,-1,1,-1,0]
    vectorcoor=longestDiagonalLine(coor)        
    angle=acad.doc.Utility.AngleFromXAxis(APoint(*vectorcoor[0:2]),APoint(*vectorcoor[2:4]))
    print(angle)

if __name__=="__main__":
    # a1=[[1,2,3],[4,5,6],[0,0,1]]
    # a2=[[1,2,3],[4,5,6],[7,8,9]]
    # coor=transform(a1,[1,2])
    # print(coor)
    job3()