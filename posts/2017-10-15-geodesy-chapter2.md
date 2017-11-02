---
title:      "地球坐标系和地球椭球"
date:       2017-10-15
author:     "YU"
categories: [大地测量]
tags:
    - 大地测量
    - 微分几何
---


## 定义

**子午圈（经圈）**：过旋转轴的平面（子午面）与椭球面的交线椭圆。
**平行圈（纬圈）**：正交于旋转轴的平面与椭球面的交线圆。
**赤道圈**：最大的平行圈，其所在的平面（赤道面）过椭圆中心。
**Frenet(伏雷内)标架**：利用曲线上任一点处的三个单位正交基构成的三维直角坐标系。其中T轴指向曲线的切线方向，N轴指向曲线的主法线方向，B轴指向曲线的副法线方向。
(注意$\{T,P,R\}$不是右手系，$\{T,P',R\}$才是右手系,按定义来讲不是Frenet标架，但是$\{T,R,P\}$是曲面的自然标架。)
**大地经度L**：是指通过地面A点和地球椭球体旋转轴的平面与起始大地子午面（本初子午面）间的夹角L。
**大地纬度B**：椭球面在该点处的法线与赤道面的夹角。
**归化纬度u**：该点所在的子午面上的椭圆的对应的外接圆的圆心角
**球心纬度Φ（地心纬度）**：该点与椭球球心的连线与赤道面的夹角
**法截面**：过椭球面上一点的椭球面法线所在平面。
**法截线（法截弧）**：法截面同椭球面的交线。
**卯酉线**：过椭球面上一点M作与该点子午线切线MT相正交的法截面，它与椭球面的交线
**法曲率**：？
**大地方位角A**：？ 
**平均曲率半径（高斯曲率半径）**：一点上所有方向法截线的曲率半径的平均值

## 旋转椭球面数学表达式

### 直角坐标方程

$$ \frac{X^2}{a^2}+\frac{Y^2}{a^2}+\frac{Z^2}{b^2}=1 $$
(由两个独立参数唯一确定)
离心率(第一偏心率）和扁率：
$$ e=c/a=\frac{\sqrt{a^2-b^2}}{a} \qquad \alpha=\frac{a-b}{a} $$
起始子午线的方程：
$$ \frac{X^2}{a^2}+\frac{Z^2}{b^2}=1,\quad Y=0 $$
经度为L的经线的方程：
$$ 
\frac{X^2}{a^2}+\frac{Y^2}{a^2}+\frac{Z^2}{b^2}=1,\quad \frac{Y}{X}=\tan L
$$

### 参数方程

![picture1](https://github.com/YU6326/YU6326.github.io/raw/master/images/归化纬度.jpg)

#### 1. 以大地经度L及归化纬度u为参数

起始子午线参数方程：
$$
X_0=a\cos u,\quad Y_0=0,\quad Z_0=b\sin u 
$$
<p align="right">(A)</p>

绕Z轴旋转即得参数椭球面参数方程：
$$ \left\{
\begin{aligned}
&X=a\cos u\cos L\\
&Y=a\cos u\sin L\\
&Z=b\sin u
\end{aligned}
\right.
$$
可推得：经线和纬线处处正交。

#### 2. 以大地经度L及大地纬度B为参数

起始子午线方程：
$$ \frac{X^2}{a^2}+\frac{Z^2}{b^2}=1 $$
<p align="right">(1) </p>

在M点处的法向量：
$$ (\frac{2X}{a^2},\frac{2Z}{b^2})$$
根据B的定义有：
$$\tan B=\frac{2Z}{b^2}/\frac{2X}{a^2} $$
即：
$$Z=X(1-e^2)\tan B $$
<p align="right">(2)</p>

联立（1）（2）有：
$$
\left\{
    \begin{aligned}
    &X=\frac{a\cos B}{\sqrt{1-e^2\sin^2 B}} \\
    &Z=\frac{a(1-e^2)\sin B}{\sqrt{1-e^2\sin^2 B}}
    \end{aligned}
\right.
$$
<p align="right">(B)</p>

令$W=\sqrt{1-e^2\sin^2 B},\quad N=\frac{a}{W} $
绕Z轴旋转有：
$$
\left\{
    \begin{aligned}
    &X=N\cos B\cos L \\
    &Y=N\cos B\sin L \\
    &Z=N(1-e^2)\sin B
    \end{aligned}
\right.
$$
<p align="right">(3)</p>

#### 3. 以大地经度L及球心纬度Φ为参数

起始子午线方程：
$$ \frac{X^2}{a^2}+\frac{Z^2}{b^2}=1 $$
椭圆的圆心极坐标方程：
$$ \rho=a\sqrt{\frac{1-e^2}{1-e^2\cos^2 \Phi}} $$
由关系式
$$
    X=\rho\cos \Phi,\quad Z=\rho\sin \Phi
$$
得
$$
X=a\cos\Phi\sqrt{\frac{1-e^2}{1-e^2\cos^2 \Phi}},\quad
Z=a\sin\Phi\sqrt{\frac{1-e^2}{1-e^2\cos^2 \Phi}}
$$
<p align="right">(C)</p>

绕Z轴旋转有：
$$
\left\{
    \begin{aligned}
    &X=a\cos\Phi\cos L\sqrt{\frac{1-e^2}{1-e^2\cos^2 \Phi}} \\
    &Y=a\cos\Phi\sin L\sqrt{\frac{1-e^2}{1-e^2\cos^2 \Phi}} \\
    &Z=a\sin\Phi\sqrt{\frac{1-e^2}{1-e^2\cos^2 \Phi}} 
    \end{aligned}
\right.
$$
比较（A)(B)(C)有：
$$
\begin{aligned}
\sin u &=\frac{\sin B\sqrt{1-e^2}}{\sqrt{1-e^2\sin^2 B}}\\
\cos u &=\frac{\cos B}{\sqrt{1-e^2\sin^2 B}} \\
\\
\tan u &=\sqrt{1-e^2}\tan B \\
\tan \Phi &=(1-e^2)\tan B
\end{aligned}
$$

### 旋转椭球面的几何性质

1. 对称性
有三个对称面，一个对称中心
2. 有界性
$$
|X| \le a,\quad |Y|\le a,\quad |Z|\le b
$$
3. 正则性（法向量不为0）
椭圆$ \frac{X^2}{a^2}+\frac{Y^2}{a^2}+\frac{Z^2}{b^2}=1 $的法向量：
$$ (\frac{2X}{a^2},\frac{2Y}{a^2},\frac{2Z}{b^2})$$
将（3）式带入并单位化得：
$$ \vec{n}=(\cos B\cos L,\cos B\sin L,\sin B) $$
4. 不可展性
旋转椭球面为不可展曲面

## 法截线的曲率及曲率半径

1. 空间曲线的曲率
由微分几何知识有：
$$\kappa=\frac{|r'(t)\times r''(t)|}{|r'(t)|^3}$$

2. 椭球面法截面曲率半径
    * 显然，法截面有无数个，相应的有无数条法截线，它们都是平面曲线。
    * 子午线曲率半径
    以归化纬度为u为子午椭圆方程的参数
    $$
    r(u)=
    \begin{pmatrix}
    x(u)\\y(u)\\z(u)
    \end{pmatrix}=
    \begin{pmatrix}
    a\cos u\\0\\b\sin u
    \end{pmatrix}
    $$
    由前式可得：
    $$\kappa(u)=\frac{ab}{\sqrt{(b^2\cos^2 u+a^2\sin^2 u)^3}}$$
    $$\kappa(B)=\frac{W^3}{a(1-e^2)}$$
    通常用M为子午线曲率半径的符号：
    $$M=\frac{1}{\kappa}=\frac{a(1-e^2)}{W^3}$$
    * 卯酉线曲率半径
    $N=a/W$(推导未知)
    * 任意方向法截线的曲率半径
    由微分几何Eular公式有
    $$k_A=\frac{\cos^2 A}{M}+\frac{\sin^2 A}{N} $$
    $$R_A=\frac{MN}{N\cos^2 A+M\sin^2 A} $$
    * 平均曲率半径
    $$R=\frac{1}{\pi/2-0}\int_0^{\pi/2}R_AdA=\frac{2}{\pi}\int_0^{\pi/2}\frac{MN}{N\cos^2 A+M\sin^2 A}dA $$
    由积分公式
    $$\int\frac{dx}{a^2\cos^2 x+b^2\sin^2 x}=\frac{1}{ab}\arctan(\frac{b}{a}\tan x)+C $$
    可知
    $$R=\sqrt{MN}=\frac{a\sqrt{1-e^2}}{W^2}$$
    又知道
    $$
    \begin{aligned}
    W=&\sqrt{1-e^2\sin^2 B} \\
    N=&\frac{a}{W}\\
    M=&\frac{a(1-e^2)}{W^3}
    \end{aligned}
    $$
    由于
    $$W\ge \sqrt{1-e^2}$$
    当且仅当$B=90^\circ$时取等号
    所以有$N\ge R\ge M$
    即任意方向曲率半径大小介于同纬度子午线和卯酉线曲率半径之间。

## 有关弧长、面积的计算

1. 由定义给出：$E=M^2,F=0,G=N^2\cdotp \cos^2 B$
2. 微小弧段$dS=\sqrt{M^2dB^2+N^2\cos^2 B\cdotp dL^2}$
3. 子午线弧长
不妨取其实子午线，其参数方程
$$
\left\{
\begin{aligned}
X=&a\cos u \\
Z=&b\sin u
\end{aligned}\right.
$$
其弧长
$$
\begin{aligned}
S_{1\sim2}=&\int \sqrt{a^2\sin^2 u+b^2\cos^2 u}du \text{第一类椭圆积分}\\
=&\int MdB\\
=&a(1-e^2)\int_{B_1}^{B_2}(1-e^2\sin^2 B)^{-\frac{3}{2}}dB\text{第三类椭圆积分}
\end{aligned}
$$

matlab中的函数
ellipticPi(n,m) %第三类完全椭圆积分
ellipticPi(n,phi,m) %第三类不完全椭圆积分
The incomplete elliptic integral of the third kind is defined as follows:
$$
\Pi(n;\varphi|m)=\int_0^\varphi\frac{1}{(1-n\sin^2\theta)\sqrt{1-m\sin^2\theta}}d\theta
$$
ellipticPi(n,pi/2,m)=ellipticPi(n,m)
故
$$S_{1\sim2}=a(1-e^2)(ellipticPi(e^2,B_2,e^2)-ellipticPi(e^2,B_1,e^2))
$$
## 参考资料
1. 现代大地控制测量（第二版） 施一民 测绘出版社