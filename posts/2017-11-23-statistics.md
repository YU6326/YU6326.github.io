---
title:      "数理统计基础"
date:       2017-11-23
author:     "YU"
categories: [数学]
tags:
    - 统计
--- 

# 数理统计基础

一般地，将随机变量大写，将观测值（随机变量的取值）小写，将参数的估计量加一尖（如$\hat\beta$），统计中一般是站在抽样前的立场上看，当随机变量观测之后大写也随着变成了小写。

总体：一个问题所研究的全部元素的集合
个体：总体之中的每个元素
样本：个体的指标值$(X_1,X_2,\cdots,X_n)$
样本容量(Sample Size)：样本中所包含的个体数n
样本观测值：对某次抽样观测得到$(X_1,X_2,\cdots,X_n)$的一组确定值$(x_1,x_2,\cdots,x_n)$
样本空间：样本$(X_1,X_2,\cdots,X_n)$可能取值的全体，记为$\mathscr X$,它可以是n维空间，也可以是其中的一个子集，样本的一次观测值$(x_1,x_2,\cdots,x_n)$就是样本空间的一个点$(x_1,x_2,\cdots,x_n)\in\mathscr X$
设总体X具有分布函数$F(x),(X_1,X_2,\cdots,X_n)$为取自总体的大小为n的样本，则$(X_1,X_2,\cdots,X_n)$的联合分布函数为$\prod_{i=1}^nF(x_i)$
统计量：设$(X_1,X_2,\cdots,X_n)$是来自总体X的一个样本，$T=T(x_1,x_2,\cdots,x_n)$是样本空间$\mathscr X$上的实值函数，若$T(X_1,X_2,\cdots,X_n)$也是随机变量，且不依赖于任何未知参数则$T(X_1,X_2,\cdots,X_n)$为统计量（Statistics).
记
$$
\bar X=\frac{1}{n}\sum_{i=1}^nX_i,\quad S^2=\frac{1}{n-1}\sum_{i=1}^n(X_i-\bar X)^2
$$
为样本均值和样本方差，称统计量
$$
A_k=\frac{1}{n}\sum_{i=1}^nX_i^k,\quad B_k=\frac{1}{n}(X_i-\bar X)^k
$$
为样本的k阶（原点）矩，和样本的k阶中心矩，样本的二阶中心矩$B_2$有时也记为$S_n^2$

常用关系：(下面将$\sum_{i=1}^n$简记为$\sum$)
$$
\begin{aligned}
\sum(X_i-\bar X)^2=& \sum(X_i^2+\bar X^2-2\bar XX_i)\\
=& \sum X_i^2+n\bar X^2-2\bar X\sum X_i\\
=&\sum X_i^2-n\bar X^2
\end{aligned}
$$
将总体的期望和方差记为$\mu,\sigma^2$,即：
$$
E(X)=\mu,\quad var(X)=\sigma^2
$$
(var是方差的现代记法)

## 多元正态分布

若随机向量X的联合分布密度函数为：
$$
f(x)=\frac{1}{(2\pi)^{\frac{n}{2}}|B|^{\frac{1}{2}}}\exp{(-\frac{1}{2}(x-a)'B^{-1}(x-a))}
$$
其中B为正定阵，则称随机向量X所服从的分布为多元正态分布，简记为$X\sim N_n(\mathbf a,B)$

记法：设$X=(X_1,X_2,\cdots,X_n)',Y=(Y_1,Y_2,\cdots,Y_n)'$是两个随机向量，$Z=(Z_{ij})_{r\times s}$为随机矩阵，记：
$$
E(X)=(E(X_1),\cdots,E(X_n)),\quad E(Z)=(E(Z_{ij}))_{r\times s}
$$
$$
var(X)=E((X-E(X))(X-E(X))')
$$
$$
\rho_{ij}=\frac{cov(X_i,X_j)}{\sqrt{var(X_i)var{(X_j)}}}
$$
为$X_i$与$X_j$之间的线性相关系数，简称相关系数。

$cov(X,Y)=(cov(Y,X))'=E((X-E(X))(Y-E(Y))')$

E(X)称为X的数学期望（均值），var(X)或cov(X,X)称为X的协方差阵，cov(X,Y)称为X和Y的协方差阵。

n元正态分布的性质：
* 性质一：多元正态分布的边缘分布依然是正态分布。（反之未必成立）
* 性质二：多元正态分布由它的前两阶矩完全确定。
若$X\sim N_n(a,B)$则
$$
E(X)=a,\quad var(X)=B
$$
* 性质三：多元正态分布中$X=(_{X_2}^{X_1})\sim N_a(a,B)$则$X_1,X_2$相互独立的充要条件是它们不相关（协方差矩阵为零矩阵）
* 性质四：（线性性），若$X\sim N_n(a,B)$，A是秩为m的$m\times n$的行满秩矩阵，b是m维实向量，则：
$$
Y\sim N_m(Aa+b,ABA')
$$
* 性质五：若$X\sim N_n(a,B)$，则存在一个正交变换$\Gamma $,使$Y=\Gamma(X-a$的各分量是相互独立，均值为0的正态变量。
特别地，若$X\sim N_n(a,\sigma^2I_n)$，则$Y=\Gamma X\sim N_n(a,\sigma^2)$,即标准正态随机向量在正交变换下保持分布不变性。

统计量的分布称为抽样分布(Sampling Distribution),它与样本的分布不同。

（正态总体抽样分布定理）
设$(X_1,X_2,\cdots,X_n)$是取自正态总体$N(\mu,\sigma^2)$的一个样本，则：
* $\bar X\sim N(\mu,\sigma^2/n)\iff \sqrt n\cdot \frac{\bar X-\mu}{\sigma}\sim N(0,1)$
* (总体均值方差均已知)$\frac{1}{\sigma^2}\sum (X_i-\mu)^2\sim \chi^2(n) $
* （总体方差已知）$(n-1)S^2/\sigma^2=nS_n^2/\sigma^2=\frac{1}{\sigma^2}\sum (X_i-\bar X)^2\sim \chi^2(n-1) $
* $\bar X,S^2$相互独立

(总体方差未知) $T=\frac{\bar X-\mu}{S}\sqrt n\sim t(n-1)$

(两个正态总体)设$(X_1,\cdots,X_{n_1})$是取自正态总体$N(\mu_1,\sigma_1^2)$的一个样本，$(Y_1,\cdots,Y_{n_2})$是取自正态总体$N(\mu_2,\sigma_2^2)$的一个样本，且两个样本相互独立，则：
* $F=\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}\sim F(n_1-1,n_2-2)$
* 若$\sigma_1^2=\sigma_2^2=\sigma^2$,则：
$$
T=\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{S_\omega\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}\sim t(n_1+n_2-2)
$$
其中
$$
S_\omega^2=\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}{n_1+n_2-2}
$$
称为两个样本的合并方差。(Pooled Variance)

## 参数估计

估计量(Estimator):直接用于估计参数的统计量，记作$\hat\theta$
估计值(Estimate):将观测值代人估计量得到的一个具体数值
估计(Estimation):将估计量和估计值的总称。
矩估计(Moment Estimation)：当样本很大时，经验分布函数与总体分布函数十分近似，因而样本矩在一定程度上反映总体矩的特征。(K.Pearson,1902)
将总体的矩用相应样本的矩替换。
步骤：
1. 将总体k阶矩写成参数的形式
2. 将总体k阶矩用样本k阶矩代替
3. 反解出参数

极大似然估计(Maximum Likelihood Estimator,MLE,ML估计):认为出现概率最大的事件发生(C.F.Gauss 1821,R.A.Fisher 1922)
似然(Likelihood):当某组观测值是依赖于一些参数的某一特定概率分布得到时，出现这组观测值的概率
步骤：
1. 写出样本的联合分布--似然函数
2. 取对数，求极值。

### 估计量的优良性准则

* 均方误差(Mean Square Error,MSE)：$MSE(\hat\theta)=E(\hat\theta-\theta)^2$,（没有限定偏没偏），**对于无偏估计量，均方误差就是方差**。均方误差是评价点估计最一般的标准。
关系：
$$
\begin{aligned}
MSE(\hat\theta)=&E((\hat\theta-E\hat\theta)+(E\hat\theta-\theta))^2\\
=& E(\hat\theta-E\hat\theta)^2+E(E\hat\theta-\theta)^2+2E(\hat\theta-E\hat\theta)(E\hat\theta-\theta)\\
=& var(\hat\theta)+(E\hat\theta-\theta)^2+0\\
=& var(\hat\theta)+b^2
\end{aligned}
$$
均方误差的平方等于方差加上偏差的平方
* 无偏性 $E(\hat\theta)=\theta$
* 偏(Bias):$b=E(\hat\theta)-\theta$(与系统误差类似)
* 渐近无偏估计 $\lim_{n\to \infty}E(\hat\theta)=\theta$
* 可估函数：对于参数$\theta$的任一实值函数，如果θ的无偏估计量存在，也就是说有估计量$T=T(X_1,\cdots,X_n)$对一切θ，有：
$$E(T)=g(\theta)$$
则称$g(\theta)$为可估函数。
不可估函数是存在的，设总体$X\sim b(n,p),0\lt p\lt 1,X_1$(一次试验)是取自这个总体的一个样本，则函数$g(p)=1/p$不可估。
$proof$
假设$g(p)$可估，构造一个估计量$T(X_1)$,记它的值为$T(i)=c_i,i=0,1,\cdots,n$使得对一切$0\lt p\le 1$，都有：
$$
E(T(X_1))=\sum_{i=0}^nc_i\binom{n}{k}p^i(1-p)^{n-i}=\frac{1}{p}
$$
这显然是不可能的，只要$g(p)$不是次数小鱼等于n的多项式，g(p)的无偏估计都不存在。
如果$\hat\theta$是θ的无偏估计，不能推出$g(\hat\theta)$是g(θ)的无偏估计，除非g是线性函数。
* 有效性 如果$\hat\theta$与$\hat\theta^*$都是未知参数$\theta$的无偏估计，如果
$$
var(\hat\theta^2)\le var(\hat\theta)
$$
则称$\hat\theta^*$比$\hat\theta$有效

* 一致最小方差无偏估计
我们引入下面记号，记
$$
U\overset{\triangle}{=}\{T:E(T)=g(\theta),var(T)\le\infty,\forall \theta\in\Theta \}
$$
U为可估函数g(θ)的方差有限的无偏估计的集合
$$
U_0\overset{\triangle}{=}\{T:E(T)=0,var(T)\le\infty,\forall \theta\in\Theta \}
$$
$U_0$是数学期望为0，方差有限的估计量的集合

定义：设T为可估函数$g(\theta)$的无偏估计量，若对于任意的$\theta\in\Theta$，和$g(\theta)$的任意无偏估计量T，都有
$$
var(T_1)\le var(T)
$$
则称$T_1$是$g(\theta)$的一致最小方差无偏估计量(Uniformly Minimum Variance Unbiased Estimator,UMVUE)

**定理**：设$T(X)$是$g(\theta)$的无偏估计，$var(T(X))\lt\infty,$则$T(X)$为UMVUE的充要条件是
$$\forall \varphi(X)\in U_0,cov(\varphi(X),T(X))=0\iff E(\varphi T)=0$$
$proof.$
必要性：设$T(X)$是$g(\theta)$的UMVUE，$\forall \varphi(X)\in U_0,\lambda\in R$
$\varphi'(X)=\lambda\varphi(X)+T(X)\in U,$
$var(T(X))\le var(\lambda\varphi(X)+T(X)),(\because T(X) is UMVUE)$
$\therefore \lambda^2var(\varphi(X))+2\lambda cov(\varphi(X),T(X))\ge 0 $
由$\lambda\in R$的任意性知：$cov(\varphi(X),T(X))=0,\forall \theta\in\Theta$


充分性：设$\forall \varphi(X)\in U_0,cov(\varphi(X),T(X))=0,\forall \theta\in\Theta$,要证$T(X)$是$g(\theta)$的UMVUE，若$\varphi'(X)\in U,T(X)-\varphi'(X)\in U_0$,由假设条件得：
$$
\begin{aligned}
& cov(T(X)-\varphi'(X),T(X))=0\\
& \because cov(X,Y)=E(XY)-EXEY\\
& E(T-\varphi'(X))T(X)=0\\
& E(T^2)-E(T\varphi')=0
\end{aligned}
$$
由Schwarz不等式知：
$$
E^2T^2=E^2(T\varphi')\le ET^2E\varphi'^2
$$
$\therefore ET^2\le E\varphi'^2$
又$ET=E\varphi'=g,varX=EX^2-E^2X$
$varT\le var\varphi'$
由$\varphi'\in U$的任意性可知，T是g的UMVUE

* 相合性：
定义：设T是$g(\theta)$的一个估计量，若对于任何$\theta\in\Theta,T_n$依概率收敛于$g(\theta)$,则称$T_n$是g的相合估计(Consistent Estimator)
$$
\lim_{n\to\infty}Pr\{|T_n-g(\theta)|\gt\varepsilon\}=0
$$








