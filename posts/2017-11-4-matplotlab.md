---
title:      "matplotlab python绘图"
date:       2017-11-4
author:     "YU"
categories: [python]
tags:
    - python
--- 
# matplotlab python绘图

[官方文档](http://matplotlib.org/users/pyplot_tutorial.html)

本文根据官方文档改编。

## 引入

```python
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
```

 If you provide a single list or array to the plot() command, matplotlib assumes it is a sequence of y values, and automatically generates the x values for you. Since python ranges start with 0, the default x vector has the same length as y but starts with 0. Hence the x data are [0,1,2,3].

plot() is a versatile command, and will take an arbitrary number of arguments. For example, to plot x versus y, you can issue the command:

`plt.plot([1,2,3,4],[1,4,9,16])`

*Format String*:The letters and symbols of the format string are from MATLAB, and you concatenate a color string with a line style string. The default format string is 'b-', which is a solid blue line. 

```python
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,6,0,20])
plt.show()
```

The axis() command in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies the viewport of the axes.

```python
import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

## Controlling line properties

* Use keyward args:
`plt.plot(x,y,linewidth=2.0)`

* Use the setter methods of Line2D
plot returns a **list** of Line2D objects; e.g., line1, line2 = plot(x1, y1, x2, y2). 
`line.set_antialiased(False) #turn off antialising(抗锯齿)`

* Use the setp() command
`plt.setp(lines,color='r',linewidth=2.0)


|Property |	Value Type |
|---------|------------|
alpha	| float
animated	| [True \| False]
antialiased or aa |	[True \| False]
clip_box	| a matplotlib.transform.Bbox instance
clip_on	| [True \| False]
clip_path	| a Path instance and a Transform instance, a Patch
color or c	| any matplotlib color
contains	| the hit testing function
dash_capstyle   |	['butt' \| 'round' \| 'projecting']
dash_joinstyle	| ['miter' \| 'round' \| 'bevel']
dashes	| sequence of on/off ink in points
data	| (np.array xdata, np.array ydata)
figure	| a matplotlib.figure.Figure instance
label	| any string
linestyle or ls |	[ '-' \| '--' \| '-.' \| ':' \| 'steps' \| ...]
linewidth or lw |	float value in points
lod	 | [True \| False]
marker	| [ '+' \| ',' \| '.' \| '1' \| '2' \| '3' \| '4' ]
markeredgecolor or mec	| any matplotlib color
markeredgewidth or mew	| float value in points
markerfacecolor or mfc	| any matplotlib color
markersize or ms	| float
markevery	|[ None \| integer \| (startind, stride) ]
picker	| used in interactive line selection
pickradius	|the line pick selection radius
solid_capstyle	| ['butt' \| 'round' \| 'projecting']
solid_joinstyle	| ['miter' \| 'round' \| 'bevel']
transform	|a matplotlib.transforms.Transform instance
visible	| [True \| False]
xdata	| np.array
ydata	| np.array
zorder	| any number

To get a list of settable line properties, call the setp() function with a line or lines as argument
`plt.setp(lines)`

### 常用属性简介

1. 颜色字符

| character | color |
|-----------|-------|
b | blue
g | green
r | red
c | cyan
m | magenta
y | yellow
k | black
w | white

2. 线条样式 linestyle

| linestyle | description |
|-----------|-------------|
\- | solid
\-\- | dashed
\-. | dash_dot，点画线
: | dotted,虚点线

3. 点样式 marker

| character | description |
|-----------|-------------|
. | dot
o | circle
\< \> \^ \v | 不同朝向三角形
s | square
p | pentagon(五边形)
\* | star
h | hexagon1(六边形)
H | hexagon2
\+ | plus
x | x
D | diamond
d | thin diamond

4. 坐标限 limits

plt方法：

```python
plt.axis([xmin,xmax,ymin,ymax])
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
```

5. 图例

pl.legend([plot1, plot2], (’red line’, ’green circles’), ’best’, numpoints=1)# make legend

## Working with multiple figures and axes

### 绘制多子图

```python
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211) #子图有属性axisbg 背景色
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
```
MATLAB, and pyplot, have the concept of the current figure and the current axes. All plotting commands apply to the current axes. The function gca() returns the current axes (a matplotlib.axes.Axes instance), and gcf() returns the current figure (matplotlib.figure.Figure instance). Normally, you don’t have to worry about this, because it is all taken care of behind the scenes. Below is a script to create two subplots.

The subplot() command specifies *numrows*, *numcols*, *fignum* where fignum ranges from 1 to numrows\*numcols. The commas in the subplot command are optional if numrows\*numcols<10. So subplot(211) is identical to subplot(2, 1, 1). You can create an arbitrary number of subplots and axes. If you want to place an axes manually, i.e., not on a rectangular grid, use the axes() command, which allows you to specify the location as axes([left, bottom, width, height]) where all values are in fractional (0 to 1) coordinates. See pylab_examples example code: axes_demo.py for an example of placing axes manually and pylab_examples example code: subplots_demo.py for an example with lots of subplots.

在matplotlib下，一个Figure对象可以包含多个子图（Axes），可以使用subplot()快速绘制，其调用形式如下：

>subplot(numRows, numCols, plotNum)

```python
for idx,color in enumerate('rgbyck'): 
    plt.subplot(321+idx,axisbg=color) #axisbg现在用facecolor
plt.show
```

图表的整个绘图区域被分成numRows行和numCols列，plotNum参数指定创建的Axes对象所在的区域。

### 绘制多图表

The figure() command here is optional because figure(1) will be created by default, just as a subplot(111) will be created by default if you don’t manually specify any axes. 

```python
import numpy as np
import matplotlib.pyplot as plt
plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2
ax1 = plt.subplot(211) # 在图表2中创建子图1
ax2 = plt.subplot(212) # 在图表2中创建子图2
x = np.linspace(0, 3, 100)
for i in xrange(5):
    plt.figure(1)  #❶ # 选择图表1
    plt.plot(x, np.exp(i*x/3))
    plt.sca(ax1)   #❷ # 选择图表2的子图1
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(x, np.cos(i*x))
plt.show()
```

All of the text() commands return an matplotlib.text.Text instance. Just as with with lines above, you can customize the properties by passing keyword arguments into the text functions or using setp():

`t = plt.xlabel('my data', fontsize=14, color='red')`

matplotlib accepts TeX equation expressions in any text expression. For example to write the expression  in the title, you can write a TeX expression surrounded by dollar signs:

`plt.title(r'$\sigma_i=15$')`