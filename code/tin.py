from pyautocad import Autocad,APoint,ACAD,aShort
import tkinter.filedialog as tkFileDialog
from pyptlist import PointSet,toLightWeightPolyline
from scipy.spatial import Delaunay,ConvexHull,KDTree
import numpy as np
import matplotlib.pyplot as plt


def tin():
    """
    从文件中读取点，生成tin
    """
    acad=Autocad()
    ptlist=[]
    num=acad.doc.Utility.GetInteger('请选择从：\n1.从文件中读取点 2.现有点（当前图层）生成三角网')
    if num==1:
        fname = tkFileDialog.askopenfilename(title=u"选择文件",filetypes=[("text file", "*.txt"), ("all", "*.*")],initialdir=r"D:\学习\计算机图形学")
        f=open(fname)
        lines=f.readlines()
        f.close()
        poLayer=acad.doc.Layers.Add('point')
        acad.doc.ActiveLayer=poLayer
        for i in range(1,len(lines),2):
            t=lines[i].split(',')
            ap=APoint(float(t[1]),float(t[2]),float(t[3]))
            ptlist.append(ap)
            acad.model.AddPoint(ap)
    elif num==2:
        try:
            acad.doc.SelectionSets.Item("SS1").Delete()
        except Exception:
            print('Delete selection failed')
        ss=acad.doc.SelectionSets.Add('SS1')
        ss.Select(ACAD.acSelectionSetAll,aShort([0,8]),['POINT','point'])
        for i in range(ss.Count):
            c=ss.Item(i).Coordinates
            ptlist.append(APoint(ss.Item(i).Coordinates))
    ptlist=PointSet(ptlist)
    minpo,maxpo=ptlist.GetBoundingBox()
    acad.app.ZoomWindow(minpo,maxpo)
    lineLayer=acad.doc.Layers.Add('line')
    lineLayer.Color=ACAD.acRed
    acad.doc.ActiveLayer=lineLayer
    points=np.array(ptlist)
    points=points[:,0:2]
    tri=Delaunay(points)
    for simplex in tri.simplices:
        aplist=[APoint(ptlist[simplex[0]]),APoint(ptlist[simplex[1]]),APoint(ptlist[simplex[2]])]
        lwp=acad.model.AddLightWeightPolyline(toLightWeightPolyline(aplist))
        lwp.Closed=True


def testtin():
    fname = tkFileDialog.askopenfilename(title=u"选择文件",filetypes=[("text file", "*.txt"), ("all", "*.*")],initialdir=r"D:\学习\计算机图形学")
    f=open(fname)
    lines=f.readlines()
    f.close()
    ptlist=[]
    for i in range(1,len(lines),2):
        t=lines[i].split(',')
        ap=[float(t[1]),float(t[2])]
        ptlist.append(ap)
    points=np.array(ptlist)
    tri=Delaunay(points)
    # for simplex in tri.simplices[0:10]:
    #     simplex=np.hstack((simplex,simplex[0]))
    #     plt.plot(points[simplex,0],points[simplex,1],'k-')
    plt.triplot(points[:,0],points[:,1],tri.simplices.copy())
    # plt.plot(points[:,0],points[:,1],'.')
    plt.show()

def testtin2():
    # Triangle Settings
    width = 200
    height = 40
    pointNumber = 1000
    points = np.zeros((pointNumber, 2))
    points[:, 0] = np.random.randint(0, width, pointNumber)
    points[:, 1] = np.random.randint(0, height, pointNumber)

    # Use scipy.spatial.Delaunay for Triangulation
    tri = Delaunay(points)

    # Plot Delaunay triangle with color filled
    center = np.sum(points[tri.simplices], axis=1)/3.0
    color = np.array([(x - width/2)**2 + (y - height/2)**2 for x, y in center])
    plt.figure(figsize=(7, 3))
    plt.tripcolor(points[:, 0], points[:, 1], tri.simplices.copy(), facecolors=color, edgecolors='k')
    plt.show()

    # Delete ticks, axis and background
    plt.tick_params(labelbottom='off', labelleft='off', left='off', right='off',
                    bottom='off', top='off')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')

    # Save picture
    plt.savefig('Delaunay.png', transparent=True, dpi=600)

def DelaunayTest():
    points=np.array([[0,0],[0,1.1],[1,0],[1,1]])
    tri=Delaunay(points)
    plt.triplot(points[:,0],points[:,1],tri.simplices.copy())
    # simplices:单纯形，为三个顶点的点号（行向量）组成的矩阵
    for j,p in enumerate(points):
        plt.text(p[0]-0.03,p[1]+0.03,j,ha='right')
    for j,s in enumerate(tri.simplices):
        p=points[s]
        p=p.mean(axis=0)#0表示沿着这个轴平均，即对与非这个轴的数求平均。
        plt.text(p[0],p[1],'#%d'%j,ha='center')
    plt.xlim(-0.5,1.5)
    plt.ylim(-0.5,1.5)
    plt.show()

def ConvexTest():
    points=np.random.rand(30,2)
    hull=ConvexHull(points)
    plt.plot(points[:,0],points[:,1],'o')
    for simplex in hull.simplices:
        plt.plot(points[simplex,0],points[simplex,1],'k-')
    plt.show()

def Voronoi():
    points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],[2,0],[2,1],[2,2]])
    tree = KDTree(points)
    tree.query([0.1, 0.1])
    x = np.linspace(-0.5, 2.5, 31)
    y = np.linspace(-0.5, 2.5, 33)
    xx, yy = np.meshgrid(x, y)
    xy = np.c_[xx.ravel(), yy.ravel()]
    plt.pcolor(x, y, tree.query(xy)[1].reshape(33, 31))
    plt.plot(points[:,0], points[:,1], 'ko')
    plt.show()

if __name__=="__main__":
    testtin()