# 这是我的一个Github page

记录有关Geographic Information System的学习笔记

版权声明：商业转载请联系作者获得授权,非商业转载请注明出处(https://YU6326.github.io），若存在侵权请联系作者删除。

email: yuzhouwei6326@outlook.com


<p align="center">
[View on Github](https://github.com/YU6326)
</p>

## 地理空间数据库原理

* [地理配准](posts/2017-10-15-地理配准.md)
* [ArcGIS矢量化](posts/2017-10-15-矢量化.md)
* [CAD数据入库及拓扑检查](posts/2017-10-15-数据入库.md)

## 计算机图形学

* [VBA语法速查](posts/2017-10-17-VBA语法.md)
* [几何变换](posts/2017-10-17-坐标变换.html)

## 现代大地控制测量

**写作宗旨**:拒绝毫无根据的结论和简陋的推导，不引入无意义的量
* [微分几何基础](posts/2017-10-15-diffgeo.html)
* [地球坐标系和地球椭球](posts/2017-10-15-geodesy-chapter2.html)

## 摄影测量

* [射影几何基础](posts/2017-10-17-projgeo.html)
* [摄影测量专业词汇](posts/2017-10-17-vocabulary.md)

## 小程序

### lisp

* [lisp小程序](posts/2017-10-16-lisp.md)

### python

开发环境：python3.6.2 64bit AutoCad2016(据说python3.4支持更好)

#### 某些bug：

* iter\_objects(),find\_one()无法使用,在python3.4中无此bug
* 函数无法从输入的参数中获得返回值(如getboundingbox),在python3.4中无此bug
* 无法传递第一个参数为空的optional变量(如getpoint(,'prompt'))
* GetPoint()在多次获取点坐标时可能会失败(<0.2)
* 选择集删除可能会不成功(<0.1)
* str类型的变量偶尔会无法转换(<0.05)
