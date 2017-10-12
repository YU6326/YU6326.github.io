# 地球坐标系和地球椭球
## 定义

**子午圈（经圈）**：过旋转轴的平面（子午面）与椭球面的交线椭圆。
**平行圈（纬圈）**：正交于旋转轴的平面与椭球面的交线圆。
**赤道圈**：最大的平行圈，其所在的平面（赤道面）过椭圆中心。
**Frenet(伏雷内)标架**：利用曲线上任一点处的三个单位正交基构成的三维直角坐标系。其中T轴指向曲线的切线方向，n轴指向曲线的主法线方向，b轴指向曲线的副法线方向。
（主法线n：切向量的导数；副法线b：与切线和主法线垂直且符合右手法则的向量$\vec{b}=\vec{T}\times \vec{n}$。）
**大地经度L**：是指通过地面A点和地球椭球体旋转轴的平面与起始大地子午面（本初子午面）间的夹角L。
**大地纬度B**：椭球面在该点处的法线与赤道面的夹角。
**归化纬度u**：该点所在的子午面上的椭圆的对应的外接圆的圆心角
**球心纬度Φ（地心纬度）**：该点与椭球球心的连线与赤道面的夹角

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

![picture1](../images/归化纬度.jpg)

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

## 补充：微分几何知识

1. 将曲线看做动点的运动轨迹。三维空间上的曲线是连续映射$a:\mathbf{I\to R^3}$,对于$t\in \mathbf{I}$,我们用
$$ a(t)=(a^1(t),a^2(t),a^3(t)) $$
作为$a$的参数化法（parametrization)。
2. 正则曲线
    * 如果曲线的参数表示式中的函数一阶连续可微函数，这称其为光滑曲线。
    * 对于光滑曲线$r=r(t)$, 假设对于曲线$r=r(t)$上$t=t_0$有$r'(t_0)\not =0$,则称这一点为曲线上的正常点。
    * 曲线上所有点都是正常点时，则称曲线为正则曲线。
3. Frenet标架
    * 定义：对于正则曲线$\Gamma: r=r(t)$,称积分$s(t)=\int_{t_0}^t |r'(\eta)|d\eta$ 为曲线$\Gamma$从点$t_0$到$t$的弧长。
    * 自然参数：以弧长作为曲线的参数，记为s。曲线表示为$r=r(s)$
    * 自然参数的性质：
        * 切向量具有单位长度$|\dot{r}(s)|=|\frac{dr(s)}{ds}|=1$，即单位速率曲线。
        * $r(s)\perp \dot{r}(s),\dot{r}(s)\perp \ddot{r}(s)$
4. 曲率
    * 曲率(curvature)： $\kappa (s)=|\ddot{r}(s)| \quad k(s)=\lim\limits_{\Delta s\to 0}|\frac{\Delta\phi}{\Delta s}|$
    * 单位切向量(unit tangent vector)：$T(s)=\dot{r}(s),|T|=1$ 
    * 主法向量(principal normal vector)：$N(s)=\frac{\ddot{r}(s)}{k(s)},|N|=1$
    * 副法向量(binormal)：$B(s)=T(s)\times N(s),|B|=1$
    * 挠率：$\tau(s)=\dot{B}(s)\cdotp N(s)$
    * Frenet标架：$\{r(s):T(s),N(s),B(s)\}$
    * 曲率刻画了曲线的弯曲程度，刻画了曲线偏离切线的程度。
    * 挠率刻画了曲线偏离密切面的程度，是曲线非平面化的量
        * 若曲线在T正向的一方，且在密切面上面，即也在B正向的这一面，这时挠率$\tau$取正。
        * 若曲线在正向的一方，且在密切面的下面，挠率$\tau$取负。
    ![切面](../images/切面.png)
    * 定义：过空间曲线上P点的切线和P点邻近一点Q可作一平面σ，当Q点沿曲线趋于P时，平面σ的极限位置π称为曲线在P点的密切平面
    * 定义：过曲线上一点P的主法线的正侧取线段PC，使PC的长为1/k。以C为圆心以1/k为半径在密切平面上确定一个圆，这个圆称为曲线在P点的密切圆或曲率圆，圆的中心叫曲率中心，圆的半径叫曲率半径。
    在点P处的曲率圆与曲线有下列密切关系：
        1. 有公切线
        2. 凹向一致
        3. 曲率相同
    ![密切平面](../images/密切平面.png)
    * Frenet公式，其系数阵为反对称方阵
    $$
    \begin{pmatrix}
    \dot{T}(s) \\
    \dot{N}(s) \\
    \dot{B}(s)
    \end{pmatrix}
    =
    \begin{pmatrix}
    0 & k(s) & 0 \\
    -k(s) & 0 & \tau (s)\\
    0 & \tau(s) & 0
    \end{pmatrix}
    \begin{pmatrix}
    T(s) \\ N(s) \\ B(s)
    \end{pmatrix}
    $$
        * 性质：自然参数条件下，$k(s)$与$\tau (s)$唯一决定空间曲线
5. 一般参数曲线的曲率、挠率的计算
    * 空间曲线：$r=r(t)$
        * 曲率：$$k=\frac{|r'(t)\times r''(t)|}{|r'(t)|^3}$$
        * 挠率：$$\tau =\frac{r'(t)\times r''(t)\cdotp r'''(t)}{|r'(t)\times r''(t)|^2}$$   
## 法截线的曲率及曲率半径


