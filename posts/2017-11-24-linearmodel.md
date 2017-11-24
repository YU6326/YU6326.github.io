---
title:      "线性模型"
date:       2017-11-23
author:     "YU"
categories: [数学]
tags:
    - 统计
--- 
## 平差和统计的概念区别

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

在间接平差（参数平差）中，一般将线性模型叫高斯—马尔柯夫模型（G-M模型），记为$\tilde L=L+\Delta=B\tilde X,D(L)=D(\Delta)=\sigma_0^2Q$,称Q为协因数阵（权逆阵）。

Gauss-Markov条件：$cov(\varepsilon,\varepsilon)=\sigma^2I_n,E(\varepsilon)=\mathbf{0}$

有时还需假定正态条件：$\varepsilon\sim N(\mathbf{0},\sigma^2I_n)$
为了对未知参数进行估计，总假定试验次数n不小于线性回归模型包含的未知参数个数，且设计矩阵X是列满秩的，即：
$$rank(X)=k+1$$

使偏离平方和$\sum_{i=1}^n(y_i-\tilde y_i)^2$取最小值的$\beta$称为它的最小二乘估计(Least Squares Estimate)，简记为LS估计。这种求估计量的方法称为最小二乘法(Method of Least Squares)，始于C.F.Gauss(1809),H后来A.A.Markov(1900)做了重要工作，奠定了这方面基础。

## 一元线性回归模型

$$y=\beta_0+\beta_1x+\varepsilon$$

假定$E(\varepsilon)=0,var(\varepsilon)=\sigma^2$,该式称为一元线性回归模型。如果加上正态条件，称其为一元线性回归模型。因为相信大家已有概率统计知识，故直接讲一般情况——多元线性回归模型。

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

### 最小二乘估计的性质

设Y，Z为随机向量，A，B为常数矩阵，有下面两个结论：

1. $E(AY)=AE(Y)$
2. $cov(AY,BZ)=Acov(Y,Z)B^T$

性质一 $\hat\beta$是$\beta$线性无偏估计
$proof.$
由（1），$\hat\beta$显然是线性估计？。
$$E(\hat\beta)=E((X'X)^{-1}X'Y)=(X'X)^{-1}X'E(Y)=(X'X)^{-1}X'X\beta=\beta $$

性质二 $cov(\hat\beta,\hat\beta)=\sigma^2(X'X)^{-1}=\sigma^2N^{-1}$
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

性质三 (Gauss-Markov定理)$C'\hat\beta$是$C'\beta$的最好线性无偏估计，其中$\hat\beta$是$\beta$的最小二乘估计，
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
var(C'\beta=C'cov(\hat\beta,hat\beta)C=\sigma^2C(X'X)^{-1}C
$$
及
$$
\begin{aligned}
0\le&||L-X(X'X)^{-1}C||^2\\
=&L'L-C'(X'X)^{-1}C\\
\therefore& var(C'\hat\beta)\le var(T)
\end{aligned}
$$

性质四 在正态条件下，$C'\hat\beta$是$0C'\beta$的一致最小方差无偏估计。

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

性质五
1. $E(\hat\varepsilon)=\mathbf{0}$
2. $cov(\hat\varepsilon,\hat\varepsilon)=\sigma^2(I_n-X(X'X)^{-1}X')$
3. $cov(\hat\beta,\hat\varepsilon)=0$

1式显然成立，下证另外两式。
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

记设计矩阵的列向量为$X_0,X_1,\cdots,X_k$,是n维欧氏空间中的k+1个向量，它们的线性组合构成了n维空间的一个线性子空间，记为$\mathscr L(X)$,对任一向量$\hat\beta,X\hat\beta\in\mathscr L(X)$,因此β的最小二乘估计$\hat\beta$就是在$\mathscr L(X)$中寻找一个向量$X\hat\beta$是的相应的$\hat\varepsilon$长度最短，这仅当$X\hat\beta$是$Y$在$\mathscr L(X)$中的投影时才能达到，如图由$X\hat\beta=X(X'X)^{-1}X'Y$,可以称：
$$
P=X(X'X)^{-1}X'
$$
![](/images/projection.png)
为空间$\mathscr L(X)$上的投影阵(projective matrix),或帽子阵(hat matirx),容易看出，投影阵具有对称性，幂等性。
当$\hat\beta$是$\beta$的最小二乘估计时，$\hat\varepsilon$表示Y到$\mathscr L(X)$的垂线，性质五的3式表示$\hat Y$与$\hat\varepsilon$相互垂直，

记残差向量的长度平方，即
$$
Q_e=||\hat\varepsilon||^2=\hat\varepsilon'\hat\varepsilon
$$
为残差平方和
$$
\begin{aligned}
Q_e=&\hat\varepsilon'\hat\varepsilon=(Y-X\hat\beta)'(Y-X\hat\beta)=(AY)'(AY)\\
=&Y'AY=\ldots=Y'Y-\hat Y'\hat Y
\end{aligned}
$$
上式说明残差向量$\hat\varepsilon$与估计量$\hat Y$的长度平方和等于观测向量$Y$的长度平方，同时也给出了$Q_e$的不同表达式。