---
title:      "射影测量名词对照"
date:       2017-11-7
author:     "YU"
categories: [摄影测量]
tags:
    - 摄影测量
--- 

# 摄影测量与射影几何

## 摄影测量名词数学解释

此文目的：用射影几何用语来解释摄影测量词汇。
记号：前面的记号为摄影测量中的记号，后面的记号为射影几何中的记号。摄影测量中的记号以大写字母表示地平面上的点，以小写字母表示像平面上的点。
本文需要一定的射影几何基础。
参见：
[射影几何（一）](2017-10-17-projgeo.html)
[射影几何（二）](2017-11-7-projgeo2.html)

![projgeo7.1](/images/projgeo7-1.png)

设像平面P为π1，地平面E为π0。摄影物镜后节点S为投影中心O。此中心射影为$\pi_0\to \pi_1$以O为投影中心的中心射影。以下将与地平面平行的平面称为水平面，与地平面垂直的平面称为竖直面。

* 透视轴、迹线TT：自对应直线$\pi_0\times \pi_1$
* 像主点o：像平面的正截影P'
* 主距f/So：像主点到投影中心O的距离OP'
* 地主点O：像主点的原象
* 摄影方向：$\vec{OP}$的方向
* 地底点N：地平面的正截影
* 像底点n：地底点的象
* 航高SN：地底点到投影中心O的距离
* 主垂面W：过O点与π0与π1都垂直的平面(公垂面)
* 主纵线vv：主垂面在像平面上的截影
* 摄影方向线VV：主垂面在地平面上的截影
* 倾角α：π0与π1的所成的二面角
* 等角点(C,c)：地主点与地底点的射影的角平分线的截影
* 合点（灭点）：像平面上的影消点
* 合线$h_ih_i$（真水平线）：像平面上的影消线
* 合面（真水平面）Es：像平面上影消线的射影
* 主合点i：像平面上的影消线与主垂面的交点N。
* 像水平线：像平面上影消线的平行线
* 等比线$h_ch_c$：过等角点c的像水平线
* 主遁点J：地平面上影消线与主垂面的交点M

![](/images/projgeo1.png)

易知，$\triangle iSo$为等腰三角形。
**长度关系**
$$
\begin{aligned}
on=&f\tan\alpha\\
oc=&f\tan\frac{\alpha}{2}\\
oi=&f\cot\alpha\\
ci=&\frac{f}{\sin \alpha}
\end{aligned}
$$
三角关系式
$$\tan\frac{\alpha}{2}+\cot{\alpha}=\frac{1}{\sin\alpha}$$
$proof.$
设$\tan\frac{\alpha}{2}=t $
由万能公式
$$
\begin{aligned}
left=&t+\frac{1-t^2}{2t}\\
=&\frac{1+t^2}{2t}=right
\end{aligned}
$$

![](/images/projgeo2.jpg)
注意到$\triangle Sii_k$与$\triangle cii_k$均为$Rt\triangle$,又$\because Si=ci,\therefore \triangle Sii_k\cong\triangle cii_k,\therefore \angle iSi_k=\angle ici_k$

* 等角点的性质:以等角点为顶点的对应角相等。
* 等比线的性质：过等比线的水平面$P^0$是理想的水平相片，等比线是理想水平相片与航摄相片的交线，等比线上的相片比例尺等于水平相片的摄影比例尺$f/H$,不受像片倾斜的影响。

## 射影测量坐标系

* 框标坐标系
以框标中心为原点，两对边机械框标的连线为x轴y轴的右手坐标系。x轴的方向与航向一致。

* **像平面坐标系**o-xy ：仿射标架(平面直角坐标系)$(x,y)$
像平面坐标系是以像主点为原点与框标坐标系x,y轴方向一致的坐标系

* **像空间坐标系**S-xyz ：空间仿射标架$(x,y,-f)$

    $(x,y,-f)$即该点的**齐次坐标**。

    与点的齐次坐标的定义有一点不同的是，射影几何中一般直接取So为单位向量，而摄影测量用So方向的单位向量。
    <img src="/images/projgeo3.jpg" width="400">
* **像空间辅助坐标系**S-XYZ
    一种过渡坐标系，以S为原点，以航线方向为X轴，以铅垂方向为Z轴的右手空间直角坐标系。
* **摄影测量坐标系**A-XpYpZp
    一种过渡坐标系，通常以地面上的某一点A为原点，坐标轴与像空间辅助坐标系一致。
* **物空间坐标系**O-XtYtZt
    物体所在的空间直角坐标系，在小范围内可以视为左手直角坐标系

## 内外方位元素

* 内方位元素：$x_0,y_0,f$
    确定摄影机的镜头中心（严格的说是镜头的像方节点）相对于影像位置的参数
    三个参数：像主点在框标坐标系的坐标$x_0,y_0$以及主距$f$。

    已知框标坐标系，内方位元素唯一确定像平面上点的齐次坐标。

    内方位元素是已知的。

* 外方位元素:$X_s,Y_S,Z_s,\varphi,\omega,\kappa$
    确定影像或摄影光束在摄影瞬间的空间位置和姿态的参数
    六个参数：S在物空间坐标系的坐标$(X_s,Y_S,Z_s)$和三个转角。
    三个角的旋转顺序是yxz。

## 旋转变换

参见[坐标系的旋转与欧拉角](2017-11-5-rotation.html)

定义一个从像空间辅助坐标系到像空间坐标系的坐标旋转变换

旧坐标为$P=(X,Y,Z)$,新坐标为$p=(x,y,-f)$

按yxz的顺序有：
$$P=Rp=R_y(\varphi)R_x(\omega)R_z(\kappa)p $$
旋转阵R即：
$$R=R_y(\varphi)R_x(\omega)R_z(\kappa)$$
其中
$$
R_x(\theta)=
\begin{pmatrix}
1 & 0 & 0\\
0 & \cos \theta & -\sin\theta \\
0 & \sin \theta & \cos\theta
\end{pmatrix}
$$
$$
R_y(\theta)=
\begin{pmatrix}
\cos \theta & 0 & -\sin\theta\\
0 & 1 &  0\\
\sin \theta & 0 & \cos\theta
\end{pmatrix}
$$
$$
R_z(\theta)=
\begin{pmatrix}
 \cos \theta & -\sin\theta &0 \\
 \sin \theta & \cos\theta &0\\
 0 & 0 & 1
\end{pmatrix}
$$

因为多个正交阵的乘积依然为正交阵，故$R^{-1}=R^T$,故$p=R^TP$

## 共线方程

在物空间坐标系中，$S(X_s,Y_s,Z_s),A(X_A,Y_A,Z_A)$,a为A在以S为射心的中心投影下的像，a的像空间坐标和像空间辅助坐标分别为$(x,y,-f)$和
$(X,Y,Z)$

由$\vec{SA}=\lambda\vec{Sa}$知：
$$
\begin{aligned}
X=&\frac{1}{\lambda}(X_A-X_S)\\
Y=&\frac{1}{\lambda}(Y_A-Y_S)\\
Z=&\frac{1}{\lambda}(Z_A-Z_S)
\end{aligned}
$$
又$(x,y,-f)^T=R^T(X,Y,Z)^T $

所以
记$T=R^T$
$$
\begin{pmatrix}
x-x_0 \\ y-y_0 
\end{pmatrix}=
-f
\begin{pmatrix}
\frac{T[0]\cdot(A-S)}{T[2]\cdot(A-S)}\\
\frac{T[1]\cdot(A-S)}{T[2]\cdot(A-S)}
\end{pmatrix}
$$
（共线条件方程式、共线方程,$\lambda$被约掉）

-------------

$$
\begin{pmatrix}
x \\ y \\ -f
\end{pmatrix}=
\frac{R^T}{\lambda}
\begin{pmatrix}
X_A-X_S\\
Y_A-Y_S\\
Z_A-Z_S
\end{pmatrix}
$$
（已知物方坐标，求像方坐标,将第三式化上去也可以约掉）
它的逆变换为
$$
\begin{pmatrix}
X_A\\
Y_A\\
Z_A
\end{pmatrix}=\lambda R
\begin{pmatrix}
x \\ y \\ -f
\end{pmatrix}+
\begin{pmatrix}
X_S \\ Y_S \\ Z_S
\end{pmatrix}
$$
(已知像方坐标，求物方坐标)

## 像点位移

航摄像片是地面景物的中心投影，地图则是地面景物的正(射)投影。

像点位移：由于地形起伏和像片倾斜而引起的像的位置的移动。

### 像片倾斜引起的像点位移

由前述结论：由等角点引出的对应角相等可知，从等角点出发，任意像点的方向角与水平像片上相应方向线的方向角相等。

方向角的定义：以c为极点，以等比线负向为极轴的极角。（根据课本自己的定义）

设A点在$P,P^0$上的对应点为$a,a^0$,像点位移$\delta_\alpha=|\vec{ca}|-|\vec{ca_0}| $,像点位移与像片倾角α，像距ca以及方向角$\psi$有关，在等比线上无位移。在主纵线上位移最大。

(公式未经证明)
$$\delta_\alpha=-\frac{r_c^2}{f}\sin\psi\sin\alpha $$

### 地形起伏引起的像点位移

<img src="/images/projgeo4.jpg" width="400">

设像片水平，地面点A距基准面的高差为h，A在基准面的正投影为A0，A和A0的像为a、a0。

因地形起伏引起的像位移记为$\delta_h$，也称为像片上的投影差。A在基准面上的中心投影为A'。称$A_0A'$为地面上的投影差，记为$\Delta h$,将a到像底点的距离为r。H为航高

由相似关系：
$$
\frac{\Delta h}{h}=\frac{r}{f}
$$
$$
\delta_h=\frac{f}{H}\Delta h=\frac{rh}{H}
$$
$$
\Delta h=\frac{Rh}{H-h}
$$

## 像片比例尺

构像比例尺：在航摄像片上某一线段影像的长度与地面上相应线段长度之比。

只有当像片与地平面平行时，像片上任意线段的比例尺都相等。

