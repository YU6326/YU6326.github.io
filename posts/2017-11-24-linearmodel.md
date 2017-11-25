---
title:      "线性模型"
date:       2017-11-23
author:     "YU"
categories: [数学]
tags:
    - 统计
--- 

# 平差和统计的概念区别

平差认为，或者说测量学的书籍认为，测量获得的值有一定的“误差”，需要进行“改正”，所以：
**真值=观测值+改正值**
而统计中和物理学中认为观测值是真值加上一些误差（或者称“噪声”）引起的，所以：
**观测值=真值+误差**
在摄影测量和数据处理的相关教材中沿用此规定。本文以统计的概念入手，所以沿用此规定，希望读者注意区别。

改正数和误差互为相反数。


# 线性模型

在数学中，变量关系有两种基本类型：函数关系和相关关系(dependent relationship),此种关系没有密切到如上所述的确定关系。

假设因变量y和k个自变量$x_1,x_2,\cdots,x_k$之间存在简单的线性关系：
$$y=\beta_0+\beta_1x_1+\cdots+\beta_kx_k+\varepsilon $$
其中$\varepsilon$是一个随机变量进一步假定对自变量的n组不同取值，得到因变量y的n次观测，则有：
$$Y=X\beta+\varepsilon$$

其中
$$
Y=
\begin{pmatrix}
y_1 \\ y_2 \\ \vdots \\y_n
\end{pmatrix},
X=\begin{pmatrix}
1 & x_{11} & \ldots & x_{1k}\\
1 & x_{21} & \ldots & x_{2k}\\
\vdots & \vdots & & \vdots \\
1 & x_{n1} & \ldots & x_{nk}
\end{pmatrix},
\beta=
\begin{pmatrix}
\beta_1 \\ \beta_2 \\ \vdots \\\beta_n
\end{pmatrix},
\varepsilon=
\begin{pmatrix}
\varepsilon_1 \\ \varepsilon_2 \\ \vdots \\\varepsilon_n
\end{pmatrix},
$$
这里$\varepsilon$表示随机误差向量，满足$E(\varepsilon)=\mathbf 0,cov(\varepsilon,\varepsilon)=\Sigma$
称上述模型为**线性模型**，记为$(Y,X\beta,\Sigma)$,其中，Y称为观测向量，X是k个自变量在n此观测中的取值，因为选择观测的量是可以控制的，这是试验设计问题，称X为**设计矩阵**（design matirx),$\beta$ 是未知的参数向量，一般假定$\Sigma$是已知的，在许多问题中还假定n此观测相互独立，有公共方差，此时$\Sigma=\sigma^2I_n$,这里$\sigma^2$是未知参数，称为误差方差。

Gauss-Markov条件：$cov(\varepsilon,\varepsilon)=\sigma^2I_n,E(\varepsilon)=\mathbf{0}$

有时还需假定正态条件：$\varepsilon\sim N(\mathbf{0},\sigma^2I_n)$
（注意到正态分布的性质$Y=X\beta+\varepsilon\sim N(X\beta,\sigma^2I_n)$）
为了对未知参数进行估计，总假定试验次数n不小于线性回归模型包含的未知参数个数，且设计矩阵X是列满秩的，即：
$$rank(X)=k+1$$

使偏离平方和$\sum_{i=1}^n(y_i-\tilde y_i)^2$取最小值的$\beta$称为它的最小二乘估计(Least Squares Estimate)，简记为LS估计。这种求估计量的方法称为最小二乘法(Method of Least Squares)，始于C.F.Gauss(1809),H后来A.A.Markov(1900)做了重要工作，奠定了这方面基础。

## 一元线性回归模型

$$y=\beta_0+\beta_1x+\varepsilon$$

假定$E(\varepsilon)=0,var(\varepsilon)=\sigma^2$,该式称为一元线性回归模型（Simple Linear Regression Model）。如果加上正态条件，称其为一元正态线性回归模型。因为相信大家已有概率统计知识，故直接讲一般情况——多元线性回归模型。

## 多元线性回归模型

我们在这里讨论多元线性回归模型$(Y,X\beta,\sigma^2I_n)$

### 参数$\beta$的估计

使总偏离平方和
$$
\begin{aligned}
Q(\beta)&=\sum_{i=1}^n[y_i-(\beta_0+\sum_{j=1}^kx_{ij}\beta_j)]^2 \\
&= (Y-X\beta)^T(Y-X\beta)=||Y-X\beta||^2
\end{aligned}
$$
达到最小的$\beta$记为$\hat\beta$即：
$$||Y-X\hat\beta||^2=\underset{\beta}{min}||Y-X\beta||^2$$
（2）
称$\hat\beta$为$\beta$的最小二乘估计。

$$
\begin{aligned}
Q=&Q(\beta)=(Y-X\beta)^T(Y-X\beta)\\
=& Y^TY-2\beta^TX^TY+\beta^TX^TX\beta
\end{aligned}
$$
对$\beta$求导，并令其为0
$$
\frac{\partial Q}{\partial \beta}=-2X^TY+2X^TX\beta=0
$$
整理后即有：
$$X^TX\beta=X^TY$$
称该式为正规方程组(system of normal equations),记N为正规方程组的系数阵
$$N=X^TX$$
因为N为列满秩矩阵，可逆，则：
$$\hat\beta=(X^TX)^{-1}X^TY$$
（1）
是正规方程组的解。

因为存在偏导数为0的点不是极值点的情况，下面的定理告诉我们正规方程组的解就是$\beta$的最小二乘估计

**定理**：
1. 正规方程组的解(1)必是$\beta$的最小二乘估计
2. $\beta$的最小二乘估计必为正规方程组的解。

$proof.$
1. 设$\tilde\beta$是正规方程组的解。即$\tilde\beta$满足：
$$
(X'X)\tilde\beta=X'Y
$$
$\forall \beta,$
$$
\begin{aligned}
Q(\beta)=& ||Y-X\beta||^2=(Y-X\beta)'(Y-X\beta)\\
=& [(Y-X\tilde\beta)+X(\tilde\beta-\beta)]'[(Y-X\tilde\beta)+X(\tilde\beta-\beta)]\\
=& (Y-X\tilde\beta)' (Y-X\tilde\beta)+(\tilde\beta-\beta)'X'X(\tilde\beta-\beta)+2(\beta-\tilde\beta)'X'(Y-X\tilde\beta)
\end{aligned}
$$
注意到：
$(\beta-\tilde\beta)'X'(Y-X\tilde\beta)=(\beta-\tilde\beta)'(X'Y-X'X\tilde\beta)=0$
$(\tilde\beta-\beta)'X'X(\tilde\beta-\beta)=||X(\tilde\beta-\beta)||^2\ge 0 $
$$\therefore Q(\beta)\ge (Y-X\tilde\beta)' (Y-X\tilde\beta)=Q(\tilde\beta)$$(3)
其中等号成立的充要条件为$||X(\tilde\beta-\beta)||^2= 0$,由$\beta$的任意性可知$\tilde\beta$满足（2）式，因此$\tilde\beta$是$\beta$的最小二乘估计。
2. 设$\hat\beta$是$\beta$的最小二乘估计，$\tilde\beta$是正规方程组的解，由（2）式：
$$Q(\hat\beta)\le Q(\tilde\beta)$$由（3）式：
$$Q(\tilde\beta)\le Q(\hat\beta)$$所以
$$Q(\hat\beta)=Q(\tilde\beta)$$这意味着
$$(\tilde\beta-\beta)'X'X(\tilde\beta-\beta)=||X(\tilde\beta-\beta)||^2= 0$$因此$X\tilde\beta=X\hat\beta$因为$\tilde\beta$满足正规方程，则
$$X'X\hat\beta=X'X\tilde\beta=X'Y $$则$\hat\beta$是正规方程组的解。

### 最小二乘估计的性质

设Y，Z为随机向量，A，B为常数矩阵，有下面两个常用结论：

1. $E(AY)=AE(Y)$
2. $cov(AY,BZ)=Acov(Y,Z)B^T$

**性质一** $\hat\beta$是$\beta$线性无偏估计
$proof.$
由（1），$\hat\beta$是Y的线性函数，故为线性估计。
$$E(\hat\beta)=E((X'X)^{-1}X'Y)=(X'X)^{-1}X'E(Y)=(X'X)^{-1}X'X\beta=\beta $$

**性质二** $cov(\hat\beta,\hat\beta)=\sigma^2(X'X)^{-1}=\sigma^2N^{-1}$
$proof.$
$$
\begin{aligned}
cov(\hat\beta,\hat\beta)&=cov((X'X)^{-1}X'Y,(X'X)^{-1}X'Y)\\
&=(X'X)^{-1}X'cov(Y,Y)X(X'X)^{-1}\\
&=\sigma^2(X'X)^{-1}X'X(X'X)^{-1}\\
&=\sigma^2(X'X)^{-1}
\end{aligned}
$$
可见$\hat\beta$的各分量在一般情况下并不独立

对任一k+1维向量$C=(c_0,c_1,\ldots,c_k)'$,若存在n维向量L，使$E(L'Y)=C'\beta$,则称$C'\beta$为可估函数，而可估函数$C'\beta$的最小方差线性无偏估计，称为它的**最好线性无偏估计**(Best Linear Unbiased Estimate,BLUE)

**性质三** (Gauss-Markov定理)：$C'\hat\beta$是$C'\beta$的最好线性无偏估计，其中$\hat\beta$是$\beta$的最小二乘估计，
$proof.$
由性质1易见$C'\hat\beta$是$C'\beta$的无偏估计，它显然是Y的线性函数，只需证明对$C'\beta$的任一线性无偏估计$T=L'Y$,有$var(T)\ge var(C'\hat\beta)$.
设$T=L'Y$是$C'\beta$的无偏估计，则对任意$\beta$有：
$$
E(T)=E(L'Y)=L'E(Y)=L'X\beta=C'\beta
$$
$\therefore L'X=C'$
注意到性质二，有
$$var(T)=var(L'Y)=L'cov(Y,Y)L=\sigma^2L'L $$
$$
var(C'\beta)=C'cov(\hat\beta,\hat\beta)C=\sigma^2C(X'X)^{-1}C
$$
及
$$
\begin{aligned}
0\le&||L-X(X'X)^{-1}C||^2\\
=&L'L-C'(X'X)^{-1}C\\
\therefore& var(C'\hat\beta)\le var(T)
\end{aligned}
$$
由于T是$C'\beta$的线性无偏估计，所以$C'\hat\beta$是$C'\beta$的BLUE。

Gauss-Markov定理指出，$C'\hat\beta$在$C'\beta$的一切线性无偏估计中是方差最小的，但在$C'\beta$的一切无偏估计中不一定方差最小。如果在正态性条件下，，$C'\hat\beta$是UMVUE。

**性质四** 在正态条件下，$C'\hat\beta$是$C'\beta$的一致最小方差无偏估计（UMVUE）。(UMVUE定义参看数理统计基础一文)
该性质证明需要用到的结论较多，故不证。

### $\sigma^2$的估计

由最小二乘估计原理知道，在线性模型$(Y,X\beta,\sigma^2I_n)$中，$\beta$用它的最小二乘估计$\hat\beta$代替时，Q达到最小，记
$$
\hat Y=X\hat\beta
$$
表示n个试验点处Y的回归值，
$$
\hat\varepsilon=Y-\hat Y=Y-X\hat\beta
$$
表示实际观测值Y与它的回归值之差，称为**残差**，关于残差有如下性质

**性质五**
1. $E(\hat\varepsilon)=\mathbf{0}$
2. $cov(\hat\varepsilon,\hat\varepsilon)=\sigma^2(I_n-X(X'X)^{-1}X')$
3. $cov(\hat\beta,\hat\varepsilon)=0$

1.式显然成立，下证另外两式。
记
$$
\begin{aligned}
\hat\varepsilon=&Y-X\hat\beta=Y-X(X'X)^{-1}X'Y\\
=&(I_n-X(X'X)^{-1}X')Y\overset{\triangle}{=}AY
\end{aligned}
$$
这里$A=I_n-X(X'X)^{-1}X'$
不难验证A是对称幂等阵
$$
A'=A,A^2=A
$$
$$
\begin{aligned}
cov(\hat\varepsilon,\hat\varepsilon)=&cov(AY,AY)=Acov(Y,Y)A'\\
=&\sigma^2AA'=\sigma^2A=\sigma^2(I_n-X(X'X)^{-1}X')\\
cov(\hat\beta,\hat\varepsilon)=&cov((X'X)^{-1}X'Y,AY)\\
=&(X'X)^{-1}X'cov(Y,Y)A'\\
=&\sigma^2(X'X)^{-1}X'A=0
\end{aligned}
$$

#### 几何意义

下面给出最小二乘估计几$\hat\beta$与残差$\hat\varepsilon$的几何意义。如果把某个随机变量的n个观测值看成n维欧氏空间的一个向量，在此空间中，向量Y的长度定义为$||Y||=\sqrt{Y'Y}$,两个向量的距离定义为$||Y_1-Y_2||$

记设计矩阵的列向量为$X_0,X_1,\cdots,X_k$,是n维欧氏空间中的k+1个向量，它们的线性组合构成了n维空间的一个线性子空间，记为$\mathscr L(X)$,对任一向量$\hat\beta,X\hat\beta\in\mathscr L(X)$,因此β的最小二乘估计$\hat\beta$就是在$\mathscr L(X)$中寻找一个向量$X\hat\beta$使得相应的$\hat\varepsilon$长度最短，这仅当$X\hat\beta$是$Y$在$\mathscr L(X)$中的投影时才能达到，如图由$X\hat\beta=X(X'X)^{-1}X'Y$,可以称：
$$
P=X(X'X)^{-1}X'
$$
![](/images/projection.png)
为空间$\mathscr L(X)$上的投影阵(projective matrix),或帽子阵(hat matirx),容易看出，投影阵具有对称性，幂等性。（投影阵性质特殊，可以将（n+1）维欧氏空间的向量投影到n维超平面上，是向量投影运算的一般化，在其他领域如CV等应用广泛，请特别留意）
当$\hat\beta$是$\beta$的最小二乘估计时，$\hat\varepsilon$表示Y到$\mathscr L(X)$的垂线，性质五的3式表示$\hat Y$与$\hat\varepsilon$相互垂直，

记残差向量的长度平方，即
$$
Q_e=||\hat\varepsilon||^2=\hat\varepsilon'\hat\varepsilon
$$
为残差平方和
$$
\begin{aligned}
Q_e=&\hat\varepsilon'\hat\varepsilon=(Y-X\hat\beta)'(Y-X\hat\beta)=(AY)'(AY)\\
=&Y'AY=Y'Y-Y'X(X'X)^{-1}(X'X)(X'X)^{-1}X'Y\\
=&Y'Y-\hat\beta'X'X\hat\beta=Y'Y-\hat Y'X\hat\beta\\
=& Y'Y-\hat Y'\hat Y
\end{aligned}
$$
(4)
上式说明残差向量$\hat\varepsilon$与估计量$\hat Y$的长度平方和等于观测向量$Y$的长度平方，同时也给出了$Q_e$的不同表达式。

残差$\hat\varepsilon$与随机误差$\sigma^2$有关,所以用$Q_e=||\hat\varepsilon||^2$来估计$\sigma^2$是合理的。

证明残差的平方和与$\sigma^2$的无偏估计之间关系，要用到下面三个结论
1. 设n维随机向量Y，有$E(Y)=a,cov(Y,Y)=\sigma^2I_n,A$为n阶对称常数阵，有
$$E(Y'AY)=a'Aa+\sigma^2tr(A) $$
2. 设A，B是两个使乘积AB，BA都为方阵的矩阵，则
$$tr(AB)=tr(BA)$$
3. $tr(A+B)=tr(A)+tr(B)$

**性质六** 记
$$
\hat\sigma^2=\frac{Q_e}{n-(k+1)}=\frac{Q_e}{n-t}
$$
称为残差方差(Residual Variance),有
$$
E(\hat\sigma^2)=\sigma^2
$$
$proof.$
由（4）式及上面三个结论，有：
$$
\begin{aligned}
E(Q_e)=& E(Y'AY)\\
=& \beta'X'[I_n-X(X'X)^{-1}X']X\beta+\sigma^2tr[I_n-X'(X'X)^{-1}X']\\
=& \sigma^2tr(I_n-X(X'X)^{-1}X')\\
=& \sigma^2[n-tr[X(X'X)^{-1}X']]\\
=& \sigma^2[n-tr(I_{k+1})]\\
=& \sigma^2(n-k-1)
\end{aligned}
$$
由此即得
$$
E(\hat\sigma^2)=E(\frac{Q_e}{n-k-1})=\sigma^2
$$

**性质七** 在正态性条件下
1. $\hat\beta,\hat\varepsilon$相互独立，且$\hat\beta\sim N(\beta,\sigma^2N^{-1}),\hat\varepsilon\sim N(\mathbf 0,\sigma^2 A)$
2. $\hat\beta,Q_e$相互独立
3. $\frac{Q_e}{\sigma^2}\sim\chi^2(n-k-1)$

由性质一，二，五知1.2.显然成立下证3.
$proof.$
$$
\begin{aligned}
Q_e=&Y'AY=(X\beta+\varepsilon)'A(X\beta+\varepsilon)\\
=& \beta'X'AX\beta+\beta'X'A\varepsilon+\varepsilon'AX\beta+\varepsilon'A\varepsilon
\end{aligned}
$$
注意到$A=I_n-X(X'X)^{-1}X'$,容易验证
$$\beta'X'AX\beta=0 $$ $$\beta'X'A=AX\beta=0 $$
因此
$$Q_e=\varepsilon'A\varepsilon$$
可见，残差平方和是随机误差$\varepsilon$的二次型。
因为矩阵A是对称幂等阵，因此一定存在一个n阶正交阵$\Gamma$,使$A=\Gamma^T\Lambda\Gamma,$其中$\Lambda=diag(\lambda_1,\cdots,\lambda_n),\lambda_1,\cdots,\lambda_n$是A的特征根，且$\lambda_i$非0即1，非零个数为$rank(A)=tr(A)=n-k-1,$不妨设为$\lambda_1=\cdots=\lambda_{n-k-1}=1$,记$e=\Gamma\varepsilon/\sigma$,由$\varepsilon\sim N(0,\sigma^2I_n)$及$\Gamma$的正交性可知$e\sim N(0,I_n)$,即$e=(e_1,\cdots,e_n)'$中每个分量$e_i$独立，都服从$N\sim(0,1)$,故
$$
\frac{Q_e}{\sigma^2}=(\frac{\varepsilon}{\sigma})'\Gamma'\Gamma A\Gamma'\Gamma(\frac{\varepsilon}{\sigma})=e'\Lambda e=\sum_{i=1}^{n-k-1}e_i^2\sim\chi^2(n-k-1)
$$

**性质八** 若$\varepsilon\sim N(0,\sigma^2I_n)$,则$\beta$的最小二乘估计$\hat\beta$也是$\beta$的极大似然估计，$\sigma^2$的极大似然估计为$Q_e/n$
$proof.$
$\varepsilon\sim N(0,\sigma^2I_n),Y\sim N(X\beta,\sigma^2I_n)$,有定义，Y有密度函数
$$
f(Y;\beta,\sigma^2)=(2\pi\sigma^2)^{-n/2}\exp[-\frac{1}{2\sigma^2}(Y-X\beta)'(Y-X\beta)]
$$似然函数
$$
\ln L(\beta,\sigma^2)=-\frac{n}{2}\ln 2\pi-\frac{n}{2}\ln\sigma^2-\frac{1}{2\sigma^2}(Y-X\beta)'(Y-X\beta)
$$
因此
$$
\begin{cases}
\frac{\partial \ln L}{\partial \beta}=-\frac{1}{2\sigma^2}(-2X'Y+2X'X\beta)\\
\frac{\partial \ln L}{\partial\sigma^2}=-\frac{n}{2\sigma^2}+\frac{1}{2\sigma^4}(Y-X\beta)'(Y-X\beta)
\end{cases}
$$
令它们为0，解得它们的极大似然估计为：
$$
\hat\beta_L=(X'X)^{-1}X'Y
$$ $$
\hat\sigma^2_L=\frac{1}{n}(Y-X\hat\beta_L)'(Y-X\hat\beta_L)=\frac{Q_e}{n}
$$

## 广义最小二乘估计

在线性回归模型$(Y,X\beta,\sigma^2I_n)$中，我们假定各次观测独立进行，即
$$cov(Y,Y)=\sigma^2I_n $$
我们考虑更一般的情况
$$
cov(Y,Y)=\sigma^2 Q
$$
其中Q是已知的对称阵，且$|Q|\neq 0$,将相应的线性回归模型记为$(Y,X\beta,\sigma^2Q)$

定义：设A是一个n阶复矩阵，如果存在一个n阶复矩阵B使$A=B^2$,则称B是A的平方根矩阵，记为$B=\sqrt A$

为了求未知参数$\beta,\sigma^2$的最小二乘估计，作变换$Z=Q^{-1/2}Y,U=Q^{-1/2}X$,那么
$$
E(Z)=E(Q^{-1/2}Y)=Q^{-1/2}E(Y)=Q^{-1/2}X\beta=U\beta
$$ $$
cov(Z,Z)=cov(Q^{-1/2}Y,Q^{-1/2}Y)=\sigma^2Q^{-1/2}\cdot Q\cdot Q^{-1/2}=\sigma^2I_n
$$
这样，线性回归模型$(Y,X\beta,\sigma^2 Q)$便化为$(Z,U\beta,\sigma^2I_n)$,这是前面已经讨论的情况，可得正规方程组
$$
U'U\beta=U'Z
$$ $$
X'Q^{-1}X\beta=X'Q^{-1}Y
$$
记$P=Q^{-1}$
那么$$
\hat\beta=(X'PX)^{-1}X'PY
$$
这就是$\beta$的最小二乘估计，称为广义最小二乘估计。
那么
$$
cov(\hat\beta,\hat\beta)=\sigma^2(U'U)^{-1}=\sigma^2(X'PX)^{-1}
$$
残差平方和
$$
\begin{aligned}
Q_e=||Z-U\hat\beta||^2=&||Q^{-1/2}Y-Q^{-1/2}X(X'PX)^{-1}X'PY||^2\\
=& Y'PY-Y'PX(X'PX)^{-1}X'PY\\
=& Y'PY-Y'PX\hat\beta
\end{aligned}
$$

## 平方和分解公式

记：
$S_{yy}=\sum(y_i-\bar y)^2=||Y-\mathbf 1\bar y||^2$称为总变差平方和（总体平方和，Total Sum of Squares,TSS),
$Q_e=||Y-\hat Y||^2$称为残差平方和(Residual Sum of Squares,RSS),$U=||\hat Y-\mathbf 1\bar y||^2=\sum (\hat y_i-\bar y)^2$称为表示回归值$\hat y_i$的波动，称为回归平方和(Explained Sum of Squares,ESS,Sum of Squares of Regression)
将
$$
S_{yy}=Q_e+U
$$
称为平方和分解公式
事实上：
$$
\begin{aligned}
S_{yy}=& ||Y-1\bar y||^2=||(Y-\hat Y)+(\hat Y-1\bar y)||^2\\
=&||Y-\hat Y||^2+||\hat Y-1\bar y||^2+2(Y-\hat Y)'(\hat Y-1\bar y)
\end{aligned}
$$
引用之前的A，P（投影阵）记号，显然$AP=0$y,又$||(Y-\hat Y||'1=0$
$$
\begin{aligned}
(Y-\hat Y)'(\hat Y-1\bar y)=&(Y-\hat Y)'\hat Y-(Y-\hat Y)'1\bar y\\
=& \{[I_n-X(X'X)^{-1}X']Y \}'[X(X'X)^{-1}X'Y]\\
=& Y'APY=0
\end{aligned}
$$
得证。

## 参考资料
1. 应用数理统计（第二版） 关静，张玉环，史道济 主编
