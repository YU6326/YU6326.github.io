from pyautocad import Autocad,APoint,aDouble,aShort,distance
from pyptlist.main import *

acad=Autocad(create_if_not_exists=True)
def job5():
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
        print('选择的多义线多于一条')
        return
    coor=entity.Coordinates
    ptlist=Ptlist(coor)
    leftup=ptlist.Topleft
    index0=ptlist.GetTopLeftIndex()
    retVal=ptlist.GetDirectionArea()
    oriention=retVal[0]
    area=abs(retVal[1])
    edge=ptlist.GetAverageEdgeLength()
    edgecenter=ptlist.GetEdgeCenter()
    height=edge/20#字高为平均边长的1/20
    num=1
    if oriention:
        for i in range(index0,index0-len(ptlist),-1):
            acad.model.AddText('J%d'%num,ptlist[i],height)
            acad.model.AddText('L%d'%num,edgecenter[i],height)
            num+=1
    else:
        for i in range(index0-len(ptlist),index0,1):
            acad.model.AddText('J%d'%num,ptlist[i],height)
            acad.model.AddText('L%d'%num,edgecenter[i],height)
            num+=1
    area=round(area,2)
    #point=GetMiddle(ptlist)
    point=ptlist.Center
    acad.model.AddText('面积=%s'%area,point,height)
    

if __name__=='__main__':
    job5()