from pyautocad import Autocad,APoint,aDouble,ACAD,distance
from math import *
from pyptlist import UnorderedPtlist,toLightWeightPolyline

acad=Autocad(create_if_not_exists=True)

def MBR():
    selection=acad.get_selection("选择一条多义线或不少于三个点")
    coor=[]
    if selection.count==1:
        entity=selection.Item(0)
        ptl=UnorderedPtlist(entity.Coordinates)
    elif selection.count>=3:
        for item in selection:
            if item.ObjectName=="AcDbPoint":
                coor.append(APoint(item.Coordinates))
        ptl=UnorderedPtlist(coor)
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
        ptl=UnorderedPtlist(entity.Coordinates)
    elif selection.count>=3:
        for item in selection:
            if item.ObjectName=="AcDbPoint":
                coor.append(APoint(item.Coordinates))
        ptl=UnorderedPtlist(coor)
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
        ptl=UnorderedPtlist(entity.Coordinates,True)
    elif selection.count>=3:
        for item in selection:
            if item.ObjectName=="AcDbPoint":
                coor.append(APoint(item.Coordinates))
        ptl=UnorderedPtlist(coor,True)
    else:
        return
    polyline=ptl.ConvexHull()
    en=acad.model.AddLightWeightPolyline(polyline)
    en.Closed=True
    en.Color=ACAD.acYellow

if __name__=="__main__":
    ConvexHull()

