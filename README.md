# Datawhale

### 作业链接 [https://hydro.ac/d/datawhale_p2s/user/50410](https://hydro.ac/d/datawhale_p2s/user/50410)
Datawhale lesson about

# p2s
---
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
