# -*- coding: utf-8 -*-

from pyautocad import Autocad,APoint,aDouble,ACAD
import pyautocad
from math import *

acad=Autocad(create_if_not_exists=True)

def job1():
    old_pdmode=acad.doc.GetVariable('pdmode')
    acad.doc.SetVariable('pdmode',2)
    n=acad.doc.Utility.GetInteger('\n请输入点的个数(至少3个):')
    if n<3:
        acad.prompt('输入点数量有误，程序终止')
        return
    ptlist=[]
    for i in range(n):
        prompt1='\n请输入第%d个点'% (i+1)
        acad.prompt(str(prompt1))
        try:
            pt=acad.doc.Utility.GetPoint()
        except Exception:
            acad.prompt('输入有误，请重新输入')
        apt=APoint(pt)
        acad.model.AddPoint(apt)
        ptlist.append(apt)
    while True:
        closed=acad.doc.Utility.GetString(0,'\n曲线是否闭合Y(闭合)/N(不闭合)?默认Y')
        if closed=='' or closed.lower()=='y':
            tagclosed=True
            break
        elif closed.lower()=='n':
            tagclosed=False
            break
        else:
            acad.prompt('输入有误，请重新输入！')
    thetalist=CalcuTheta(ptlist,tagclosed)
    pqlist=CalcuParam(ptlist,thetalist,tagclosed)
    coor=AddCoor(pqlist)
    en=acad.model.AddLightWeightPolyline(aDouble(coor))
    en.Color=ACAD.acBlue
    acad.doc.SetVariable('pdmode',old_pdmode)


def CalcuParam(ptlist,thetalist,tagclosed):
    pqlist=[]#排列方式[[p0 p1 p2 p3 q0 q1 q2 q3],...]
    for i in range(-len(ptlist),tagclosed-1):
        r=pyautocad.distance(ptlist[i],ptlist[i+1])
        para=[]
        para.append(ptlist[i][0])
        para.append(r*thetalist[i][0])
        para.append(3*(ptlist[i+1][0]-ptlist[i][0])-r*(thetalist[i+1][0]+2*thetalist[i][0]))
        para.append(-2*(ptlist[i+1][0]-ptlist[i][0])+r*(thetalist[i+1][0]+thetalist[i][0]))
        para.append(ptlist[i][1])
        para.append(r*thetalist[i][1])
        para.append(3*(ptlist[i+1][1]-ptlist[i][1])-r*(thetalist[i+1][1]+2*thetalist[i][1]))
        para.append(-2*(ptlist[i+1][1]-ptlist[i][1])+r*(thetalist[i+1][1]+thetalist[i][1]))
        pqlist.append(para)
    return pqlist

def AddPoint(ptlist,tagclosed):
    ptlistplus=ptlist.copy()
    if tagclosed:
        ptlistplus.insert(0,ptlist[-1])
        ptlistplus.insert(0,ptlist[-2])
        ptlistplus+=ptlist[0:2]
    else:
        pta=(ptlist[2]-3*ptlist[1]+3*ptlist[0])
        ptb=(ptlist[1]-3*ptlist[0]+3*pta)
        ptlistplus=[ptb,pta]+ptlistplus
        for i in range(2):
            ptlistplus.append(ptlistplus[-1]*3-ptlistplus[-2]*3+ptlistplus[-3])
    return ptlistplus

def CalcuTheta(ptlist,tagclosed):
    '''akima [cos sin]
    '''
    thetalist=[]
    n=len(ptlist)
    ptlistplus=AddPoint(ptlist,tagclosed)
    for i in range(2,n+2):#对每个点算出
        ablist=[]#a先,b后
        for j in range(i-2,i+2):
            ablist.append(ptlistplus[j+1]-ptlistplus[j])
        w2=abs(ablist[2][0]*ablist[3][1]-ablist[3][0]*ablist[2][1])
        w3=abs(ablist[0][0]*ablist[1][1]-ablist[1][0]-ablist[0][1])
        a0=w2*ablist[1][0]+w3*ablist[2][0]
        b0=w2*ablist[1][1]+w3*ablist[2][1]
        root=sqrt(a0*a0+b0*b0)
        costheta=a0/root
        sintheta=b0/root
        thetalist.append((costheta,sintheta))
    return thetalist


def AddCoor(pqlist):
    coor=[]
    for i in pqlist:
        z=0.
        while z<1:
            x=i[0]+i[1]*z+i[2]*z*z+i[3]*z*z*z
            y=i[4]+i[5]*z+i[6]*z*z+i[7]*z*z*z
            coor+=[x,y]
            z+=0.05
    coor+=[sum(i[0:4]),sum(i[4:8])]
    return coor  



if __name__=='__main__':
    job1()
