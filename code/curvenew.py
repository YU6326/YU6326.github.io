from pyautocad import Autocad,APoint,ACAD
import numpy as np
import pyptlist
import random
import time

acad=Autocad(create_if_not_exists=True)

def getpoint():#从cad中获得点
    acad.doc.SetVariable('pdmode', 2)
    n = acad.doc.Utility.GetInteger('请输入点的个数(至少3个):')
    if n < 3:
        acad.prompt('输入点数量有误，程序终止')
        return
    ptlist = []
    for i in range(n):
        prompt1 = "请输入第%d/%d个点" % (i + 1, n)
        acad.prompt(prompt1)
        while True:  # 遇到呼叫错误，不断重复尝试。
            try:
                pt = acad.doc.Utility.GetPoint()
            except Exception:
                time.sleep(0.2)
                acad.doc.Regen(ACAD.acActiveViewport)
                #acad.prompt(prompt1)
                print('呼叫错误，重试')
            else:
                break
        time.sleep(0.1)
        pt = APoint(pt)
        acad.model.AddPoint(pt)
        ptlist.append(pt)
    while True:
        closed = acad.doc.Utility.GetString(0, '\n曲线是否闭合Y(闭合)/N(不闭合)?默认Y')
        if closed == '' or closed.lower() == 'y':
            tagclosed = True
            break
        elif closed.lower() == 'n':
            tagclosed = False
            break
        else:
            acad.prompt('输入有误，请重新输入！')
    return ptlist,tagclosed


def job1():
    ptlist,tagclosed=getpoint()
    myptlist=pyptlist.Polygon(ptlist)
    coor=myptlist.Akima(tagclosed)
    en=acad.model.AddLightWeightPolyline(np.float_(coor))
    en.Color=ACAD.acBlue


def job2():
    ptlist,tagclosed=getpoint()
    myptlist = pyptlist.Polygon(ptlist)
    coor = myptlist.Poly2interpolation(tagclosed)
    en = acad.model.AddLightWeightPolyline(np.float_(coor))
    en.Color = ACAD.acRed

def jobcombine():
    ptlist,tagclosed=getpoint()
    myptlist=pyptlist.Polygon(ptlist)
    coor=myptlist.Akima(tagclosed)
    en=acad.model.AddLightWeightPolyline(np.float_(coor))
    en.Color=ACAD.acBlue
    coor = myptlist.Poly2interpolation(tagclosed)
    en = acad.model.AddLightWeightPolyline(np.float_(coor))
    en.Color = ACAD.acRed


if __name__=="__main__":
    jobcombine()