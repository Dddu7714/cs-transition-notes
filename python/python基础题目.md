- [A+B问题1](#ab问题1)
  - [题目](#题目)
  - [输入](#输入)
  - [数据类型](#数据类型)
  - [变量赋值](#变量赋值)
  - [多重赋值](#多重赋值)
  - [计算A+B](#计算ab)
  - [循环输入输出](#循环输入输出)
  - [模块](#模块)
- [A+B问题2](#ab问题2)
  - [题目](#题目-1)
  - [\_占位符](#_占位符)
  - [列表List](#列表list)
  - [range()函数](#range函数)
  - [for循环](#for循环)
  - [while循环](#while循环)
  - [数据类型转换](#数据类型转换)
  - [sys模块](#sys模块)
- [A+B问题3](#ab问题3)
  - [题目](#题目-2)
  - [if语句](#if语句)
  - [关系运算符](#关系运算符)
  - [逻辑运算符](#逻辑运算符)
  - [break循环](#break循环)
  - [continue](#continue)
  - [条件运算符/三元](#条件运算符三元)
- [A+B问题4](#ab问题4)
  - [题目](#题目-3)
  - [算术运算符](#算术运算符)
  - [复合赋值运算符](#复合赋值运算符)
  - [内置数学函数](#内置数学函数)
  - [内置sum(列表, 初始值)函数](#内置sum列表-初始值函数)
  - [map(function, list)函数](#mapfunction-list函数)
- [A+B问题5](#ab问题5)
  - [题目](#题目-4)
- [数组的倒序与隔位输出6](#数组的倒序与隔位输出6)
  - [题目](#题目-5)
  - [数组](#数组)
  - [序列](#序列)
  - [可变值和不可变值](#可变值和不可变值)
  - [列表](#列表)
  - [切片](#切片)
- [摆平积木](#摆平积木)
  - [题目](#题目-6)
  - [算术运算符](#算术运算符-1)
  - [复合赋值运算符](#复合赋值运算符-1)

# A+B问题1
## 题目
- 题目描述：  
你的任务是计算 a+b。
- 输入描述：  
输入包含一系列的 a 和 b 对，通过空格隔开。一对 a 和 b 占一行。
- 输出描述：  
对于输入的每对 a 和 b，你需要依次输出 a、b 的和。  
如对于输入中的第二对 a 和 b，在输出中它们的和应该也在第二行。
- 输入示例： 
    ```text
    3 4
    11 40
    ```
- 输出示例： 
    ```text
    7
    51
    ```
- 答案：
    ```python
    while True:
        try:
            data=input().split()
            res= int(data[0]) + int(data[1])
            print(res)
        except:
            break    
    ```
## 输入
**input()**：接收的总是一个字符串，``int(input())``例如输入整数3, input()接收的内容是 "3", int("3")转为整数3  
``input("请输入一些文本: ")``  
print()函数和input()函数结合起来，实现与用户的交互 
  
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
data = input().split() # 将输入字符按空格分割得到数据列表
res = int(data[0])+int(data[1]) # 取元素并转换为整数，相加后赋值给res
print(res)
```

## 循环输入输出
为了满足多组数据的计算要求，需要循环输入输出。   
**while循环**：在满足特定条件时重复执行代码块的控制结构，若设置条件部分为True，循环将一直执行直到使用break语句终止循环   
**try代码块**：try中的代码被尝试执行，如果未发生错误则正常执行，若停止输入后输入的内容无法被正确分割成两个整数，这时由except捕获异常并执行异常处理代码   

```python
while True:
    try:
    # 尝试执行这部分程序
    except:
    # 捕获异常，执行异常处理代码
        break
```


    

## 模块
每一个模块都有一个内置属性`__name__` ，使得同一个Python文件既可以作为可执行程序运行，也可以作为模块被其他程序导入使用。 <font color=red>注意缩进！</font> 
```python
 #直接运行程序
 if __name__ == "__main__":
    # 这里写测试代码
```
```python
# math作为模块被导入
import  math
print(math.aqrt(25))

from math import sqrt
print(sqrt(25))
```



# A+B问题2
## 题目
- 题目描述：  
  计算a+b，但输入方式有所改变。
- 输入描述：  
第一行是一个整数N，表示后面会有N行a和b，通过空格隔开。  
- 输出描述：  
对于输入的每对a和b，你需要在相应的行输出a、b的和。
如第二对a和b，对应的和也输出在第二行。
- 输入示例： 
    ```text
    2
    2 4
    9 21
    ```
- 输出示例： 
    ```text
    6
    30
    ```
- 提示信息：   
  测试数据不仅仅一组。也就是说，会持续输入N以及后面的a和b
- 答案：
    ```python
    # for循环
    while True:
        try:
            N = int(input())
            for _ in range(N):
                a,b = input().split()
                print(int(a)+int(b))
        except:
            break
     ```   
- 解题过程
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
## _占位符
_ 不是特殊语法，只是一个通常表示“这个变量我不打算用”的变量名。只关心“循环几次”，不关心当前是第几次
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

## while循环  
while和while True的<font color=red>区别</font>：前者是满足条件就继续运行，后者一直运行但if某种情况才break即条件在循环内部。
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





# A+B问题3
## 题目
- 题目描述：  
  计算a+b。
- 输入描述：  
  输入中每行是一对a和b。其中会有一对是0和0标志着输入结束，且这一对不要计算。  
- 输出描述：  
对于输入的每对a和b，你需要在相应的行输出a、b的和。
如第二对a和b，对应的和也输出在第二行。
- 输入示例： 
    ```text
    2 4
    11 19
    0 0
    ```
- 输出示例： 
    ```text
    6
    30
    ```
- 答案：
    ```python
    while True: 
        try:
            s = input().split()
            a, b = int(s[0]), int(s[1])
            # 如果输入的a和b同时为0， 则终止循环，如果不是同时为0，则跳过该代码块，不执行
            if a == 0 and b == 0:
                # 遇到特定输入时退出循环
                break
            print(a + b)
        except:
            break
    ```

*自己尝试出的*
```python
while True:
    try:
        a,b=map(int,input().split())
        if (a!=0) or (b!=0):
        #if not a and not b:等价于if a==0 and b==0:
        ## 如果不加int操作，比较的是字符串 "0" 和整数 0，它们永远不相等
            print(a+b)
        else:
            print("\n")
    except:
        break
```



## if语句
条件语句，表示假设在某种条件下，代码才可以执行。  
<font color=red>注意</font>：尽量不适用else，否则时间花费会更多。  
**condition**是条件判断，返回布尔值（真和假），真-执行缩进里的代码；假-跳过这一段。
```  python
if condition:
    # 执行代码块
```
**else**语句，假设条件不满足时执行缩进里的代码。  
**elif**条件分支可以有多个，但都是在if不成立时执行。  
```python
if 有西瓜:
    # 如果有西瓜，则执行这里的代码块
elif 有苹果:
    # 在没有西瓜的情况下，有苹果，则执行这里的代码块
else:
    # 既没有西瓜，也没有苹果，上面的条件都为假，则执行这里的代码块
```
## 关系运算符
- =  右边的值赋给左边  
- ==  比较两个值之间是否相等  
- \> 左侧是否大于右侧
- < 左侧是否小于右侧
- \>=，>=
- != 不等于，两个值是否不相等
  
## 逻辑运算符
- and 都为真才真
- or 至少一个为真
- not 将条件判断的值取反后返回
```python
# 如果val是任何的非0值，条件为真，执行代码
if val:
# 如果val是0，转换为false,经过非运算后进行取反,条件为真
if not val:
```

## break循环
完全退出循环，终止离它最近的while、for语句的，break之后的代码都不会再执行，

## continue
用于控制跳出循环，同样的，它也只能出现在for、while循环的内部，跳过当前循环迭代的剩余部分，然后继续下一次循环迭代， 通常用于在某个特定条件下，跳过某些特定的迭代操作，但仍然继续循环   
```python
numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    # 当满足条件时，跳过本次迭代，继续下一次循环
    if number == 2:
        continue  # 当number等于2时，跳过本次循环迭代，但会进行number == 3的循环
    print(number)
# continue 输出1 3 4 5 6 7
# break 输出1
```
## 条件运算符/三元
经过简化后的if-else语句，先对条件表达式进行求值判断, 如果判断结果为True, 则执行语句1，并返回执行结果，如果判断结果为False, 则执行语句2，并返回执行结果  

```python
语句1 if 条件表达式 else 语句2
```


# A+B问题4
## 题目
- 题目描述：  
  计算若干整数的和。
- 输入描述：  
  每行的第一个数N，表示本行后面有N个数。
  如果N=0时，表示输入结束，且这一行不要计算。  
- 输出描述：  
  对于每一行数据需要在相应的行输出和。
- 输入示例： 
    ```text
    4 1 2 3 4
    5 1 2 3 4 5
    0
    ```
- 输出示例： 
    ```text
    10
    15
    ```

- 自己尝试  
    ```python
    while True:
        try:
            data =list(map(int, input().split()))
            N = data[0]
            if N==0:
                break
            res = 0
            for i in range(N):
                res = res + data[i+1]
            print(res)
        except:
            break
    ```
- 答案1
    ```python
    while True:
        input_line = input().split()
        n = int(input_line[0])
        if n == 0:
            break
        else:
            res = 0
            for i in range(n):
                res = res + int(input_line[i+1])
            print(res)
    ```
- 答案2 使用map, sum, 切片
    ```python
    while True:
        input_line = input().split()
        n = int(input_line[0])
        if n == 0:
            break
        else:
            numbers = list(map(int, input_line[1:]))
            res = sum(numbers)
            print(res)
    ```

## 算术运算符
加法+  
减法-  
乘法*  
除法/（总是除去浮点数）  
整除//（5//2得2）  
幂运算**（2**3=8）
取余%（10%4=2）

## 复合赋值运算符
`sum = sum + i`
```python
a += 5 # a = a + 5
a -= 5 # a = a - 5
a *= 5 # a = a * 5
**=  /=  //=  %=
```

## 内置数学函数
- abs(x): 绝对值
- max(x, y, z, ...): 最大值
- min(x, y, z, ...): 最小值
- pow(x, y): y的x次方，参数为整数
- round(x): 浮点数x的四舍五入值     
- 更多的需要`import math`
- math.ceil(x): 大于或等于x的最小整数
- math.floor(X): 向下取整，返回一个比x小的最大整数
- math.pow(x, y): y的x次方，math模块会把参数转换成浮点数
- math.sqrt(x): 返回x的平方根
- 生成随机数`import random`
```python
import random
print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数  
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数

a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
random.shuffle(a)
print(a)
```



## 内置sum(列表, 初始值)函数
- 如果在代码中重新定义了`sum变量`，将覆盖内置的`sum函数`
初始值是总和的初始值，然后将列表中的元素依次相加，如下示例
```python
sum(列表, 初始值)

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total) # 输出15
```

## map(function, list)函数
将一个函数应用到序列中的每个元素，并返回一个包含结果的新序列
- function是要应用到列表中每个元素的函数
- list是要处理的列表
```python
str_numbers = ["1","2","3","4"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)
# 输出[1, 2, 3, 4]
```


# A+B问题5
## 题目
- 题目描述:   
  你的任务是计算若干整数的和。   
- 输入描述:    
  输入的第一行为一个整数N，接下来N行每行先输入一个整数M，然后在同一行内输入M个整数。   
- 输出描述:    
  对于每组输入，输出M个数的和，每组输出之间输出一个空行。   
- 输入示例:
  ```text    
    3   
    4 1 2 3 4    
    5 1 2 3 4 5    
    3 1 2 3    
    ```
- 输出示例:   
  ```text   
    10    

    15   

    6  
    ``` 

提示：注意以上样例为一组测试数据，后端判题会有很多组测试数据，也就是会有多个N的输入，只保证每组数据内部之间有空白行，两组数据之间没有空行！  

 <font color=red>vscode输入时，按shift+enter为换行，但是上一行不显示只显示当前行，边输入边运行，eg:输入3没反应，再输4 1 2 3 4 计算出结果输出</font>

*自己尝试*
```python
while True:
    try:
        N = int(input())
        for i in range(N):
            data = list(map(int, input().split()))
            M = data[0]
            res = 0
            for j in range(M):
                res += data[j+1]
            print(res)
            if i < (N-1):
                print()
            else:
                break
    except:
        break
```
- 答案：  
    ```python
    while True:
        try:
            N = int(input())
            for i in range(N):
                input_line = input().split()
                m = int(input_line[0])
                total = 0
                # 累加 m 个数值
                for j in range(m):
                    total += int(input_line[j + 1])
                print(total)
                # 控制输出一个空行，每组数据的最后一行不输出
                if i < N-1:
                    print()
        except:
            break
    ```


# 数组的倒序与隔位输出6
## 题目
- 题目描述:    
给定一个整数数组，编写一个程序实现以下功能：  
将输入的整数数组倒序输出，每个数之间用空格分隔。  
从正序数组中，每隔一个单位（即索引为奇数的元素），输出其值，同样用空格分隔。       
- 输入描述:    
第一行包含一个整数 n，表示数组的长度。  
接下来一行包含 n 个整数，表示数组的元素。    
- 输出描述:  
  首先输出倒序排列的数组元素，然后输出正序数组中每隔一个单位的元素。    

- 输入示例:
  ```text    
    5   
    2 3 4 5 6   
  ```
    
- 输出示例:      
  ```text
    6 5 4 3 2    
    2 4 6   
  ```
- 提示：   
  数据范围1 <= n <= 1000.   

- 自己尝试:    
    ```python
    n = int(input())
    if (n>=1) and (n<=1000):
        nums = list(map(int, input().split()))
        for i in range(n):
            print(nums[-i-1], end=" ")
        print()
        for j in range(0, n, 2):
            print(nums[j], end=" ")
    else:
        print('输入错误')
    ```
- 答案：  
    ```python
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(-1, -n-1, -1):
        print(nums[i], end=" ")
    print()
    for j in range(0, n, 2):
        print(nums[j], end=" ")
    ```
__倒序输出__：使用`for循环`和`range函数`倒序遍历  
__隔位输出__：`print(object, end=" ")`


## 数组
一种用于存储相同数据类型的元素的**数据结构**
- 大小固定：元素个数一旦声明，不能在运行时动态更改
-  相同数据类型：所有元素类型相同
-  连续存储：在内存中连续存储
-  下标访问：通过索引进行访问，从0开始

## 序列
python中保存一组有序数据的数据类型，所有数据都有唯一的位置（索引），主要序列类型如下：   
- 列表：[]，元素之间逗号,分隔。可变，可增删改
- 元组：()，元素之间逗号,分隔。不可变，创建后元素不可改
- 字符串："  "或' '包裹起来的字符集合，元素是字符，不可变    
序列有一些共同特性，比如通过索引访问、切片、长度计算、迭代等，即切片和for循环操作在元组和字符串中也可以进行。

## 可变值和不可变值
python中数据类型按照创建后是否可以被改变分为2类。   
- 可变：创建后可以**原地**进行修改，包括列表、字典、集合等
- 不可变：创建后不能被修改，包括整数、浮点数、字符串、元组等，当改变值的时候，会创建一个**新的对象**  
![alt text](https://img2024.cnblogs.com/blog/3696856/202509/3696856-20250909092712810-650876974.png)

## 列表
python中用列表替换了数组，与数组相比更灵活，存储一组有序的元素，但可以包含各种*8不同类型**的元素甚至是其他列表，而且列表长度可变。  
1. 创建列表：方括号[]或list(可迭代对象)，`list函数`可将其他可迭代对象转换成列表
   ```python
   a = [1, 2, 3, 4]
   # 错 a = list(1, 2, 3)
   b = list() # 生成一个空列表
   c = "hello"
   c_list = list(c) # ['h', 'e', 'l', 'l', 'o']
   ```
2. 访问列表元素：从0表示一个元素开始的索引，`a_list[0]`
   或负数索引，-1最后一个，-2倒数第二个
3. 修改列表元素：通过索引修改，`a_list[1] = 10`
4. 列表长度：使用`len()函数`获取长度即元素个数
5. 其他常见操作：
   - my_list.append(value):将新元素添加到列表末尾
   - my_list.insert(index, value):在索引index处插入元素value
   - my_list.remove(value):移除第一个值为value的元素
   - my_list.pop(index):删除并返回索引index处的元素
   - my_list.index(value):返回第一个指定值value的元素索引位置
   - my_list.sort():升序排列元素
   - my_list.reverse():反转元素顺序   
   - <font color=red>以上大部分操作为原地操作</font>

```python
my_list = [3, 1, 4, 2]

# 1. append() - 原地添加，返回None
result = my_list.append(5)
print(result)       # None
print(my_list)      # [3, 1, 4, 2, 5]

# 2. insert() - 原地插入，返回None  
result = my_list.insert(1, 99)
print(result)       # None
print(my_list)      # [3, 99, 1, 4, 2, 5]

# 3. remove() - 原地移除，返回None
result = my_list.remove(1)
print(result)       # None  
print(my_list)      # [3, 99, 4, 2, 5]

# 4. sort() - 原地排序，返回None
result = my_list.sort()
print(result)       # None
print(my_list)      # [2, 3, 4, 5, 99]

# 5. reverse() - 原地反转，返回None
result = my_list.reverse()
print(result)       # None
print(my_list)      # [99, 5, 4, 3, 2]

##############################

# pop() - 删除并返回元素，原地修改但返回被删除的值
result = my_list.pop(1)    # 删除索引1的元素
print(result)              # 1 (返回被删除的值)
print(my_list)             # [3, 4, 2] (原列表被修改)

# index() - 返回值，不修改原列表
result = my_list.index(4)  # 查找元素4的索引
print(result)              # 1 (返回索引值)
print(my_list)             # [3, 4, 2] (原列表不变)
```

## 切片
获取列表中的一小部分元素，即子列表`my_list(startIndex: endIndex: step)`   
且在索引元素前的空隔，包含start不含end，step默认为1挨着取
![alt text](https://img2024.cnblogs.com/blog/3696856/202509/3696856-20250909092713848-346441485.png)

# 摆平积木
## 题目
- 题目描述：  
  计算若干整数的和。
- 输入描述：  
  每行的第一个数N，表示本行后面有N个数。
  如果N=0时，表示输入结束，且这一行不要计算。  
- 输出描述：  
  对于每一行数据需要在相应的行输出和。
- 输入示例： 
    ```text
    4 1 2 3 4
    5 1 2 3 4 5
    0
    ```
- 输出示例： 
    ```text
    10
    15
    ```

- 自己尝试  
    ```python

    ```
- 答案1
    ```python

    ```


## 算术运算符


## 复合赋值运算符
`sum = sum + i`
