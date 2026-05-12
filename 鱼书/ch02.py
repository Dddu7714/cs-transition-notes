# 定义接收参数x1和x2的AND函数 与门
def AND(x1, x2):
    # 初始化参数
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1+x2*w2
    if tmp > theta:
        return 1
    else:
        return 0

AND(0, 0)

## 导入权重和偏置,计算2.2式
import numpy as np
x = np.array([0,1])
w = np.array([0.5, 0.5])
b = -0.7
print(w*x)
# [0.  0.5]
print(np.sum(w*x))
# 0.5
print(np.sum(w*x)+b)
# -0.19999999999999996

## 与门
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
       return 0
    else:
       return 1
    
## 与非门
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # 仅权重和偏置与AND不同！
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # 仅权重和偏置与AND不同！
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


## 异或门的实现
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

XOR(0, 0)
XOR(1, 1)
XOR(1, 0)