from pyautocad import Autocad,APoint,aDouble,aShort,distance
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
    min,max=GetBoundingBox(coor)
    leftup=APoint(min[0],max[1])
    ptlist=GetPtList(coor)
    del coor
    index0=GetIndex(ptlist,leftup)
    retVal=GetOrientionArea(ptlist)
    oriention=retVal[0]
    area=retVal[1]
    edge=retVal[2]
    height=edge/20#字高为平均边长的1/20
    num=1
    if oriention:
        for i in range(index0,index0-len(ptlist),-1):
            acad.model.AddText('J%d'%num,ptlist[i],height)
            num+=1
    else:
        for i in range(index0-len(ptlist),index0,1):
            acad.model.AddText('J%d'%num,ptlist[i],height)
            num+=1
    area=round(area,2)
    point=GetInner(ptlist)
    acad.model.AddText('面积=%s'%area,point,height)

def GetBoundingBox(coor):
    '''得到boundingbox仅限于lwpolyline
    '''
    coorx=coor[::2]
    coory=coor[1::2]
    minx,maxx=min(coorx),max(coorx)
    miny,maxy=min(coory),max(coory)
    return APoint(minx,miny),APoint(maxx,maxy)

def GetInner(ptlist):
    n=len(ptlist)
    if n==3:
        return GetCenter(ptlist)
    elif n>3:
        return GetMiddle(ptlist)
    else:
        print('非多边形')
        return

def GetMiddle(ptlist):
    return ptlist[0]/2+ptlist[2]/2

def GetCenter(ptlist):
    cenx=0
    ceny=0
    for item in ptlist:
        cenx+=item.x
        ceny+=item.y
    length=len(ptlist)
    cenx,ceny=cenx/length,ceny/length
    return APoint(cenx,ceny)

def GetOrientionArea(ptlist):
    darea=0
    edgelist=[]
    for i in range(-len(ptlist),0):
        darea+=ptlist[i].x*ptlist[i+1].y-ptlist[i].y*ptlist[i+1].x
        edgelist.append(distance(ptlist[i],ptlist[i+1]))
    aver=sum(edgelist)/len(edgelist)
    if darea>0:
        return True,darea/2,aver
    elif darea<0:
        return False,-darea/2,aver
    else:
        print('多义线未闭合')
    return

def GetIndex(ptlist,leftup):
    lenlist=[]
    for item in ptlist:
        lenlist.append(distance(item,leftup))
    index0=lenlist.index(min(lenlist))
    return index0

def GetPtList(coor):
    ptlist=[]
    for i in range(0,len(coor),2):
        ptlist.append(APoint(coor[i],coor[i+1]))
    return ptlist

if __name__=='__main__':
    job5()