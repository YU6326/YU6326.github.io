# VBA语法提要

## 数据类型

数据类型|类型标识符|所占字节数
-------|--------|----------
Byte| |1
Boolean||2
Integer|%|2
Long|&|4
Single|!|4
String|$|
Double|#|8
Date| |8
Currency|@|8
Decimal| |14
Variant| |以上任意类型
Object| |4

## 标识符

由字母或下划线开头，后面可跟字母数字下划线。

## 运算符

1. 算数运算符

    按优先级顺序排列为：^, -, *, /, \, Mod, +, -

    True=-1, False=0

2. 字符串连接符

    &，+

3. 关系运算符

    =, >, >=, <, <=, <>, Like

4. 逻辑运算符

    Not, And, Or, Xor

5. 赋值运算符

    =

## 变量与常量

1. 整型
    八进制：&O，十六进制：&H 
2. 单精度
    小数形式：m.n, 指数形式：nE+-m
3. 字符串型
    “string”
4. 符号常量
    Const name [As type]=expr
5. 系统常量
    vbCrLf

* VBA允许使用未定义的变量，默认是变体变量。 
* 在模块通用说明部份，加入 Option Explicit 语句可以强迫用户进行变量定义。
* 变量定义语句及变量作用域。一般变量作用域的原则是，那部份定义就在那部份起作用，模块中定义则在该模块那作用。
    * Dim  变量 as 类型   '定义为局部变量，如 Dim   xyz as integer 
    * Private 变量 as 类型   '定义为私有变量，如 Private  xyz as byte 
    * Public 变量 as 类型   '定义为公有变量，如 Public  xyz as single 
    * Global  变量 as 类型   '定义为全局变量，如 Globlal  xyz as date 
    * Static 变量 as 类型   '定义为静态变量，如 Static   xyz as double 
* 常量为变量的一种特例，用Const定义，且定义时赋值，程序中不能改变值，作用域也如同变量作用域。

## 数组

Dim 数组名([lower to ]upper [, [lower to ]upper, ….]) as type Lower缺省值为0。二维数组是按行列排列。

如Dim X(9) as String 声明了一个10个元素的数组，X(0)~X(9),如果没有指定lower,则默认lower=0。 

除了以上固定数组外，VBA还有一种功能强大的动态数组，定义时无大小维数声明；在程序中再利用Redim语句来重新改变数组大小，原来数组内容可以通过加preserve关键字来保留。如下例：

```vb
Dim array1() as double
Redim array1(5)
array1(3)=250
Redim preserve array1(5,10) 
```

## 注释和赋值语句

1. 注释

    单引号', 如：

    ```vb
    '定义全局变量；可以位于别的语句之尾，也可单独一行
    ```
2. 赋值语句是进行对变量或对象属性赋值的语句

    采用赋值号 =，如X=123:Form1.caption=”我的窗口” 

    对对象的赋值采用：set myobject=object 或  myobject:=object

## 书写规范

1. VBA不区分标识符的字母大小写，一律认为是小写字母 
2. 最好以行只写一条语句。一行可以书写多条语句，各语句之间以冒号 : 分开
3. 一条语句可以多行书写，以空格加下划线 _ 来标识下行为续行
4. 标识符最好能简洁明了，不造成歧义

## 语句

### 判断语句

1. If…Then…Else语句 
    ```vb
    If condition Then [statements] [Else elsestatements] 
    'condition 是个判断条件，
    '当condition为真True，就执行Then后面的statements那些语句
    '如果为假False,执行elsestatements语句 
    '如：
    If A>B And C<D Then A=B+2 Else A=C+2
    If x>250 Then x=x-100 
    '或者，可以使用块形式的语法，即If…Then…Else语句 可以嵌套： 
    If condition Then 
    [statements] 
    [ElseIf condition-n Then 
    [elseifstatements]
    '...
    [Else 
    [elsestatements]] 
    End If 
    '如:
    If Number < 10 Then 
    Digits = 1 
    ElseIf Number < 100 Then
    Digits = 2 
    Else 
    Digits = 3 
    End If 
    ```
2. Select Case…Case…End Case语句

    如：Pid的取值来决定执行不同的语句

    ```vb
    Select Case Pid
        Case "A101"
            Price = 200   '当Pid的实际值是“A101”，就执行Price=200.后面的以此类推 
        Case "A102" 
            Price = 300
        Case Else 
            Price = 900 
    End Select
    ```

### 循环语句

1. For Next语句

    以指定次数来重复执行一组语句

    ```vb
    For counter = start To end [Step step]    ' step 缺省值为1 
    [statements] 
    [Exit For] 
    [statements] 
    Next [counter] 
    '如：for语句也可以嵌套，如下，两重for循环
    For Words = 10 To 1 Step -1  ' 建立 10 次循环
        For Chars = 0 To 9         ' 建立 10 次循环 
            MyString = MyString & Chars     ' 将数字添加到字符串中     
        Next Chars          ' Increment counter     
        MyString = MyString & " "      ' 添加一个空格
    Next Words
    ```  
2. For Each…Next语句

    主要功能是对一个数组或集合对象进行，让所有元素重复执行一次语句,其作用就是遍历一遍数组或集合对象中的所有元素

    ```vb
    For Each element In group   
    'group 必要参数。对象集合或数组的名称（用户定义类型的数组除外）。 
    [Statements] 
    [Exit for] 
    [Statements]
    Next [element] 
    '如1： 
    For Each range2 In range1 
        With range2.interior 
            .colorindex=6 
            .pattern=xlSolid 
        End with
    Next
    'With…End With 语句，目的是省去对象多次调用，加快速度；语法为： 
    With object 
        [statements] 
    End With
    ```
3. Do…loop语句 

    在条件为true时，重复执行区块命令

    ```vb
    Do {while |until} condition 
    ' while 为当型循环，until为直到型循环，顾名思义，不多说啦 
    [Statements] 
    Exit do 
    [Statements] 
    Loop 
    '或者使用下面语法 
    Do   ' 先do 再判断，即不论如何先干一次再说 
    [Statements] 
    Exit do 
    [Statements]
    Loop {while | until} condition 
    ```
4. while…wend语句

    只要条件为TRUE，循环就执行 如下例：

    ```vb
    While condition 'while I<50 
    [statements] 'I=I+1
    Wend
    ```
   
## 错误处理

```vb
On Error Goto Line    '当错误发生时，会立刻转移到line行去 
On Error Resume Next  '当错误发生时，会立刻转移到发生错误的下一行去 
On Error Goto 0       '当错误发生时，会立刻停止过程中任何错误处理过程 
```

## 常用函数

1. 测试函数
    ```vb
    IsNumeric(x)        '是否为数字, 返回Boolean结果，True or False 
    IsDate(x)          '是否是日期, 返回Boolean结果，True or False 
    IsEmpty(x)      '是否为Empty, 返回Boolean结果，True or False 
    IsArray(x)     '指出变量是否为一个数组。 
    IsError(expression)   '指出表达式是否为一个错误值 
    IsNull(expression)   '指出表达式是否不包含任何有效数据 (Null)。 
    IsObject(identifier)   '指出标识符是否表示对象变量
    ```
2. 数学函数

    ```vb
    Sin(x)
    Cos(x)
    Tan(x)
    Atan(x)  '三角函数，单位为弧度 
    Log(x) '返回x的自然对数 
    Exp(x)'返回 ex 
    Abs(x) '返回绝对值 
    Int(number)
    Fix(number) '都返回参数的整数部分，区别：Int 将 -8.4 转换成 -9，而 Fix 将-8.4 转换成 -8 
    Sgn(number) '返回一个 Variant (Integer)，指出参数的正负号 
    Sqr(number) '返回一个 Double，指定参数的平方根 
    VarType(varname) '返回一个 Integer，指出变量的子类型 
    Rnd(x)'返回0-1之间的单精度数据，x为随机种子 
    ``` 
3. 字符串函数 
    ```vb
    Trim(string)     '去掉string左右两端空白 
    Ltrim(string)     '去掉string左端空白 
    Rtrim(string)     '去掉string右端空白 
    Len(string)     '计算string长度
    Left(string, x)   '取string左段x个字符组成的字符串 
    Right(string, x)    '取string右段x个字符组成的字符串 
    Mid(string, start,x)   '取string从start位开始的x个字符组成的字符串 
    Ucase(string)     '转换为大写 
    Lcase(string)     '转换为小写 
    Space(x)     '返回x个空白的字符串 
    Asc(string)     '返回一个 integer，代表字符串中首字母的字符代码
    Chr(charcode)    '返回 string，其中包含有与指定的字符代码相关的字符
    ```  
4. 转换函数

    ```vb
    CBool(expression)   '转换为Boolean型 
    CByte(expression)   '转换为Byte型 
    CCur(expression)    '转换为Currency型 
    CDate(expression)   '转换为Date型 
    CDbl(expression)    '转换为Double型 
    CDec(expression)    '转换为Decemal型 
    CInt(expression)    '转换为Integer型 
    CLng(expression)    '转换为Long型 
    CSng(expression)    '转换为Single型 
    CStr(expression)    '转换为String型 
    CVar(expression)    '转换为Variant型 
    Val(string)     '转换为数据型 
    Str(number)    '转换为String
    ```
5. 时间函数

    ```vb
    Now     '返回一个 Variant (Date)，根据计算机系统设置的日期和时间来指定日期和时间。
    Date    '返回包含系统日期的 Variant (Date)。 
    Time     '返回一个指明当前系统时间的 Variant (Date)。 
    Timer    '返回一个 Single，代表从午夜开始到现在经过的秒数。 
    TimeSerial(hour, minute, second) '返回一个 Variant (Date)，包含具有具体时、分、秒的时间。 
    DateDiff(interval, date1, date2[, firstdayofweek[, firstweekofyear]]) '返回 Variant (Long) 的值，表示两个指定日期间的时间间隔数目 
    Second(time) '返回一个 Variant (Integer)，其值为 0 到 59 之间的整数，表示一分钟之中的某个秒 
    Minute(time) '返回一个 Variant (Integer)，其值为 0 到 59 之间的整数，表示一小时中的某分钟 
    Hour(time)   '返回一个 Variant (Integer)，其值为 0 到 23 之间的整数，表示一天之中的某一钟点 
    Day(date)  '返回一个 Variant (Integer)，其值为 1 到 31 之间的整数，表示一个月中的某一日 
    Month(date)  '返回一个 Variant (Integer)，其值为 1 到 12 之间的整数，表示一年中的某月 
    Year(date)  '返回 Variant (Integer)，包含表示年份的整数。 
    Weekday(date, [firstdayofweek]) '返回一个 Variant (Integer)，包含一个整数，代表某个日期是星期几 
    ```