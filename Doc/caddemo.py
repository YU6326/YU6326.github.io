from pyautocad import Autocad,APoint,aDouble,aInt,aShort,ACAD
import math
from comtypes.automation import VARIANT
# aDouble 将*seq转换为double类型的array
# aInt 将*seq转换为int类型的array
# array.array(typecode,*seq)
# 'h' signed short 'i' signed int 'd' double
acad=Autocad(create_if_not_exists=True)
def demo1():#画线
    p1=APoint(0,0)
    p2=APoint(30,20)
    LineObj=acad.model.AddLine(p1,p2)

def demo2():#返回第一个实体的名称
    if acad.model.count:
        entity=acad.model.item(0)
        print(entity.ObjectName+' is the first entity in model space')
    else:
        print('There are no objects in model space')

def demo3():#返回层名
    for i in range(0,acad.doc.Layers.count):
        print(acad.doc.Layers(i).Name)

def demo4():#删除指定图层
    aLayer=acad.doc.Layers('abc')
    aLayer.Delete()

def demo5():#选择集
    try:
        acad.doc.SelectionSets.Item('SS4').Delete()
    except Exception:
        print('未删除成功')
    sstext=acad.doc.SelectionSets.Add('SS4')
    filtertype=aShort([0])
    filterdata=('circle',)
    sstext.SelectOnScreen(filtertype,filterdata)

def demo6():#角度换弧度
    print(acad.doc.Utility.AngleToReal(30,0))

def demo7():#设置环境变量
    cmde=acad.doc.GetVariable('cmdecho')
    print(cmde)

def demo8():#选点交互
    prompt1='\n'+'Enter the start point of the line:'
    prompt2='\n'+'Enter the end point of the line:'
    acad.prompt(prompt1)
    ep=acad.doc.Utility.GetPoint()
    acad.model.AddLine(sp,ep)
    acad.ZoomAll()

def demo9():#获得string
    str=acad.doc.Utility.GetString(1,'输入参数个数')

def demo10():#创建pl
    lis=aDouble(0,0,100,200)
    acad.model.AddLightWeightPolyline(lis)

def demo11():#返回坐标
    try:
        acad.doc.SelectionSets.Item('SS1').Delete()
    except Exception:
        print('Delete selection failed')

    selection=acad.doc.SelectionSets.Add('SS1')
    acad.prompt('选择一条多义线')
    selection.SelectOnScreen()
    if selection.Count==1:
        entity=selection.item(0)
    else:
        print("选择的多义线多于一条")
        return
    if entity.ObjectName=='AcDbPolyline':
        coor=entity.Coordinates#元组
        coorx=coor[::2]
        coory=coor[1::2]
        coortuplelist=zip(coorx,coory)
        oldcoor=zip(*coortuplelist)
        print(coorx)
        print(coory)       
    
def demo12():#选择0层圆并将颜色改为红色
    try:
        acad.doc.SelectionSets.Item('SS5').Delete()
    except Exception:
        print('ss5不存在')
    ss=acad.doc.SelectionSets.Add('SS5')
    filtertype=aShort([0,8])
    filterdata=('Circle','0')
    ss.SelectOnScreen(filtertype,filterdata)
    newcolor=acad.app.GetInterfaceObject('AutoCAD.AcCmColor.20')
    #.20 version independent
    newcolor.SetRGB(255,0,0)
    #Colors are identified by an AcCmColor object. 
    # This object can hold an RGB value, an ACI number
    # (an integer from 1 to 255), or a named color.
    # Using an RGB value, you can choose from millions of colors. 
    for entity in ss:
        entity.TrueColor=newcolor
    ss.Delete()

def demo13():#画围棋棋盘
    p1=APoint(0,0)
    p2=APoint(0,180)
    for i in range(19):
        acad.model.AddLine(p1,p2)
        p1.x+=10
        p2.x+=10
    p1=APoint(0,0)
    p2=APoint(180,0)
    for i in range(19):
        acad.model.AddLine(p1,p2)
        p1.y+=10
        p2.y+=10

def demo14():#函数绘图
    x=1
    ptlist=[0,0,1,0]
    while x<2:
        x+=0.05
        y=math.sin(math.pi/2*(x-1))
        ptlist+=[x,y]
    ptlist+=[2,1,3,1]
    en=acad.model.AddLightWeightPolyline(aDouble(ptlist))
    basePnt=APoint(0)
    endPnt=APoint(0)
    for i in range(100):
        copyen=en.Copy()
        endPnt.x+=0.5
        copyen.Move(basePnt,endPnt)

def test():#常量值
    print(ACAD.acRed)
    print(ACAD.acYellow)
    print(ACAD.acGreen)
    print(ACAD.acCyan)
    print(ACAD.acBlue)
    print(ACAD.acMagenta)
    print(ACAD.acWhite)
    print(ACAD.acByBlock)
    print(ACAD.acByLayer)
    #设置颜色，依次为1 2 3 4 5 6 7 0 256
    print(ACAD.acActiveViewport)
    print(ACAD.acAllViewports)
    #在acad.doc.Regen(param)中调用 0 1

#python 生成tuple
# coorx=coor[::2]
# coory=coor[1::2]
# coortuplelist=list(zip(coorx,coory))
# for x,y in zip(coorx,coory):并行迭代

if __name__=="__main__":#选择测试的函数
    test()
