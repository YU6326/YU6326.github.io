import tkinter.filedialog as tkFileDialog
import numpy as np
from numpy import sin,cos
import os

def InnerOrientation(mat1,mat2):
    """
    mat1 为像素坐标，4*2，mat2为理论坐标4*2,
    h0,h1,h2,k0,k1,k2,这六个参数由下列矩阵定义：
    [x]=[h0]+[h1 h2] [i]
    [y]=[k0]+[k1 k2] [j]
    返回6个定向参数的齐次矩阵,x方向单位权方差，y方向单位权方差
    [h1 h2 h0]
    [k1 k2 k0]
    [0  0  1 ]
    """
    # mat1=np.matrix(mat1)
    # mat2=np.matrix(mat2)
    y=mat2.ravel()
    y=y.T
    xlist=[]
    for i in range(int(y.size/2)):
        x0=np.matrix([[1,mat1[i,0],mat1[i,1],0,0,0],[0,0,0,1,mat1[i,0],mat1[i,1]]])
        xlist.append(x0)
    x=np.vstack(xlist)
    # print(x)
    N=np.linalg.inv(x.T @ x)
    beta=N @ x.T @ y
    # print(beta)
    r=(np.size(y)-6)
    e=y-x@beta
    ex=e[0::2]
    ey=e[1::2]
    sigmax=(np.linalg.norm(ex)/r)
    sigmay=(np.linalg.norm(ey)/r)
    # print(sigmax)
    # print(sigmay)
    return(np.matrix([[beta[1,0],beta[2,0],beta[0,0]],[beta[4,0],beta[5,0],beta[3,0]],[0,0,1]]),sigmax,sigmay)

def openkbfile():
    #default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
    fname = tkFileDialog.askopenfilename(title=u"选择文件",filetypes=[("kb file", "*.kb"), ("all", "*.*")],initialdir=r"D:\学习\摄影测量\摄影测量实验数据-后方交会、前方交会")
    f=open(fname,mode='r')
    lines=f.readlines()
    f.close()
    mat=[]
    for line in lines:
        t=line.split()
        mat.append([float(t[0]),float(t[1])])
    #initialdir=(os.path.expanduser(default_dir))
    # print(fname)  # 返回文件全路径
    mat1=mat[0::2]
    mat2=mat[1::2]
    mat,sigmax2,sigmay2=InnerOrientation(np.matrix(mat1),np.matrix(mat2))
    print(mat,sigmax2,sigmay2)

# def transform(mat,coormat):
#     """
#     mat:齐次矩阵，由InnerOrientation获得
#     coormat:齐次坐标：即每列第三个元素为1，每个坐标均为列向量。列数不限。
#     返回：转换后的坐标
#     """
#     return mat@coormat
# def openaofile():
#     fname = tkFileDialog.askopenfilename(title=u"选择文件",filetypes=[("ao.txt file", "*.txt"), ("all", "*.*")],initialdir=r"D:\学习\摄影测量\摄影测量实验数据-后方交会、前方交会")
#     f=open(fname,mode='r')
#     lines=f.readlines()
#     f.close()
#     matimage=[]
#     matground=[]
#     for line in lines[1:]:
#         t=line.split()
#         matimage.append([float(t[0]),float(t[1])])
#         matground.append([float(t[2]),float(t[3]),float(t[4])])
#     return(np.matrix(matimage),np.matrix(matground))

# def resection():
#     matimage,matground=openaofile()
#     dist=np.linalg.norm(matimage[1]-matimage[0])
#     Dist=np.linalg.norm(matground[1]-matground[0])
#     matimage=matimage.T
#     matground=matground.T
#     n=dist.shape[0]
#     assert n==5
#     m=Dist/dist
#     x0,y0,f=0,0,210.681 #均以毫米作单位
#     Xs0,Ys0,H=np.average(matground,axis=0)
#     H+=m*f
#     phi,omega,kappa=0,0,0
#     R=np.zeros((3,3))
#     R[0,0]=cos(phi)*cos(kappa)-sin(phi)*sin(omega)*sin(kappa)
#     R[0,1]=-cos(phi)*sin(kappa)-sin(phi)*sin(omega)*cos(kappa)
#     R[0,2]=-sin(phi)*cos(omega)
#     R[1,0]=cos(omega)*sin(kappa)
#     R[1,1]=cos(omega)*cos(kappa)
#     R[1,2]=-sin(omega)
#     R[2,0]=sin(phi)*cos(kappa)+cos(phi)*sin(omega)*sin(kappa)
#     R[2,1]=-sin(phi)*sin(kappa)+cos(phi)*sin(omega)*cos(kappa)
#     R[2,2]=cos(phi)*cos(omega)
#     matimage1=np.zeros((2,5))
#     S=np.matrix([Xs0,Ys0,H]).T
#     Alist=[]
#     Vlist=[]
#     Llist=[]
#     for i in range(5):
#         u=matground[:,i]-S
#         matimage1[0,i]=-f*np.dot(R[0],u)/np.dot(R[2],u)
#         matimage1[1,i]=-f*np.dot(R[1],u)/np.dot(R[2],u)
#         zba=np.dot(R[2],u)
#         A=np.zeros(2,6)
#         # A[0,0]=(R[0,0]*f+R[0,2]*matimage[])[]
    

if __name__=="__main__":
    openkbfile()