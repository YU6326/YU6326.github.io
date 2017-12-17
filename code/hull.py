from pyautocad import Autocad,APoint,aDouble,ACAD,distance
from math import *
from pyptlist import PointSet,toLightWeightPolyline
import time

acad=Autocad(create_if_not_exists=True)

def MBR():
    selection=acad.get_selection("选择一条多义线或不少于三个点")
    coor=[]
    if selection.count==1:
        entity=selection.Item(0)
        ptl=PointSet(entity.Coordinates)
    elif selection.count>=3:
        for item in selection:
            if item.ObjectName=="AcDbPoint":
                coor.append(APoint(item.Coordinates))
        ptl=PointSet(coor)
    else:
        return
    polyline=ptl.MBR()
    en=acad.model.AddLightWeightPolyline(polyline)
    en.Closed=True
    en.Color=ACAD.acRed

def MER():
    selection=acad.get_selection("选择一条多义线或不少于三个点")
    coor=[]
    if selection.count==1:
        entity=selection.item(0)
        ptl=PointSet(entity.Coordinates)
    elif selection.count>=3:
        for item in selection:
            if item.ObjectName=="AcDbPoint":
                coor.append(APoint(item.Coordinates))
        ptl=PointSet(coor)
    else:
        return
    polyline=ptl.MER()
    en=acad.model.AddLightWeightPolyline(polyline)
    en.Closed=True
    en.Color=ACAD.acBlue

def ConvexHull():
    selection=acad.get_selection("选择一条多义线或不少于三个点")
    coor=[]
    if selection.count==1:
        entity=selection.item(0)
        ptl=PointSet(entity.Coordinates,True)
    elif selection.count>=3:
        for item in selection:
            if item.ObjectName=="AcDbPoint":
                coor.append(APoint(item.Coordinates))
        ptl=PointSet(coor,True)
    else:
        return
    polyline=ptl.GrahamScan() #80个点，100次运行时间：2.399s
    # polyline=ptl.JarvisMarch() #100次运行时间：17.894s

    en=acad.model.AddLightWeightPolyline(polyline)
    en.Closed=True
    en.Color=ACAD.acYellow

def ConcaveHull():
    selection=acad.get_selection("选择一条多义线或不少于三个点")
    coor=[]
    if selection.count==1:
        entity=selection.item(0)
        ptl=PointSet(entity.Coordinates,True)
    elif selection.count>=3:
        for item in selection:
            if item.ObjectName=="AcDbPoint":
                coor.append(APoint(item.Coordinates))
        ptl=PointSet(coor,True)
    else:
        return
    # iset=[1,2,3,5,10,100]
    # for i in iset:
    polyline,centerli,alpha=ptl.ConcaveHull(1.5)
    en=acad.model.AddLightWeightPolyline(polyline)
    en.Closed=True
    # for c in centerli:
    #     acad.model.AddCircle(c,alpha)
    en.Color=ACAD.acMagenta

if __name__=="__main__":
    ConcaveHull()

