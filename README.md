# Datawhale
Datawhale lesson about

# p2s

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

# Python学习日记

### Day1
- 从来没有系统性的学习过python。正好乘着这个机会进行系统性的学习，查缺补漏。原本以为只是单纯的去`www.python.com`安装一个python应用程序就可以使用了。没想到还有conda环境，就像一个虚拟机一样把一个个python隔离开来。git也没有想象中那么复杂，最基本的git clone指令甚至都不需要手动输入而是通过github网址直接复制下来就可以开始同步了，非常的方便。目前还没有进行python的实际操作。不过基本的
  ```python
  print('Hello world')
  ```
  已经能够成功运行了。哈哈哈哈
