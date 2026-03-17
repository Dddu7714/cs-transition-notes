- [Python基础A+B问题1](#python基础ab问题1)
  - [输入](#输入)
  - [数据类型](#数据类型)
  - [变量赋值](#变量赋值)
  - [多重赋值](#多重赋值)
  - [计算A+B](#计算ab)
  - [循环输入输出](#循环输入输出)
  - [模块](#模块)
- [python基础2](#python基础2)
  - [列表List](#列表list)
  - [range()函数](#range函数)
  - [for循环](#for循环)
  - [题目](#题目)
  - [while循环](#while循环)
  - [题目](#题目-1)
  - [数据类型转换](#数据类型转换)
  - [sys模块](#sys模块)

# Python基础A+B问题1

## 输入
**input()**：接收的总是一个字符串，``int(input())``例如输入整数3, input()接收的内容是 "3", int("3")转为整数3  
``input("请输入一些文本: ")``  
print()函数和input()函数结合起来，实现与用户的交互 
**  
input()遇到空格不会停止接收输入，且输入的是字符串，那么使用split()方法分隔并返回一个列表（见下节）  
**split()**：()以空格分隔；(",")以,分隔

## 数据类型
int整数  
float浮点数  
bool布尔值逻辑值真假  
string字符串'或"括起来

## 变量赋值
=往往意味着把右边的值赋值给左边  
python 是一种动态类型语言，变量的数据类型可以随着分配给他们的值而改变

## 多重赋值
```python
a=b=c=42
x,y,z=1,2,3
a,b=[1,2]
```

## 计算A+B
```python
data = input().split # 将输入字符按空格分割得到数据列表
res = int(data[0])+int(data[1]) # 取元素并转换为整数，相加后赋值给res
print(res)
```

## 循环输入输出
**while循环**：在满足特定条件时重复执行代码块的控制结构，若设置条件部分为True，循环将一直执行直到使用break语句终止循环   
**try代码块**：try中的代码被尝试执行，如果未发生错误则正常执行，停止输入后输入的内容无法被正确分割成两个整数，这时由except捕获异常并执行异常处理代码   

```python
while True:
    try:
    # 尝试执行这部分程序
    except:
    # 捕获异常，执行异常处理代码
        break
```


```python
while True:
    try:
        data=input().split()
        res= int(data[0]) + int(data[1])
        print(res)
    except:
        break    
```
    

## 模块
每一个模块内部都有一个`__name__`属性  
```python
import  math
print(math.aqrt(25))

from math import sqrt
print(sqrt(25))
```
**主模块**：   
` if __name__ == "__main__":`



# python基础2

## 列表List
数据之间逗号,分隔，由方括号[]括起来  
可以包含各种数据类型   
**索引**访问列表元素，从0开始

## range()函数
是python中的一个内置类型，表示一个不可变的数字序列,<font color=red>不可以直接与数字相加减</font>   
range(stop)：0-stop(不含)  
range(start, stop)：start-stop(不含)   
range(start, stop, step)：步长控制间隔，默认为1
```python
r = range(5)
print(list(r))  # 输出: [0, 1, 2, 3, 4]
```
- 惰性计算：不立即生成所有数字，节省内存
- 不可变：创建后不能修改
- 可迭代：可以在for循环中使用
- 支持索引：可通过下表访问
```python
r = range(5)
print(r[0])   # 输出: 0
print(r[3])   # 输出: 3
print(len(r)) # 输出: 5
```

## for循环
遍历一个列表中的元素并执行循环中的代码块，list是列表，item是一个循环变量
```python
for intem in list:
    # 循环体 

persons = ["tom", "jerry", "mike"]
# 遍历列表，n表示每次循环时的值
for n in persons:
    print(n)

word = 'hello'
# 遍历字符串，letter表示字符串中的每一个字符
for letter in word:
    print(letter)
```



## 题目
```python
while True:
    try:
        N = int(input())
        for _ in range(N):
            a,b = input().split()
            print(int(a)+int(b))
    except:
        break
```

## while循环
```python
# 初始化语句
while 条件判断:
      # 迭代语句
```
例如：从1数到100
- 初始化语句：我们计数通常从1开始，也就是说，我们最开始初始化了一个值1
- 条件：判断值是否小于100，如果小于100，说明我们还没有计数完，需要继续计数，如果等于100，说明已经计数完毕，则结束计数
- 迭代语句：如果本次计数值小于100，将值加1
- 重复步骤二，再次判断值是否小于100
- 重复步骤三，计数值再加1

```python
count = 1 # 初始化
while count <= 100: # 判断
    print(count)
    # 迭代
    count = count +1
```

## 题目
```python
N = int(input())
i=0
while i < N:
    a,b=input().split()
    print(int(a)+int(b))
    i = i+1 
```
上述代码只能运行一次N的输入，但是如果先算一组N1行，接着算一组N2行就会报错，如下正确
```python
while True:
    try:
        N = int(input())
        i = 0
        while i < N:
            a,b=input().split()
            print(int(a)+int(b))
            i = i+1 
    except:
        break
```

## 数据类型转换
- 隐式：python自动完成，如整数和浮点数运算时，整数隐式转换为浮点数；while条件判断0为false,其他非0的为true
- 显式： int()、float()、str()、bool() 

## sys模块
包含了许多与系统相关的变量和函数，常用来处理输入和输出  
- sys.exit([status]): 退出程序。status 是一个整数，通常为 0 表示成功，非零表示错误。  
- sys.stdin: 标准输入流，用于从键盘或其他输入设备读取数据。
- sys.stdout: 标准输出流，用于将数据打印到屏幕
```python
# 导入 sys 模块
import sys  

# sys.stdin表示输入流，遍历获取的line表示每一行输入
for line in sys.stdin:
      # 对每行数据进行处理
```
**ipynb文件转为md**

在终端输入：
 jupyter nbconvert --to markdown 'python基础1.ipynb' 
