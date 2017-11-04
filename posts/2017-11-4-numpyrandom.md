---
title:      "numpy 随机类"
date:       2017-11-4
author:     "YU"
categories: [python]
tags:
    - python
--- 
# NumPy 随机类

## Class:numpy.random

[官网链接](https://docs.scipy.org/doc/numpy/reference/routines.random.html)

##静态方法

d0-dn分别为每个维度的长度。
空参数返回一个数。
size为一个tuple(d1,..,dn),可缺省。

* rand(d0,d1,d2,...,dn) random values in a given shape. 产生在区间\[0,1\)均匀分布的浮点随机数。

* randn(d0,d1,...,dn) 产生服从标准正态分布N(0,1)的浮点随机数

Note: 
如果$X\sim N(0,1) $
$Y=\sigma X+\mu\sim N(\mu,\sigma^2)$
For random samples from $N(\mu,\sigma^2)$，use:

> sigma * np.random * randn(...) + mu

* randint(low,high=None,size=None,dtype='i')
* random_integers(low[,high,size]) =randint(low,high,size=None,dtype=numpy.int)

返回随机整数服从$[low,hight)$的离散均匀分布，如果high没给出，则返回服从$[0,low)$的离散均匀分布。

* random_sample(size)
* random(size)
* randf(size)
* sample(size) 以上四个都是产生$[0,1)$的浮点随机数

* uniform(low,high,size) 产生在区间$[1,6)$的均匀分布浮点随机数

* normal(loc=0,scale=1,size) 产生服从N(loc,scale^2)的正态分布浮点随机数
