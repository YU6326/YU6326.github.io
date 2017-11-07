记录有关需要注意的事项

图片链接：https://github.com/YU6326/YU6326.github.io/raw/master/images/ + 图片名

文件名和后缀的大小写都要注意

主页和纯文本用的是hacker主题
其余的都是markdown preview enhanced中的主题。

代码块
```language
code
```

* md上可以用相对路径，html上似乎有问题

pyautocad的开发环境：
开发环境：python3.6.2 64bit AutoCad2016(据说python3.4支持更好)

### 某些bug：

* iter\_objects(),find\_one()无法使用,在python3.4中无此bug
* 函数无法从输入的参数中获得返回值(如getboundingbox),在python3.4中无此bug？
* 无法传递第一个参数为空的optional变量(如getpoint(,'prompt'))
* GetPoint()在多次获取点坐标时可能会失败(<0.2)
* 选择集删除可能会不成功(<0.1)
* str类型的变量偶尔会无法转换(<0.05)