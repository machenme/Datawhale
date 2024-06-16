# Datawhale

# llm

【教程地址】https://datawhalechina.github.io/llm-universe/  
【开源项目仓库】https://github.com/datawhalechina/llm-universe  
【小程序使用说明】https://mp.weixin.qq.com/s/iPmzb72Yk0mhIA2NYezXDg  
【学习者手册】 https://mp.weixin.qq.com/s/pwWg0w1DL2C1i_Hs3SZedg  
### 新的征程已经开始,溜溜梅宇宙队冲鸭

### 6.15
一晃半个月过去了.又掌握了不少python的知识,是时候朝着星辰大海出发了!















### 作业链接 [https://hydro.ac/d/datawhale_p2s/user/50410](https://hydro.ac/d/datawhale_p2s/user/50410)
Datawhale lesson about

# p2s
## 聪明的办法学python
---
### 5.31
后记  
今天完成了结营仪式，算是真正意义上的结束了`聪明的办法学python`,不过这才是python的开始,并不是结束.期待以后的时光

---
### 5.25
随着最后一次打卡,感觉又回到了校园一样完成了一个学期,虽然只有短短半个月,仍然感觉非常有意义,这是我第一次参加这种类型的上课.也非常感谢Datawhale能够不计回报,无私奉献,也许这才是开源的真正意义.对于我这种很不自律的人来说,也许这就是一个好的开始.也许今天之后又回到了以前的状态,但是至少这是一个好的开始.后续如果有感兴趣的课程也会接着参加.到此为止python基础知识.后续要是有提高课程我还会继续.非常感谢`骆师傅` `爱吃饭助教`对我提出的问题进行详细的解答.
江湖路远,后会有期

---
### 5.23
`repr()` 返回一个对象的 string形式
```python
>>> a = 't'
>>> print(a)
t
>>> print(repr(a))
't'
>>>
```
字符串的乘法就是重复多少次,只能是字符串乘以整数  
  
`ord` 能获取字符串的ascii  
`chr` 能从ascii获取对应的字符串  

用`find`代替`index`.因为索引不存在的时候,find会返回-1 而index会报错
```python
>>> help(str.find)
Help on method_descriptor:

find(...)
    S.find(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.

Help on method_descriptor:

index(...)
    S.index(sub[, start[, end]]) -> int
    Raises ValueError when the substring is not found.
```




---
### 5.21

python里面的取值,默认都是左闭右开,能取到左边取不到右边
`range` 默认参数应该是 `range(start,end+1,1)` 

- 特别注意,如果是从负数开始,任然是依次遍历 start,start+step,start + 2 * steap, ...
- 如果是后面的字符串切片,最好统一要么都用正向索引或者统一负向索引
```python
>>> for i in range(-5,-2,1):
...     print(i)
...
-5
-4
-3
>>>
```
补充教材没有的, 对于`for`循环来说.还有个很实用的叫做`enumerate()`功能.  
```python
>>> for idx,i in enumerate(range(-1,-5,-1)):
...     print(f'index = {idx},i = {i}')
...
index = 0,i = -1
index = 1,i = -2
index = 2,i = -3
index = 3,i = -4
>>>
```

`while`循环最大的注意点在于是否有停止的条件,否则会无限循环.  
`break`会终止距离他最近的循环.  
`continue`会跳过当次循环的剩余部分.  



---
### 5.19
今天学习的`if else`条件语句,没什么好说的,说实话这章其实可以放在Day2 左右都行
### 5.17
```python
>>>int(2.9)
2  # int直接用的去尾,向上取整还得math.ceil.
>>>round(x,ndigits=None)  # 如果ndigits是None,就会返回int,其他情况均返回float
>>>round(1.0,0)  注意,哪怕是0也返回float
1.0
# 如何判断两个圆相交,从内切到外切 之间都是相交,要同时满足
if r1 + r2 >= distance and abs(r1-r2) <= distance:
```

---
### Day3
```python
5//2     # 2 
5//2.5   # 2.0  如果一个操作数 除数或者被除数是float，那么结果一定是返回float
5%2.0    # 1.0  同上，如果一个操作数是float，那么除法，取模，取余都会返回float

import math
math.floor(x)  # 返回一个int类型

>>> math.fmod(-5,2)
-1.0  # math.fmod始终与被除数的符号相同

>>> help(isinstance)
""" 
isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.
    # 返回前者是否与后者是同一类型，如果是x与一个tuple,那么会分别对x与tuple的每一项进行instance然后取或运算
    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.
"""

# 判断x是不是一个数字
import numbers
isinstacne(x,numbers.Number)
```





- 台球按行排列，其中第一行包含 1 个台球，每一行最多比上一行多 1 个球，填满这一行之后才可以填充下一行。例如，3 行最多包含 6 个台球 （1+2+3）。输入一个 int 整数 n，代表台球总数，要求编写程序，输出 row 代表台球的总行数

~~要长脑子了~~  
`ax^2 + bx + c = 0`  

n 就是台球总数  
转为等差数列， `S = (a1+an)*n/2`  
`n^2 + n - 2S = 0`   
本质上台球和盒子一样。还是要向上取整
```python
math.ceil()
```

---
### Day2
```python
# sep 和 end都是默认的，可以不写也可以改。

print('hello world', sep=' ', end='\n')
"""
双引号可以接多行注释，python中字符串与整数相乘则是重复次数。
"""
# print('h'*4) ==> 'hhhh'
```
```python
# 最大公约数
import math
print(gcd(18,36))
```

```python
import ast
ast.literal_eval
# 这玩意儿有可能导致错误，不用也罢！安心多写一个.split(',')啥的
```

# 常见错误类型

- SyntaxError  # 语法错误
- ValueError # 字符串转数字是ValueError，因为本身可以支持字符串传入，但是传入的值不合法，所以并不是TypeError！
- TypeError   # 无法接受的传入类型
- NameError  # 未导入第三方库或者没有定义该变量
- ZeroDivisionError  # 数学上除数不能为0
- 
---
### Day1
- 从来没有系统性的学习过python。正好乘着这个机会进行系统性的学习，查缺补漏。原本以为只是单纯的去`www.python.com`安装一个python应用程序就可以使用了。没想到还有conda环境，就像一个虚拟机一样把一个个python隔离开来。git也没有想象中那么复杂，最基本的git clone指令甚至都不需要手动输入而是通过github网址直接复制下来就可以开始同步了，非常的方便。目前还没有进行python的实际操作。不过基本的
  ```python
  print('Hello world')
  ```
  已经能够成功运行了。哈哈哈哈
