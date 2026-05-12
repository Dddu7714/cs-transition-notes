import numpy as np



### 4.2 损失函数
## 均方误差
# region
def mean_squared_error(y, t):
    return 0.5*np.sum((y - t)**2)
# endregion

## 交叉熵误差
# region
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
# 加上一个微小值，防止出现log(0)时得到inf，导致后续计算无法进行
# endregion

## mini-batch学习
# region mini-batch学习
import numpy as np
import sys
sys.path.append('F:\\blogs\\鱼书')  # 将父目录（dataset所在的目录）添加到系统路径中
from dataset.mnist import load_mnist
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
print(x_train.shape) #(60000, 784)
print(t_train.shape) #(60000, 10)
# 如何从训练数据中随机抽取10笔数据
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
# 从0-59999之间随机选择10个数字，即被选数据的索引
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
# endregion

## mini-batch交叉熵误差的实现
# 独热编码版
# region 独热编码版交叉熵
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        # 通过reshape将y和t转换为二维数组（形状为[1, 特征数]），统一批量样本和单个样本的处理逻辑
    batch_size = y.shape[0]
    return - np.sum(t * np.log(y + 1e-7)) / batch_size
# endregion

# 标签形式版
# region 标签形式版交叉熵
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return - np.sum(np.log(y[np.arange(batch_size) , t] + 1e-7)) / batch_size
# y[np.arange(batch_size), t]能抽出各个数据的正确解标签对应的神经网络的输出（在这个例子中，会生成NumPy数组[y[0,2], y[1,7], y[2,0], y[3,9], y[4,4]]）
# endregion

### 数值微分
## 导数
# 不好的
# region 
def numerical_diff(f, x):
    h = 10e-50
    return (f(x+h) - f(x)) / h
# endregion
# 改进的
# region 
def numerical_diff(f, x):
    h = 1e-4 #0.0001
    return (f(x+h) - f(x-h)) / (2*h)
# endregion

### 4.4 梯度
def numerical_gradient(f, x):
    h = 1e-4 # 0.0001 避免舍入误差
    # 生成和x形状相同的数组，存储梯度
    grad = np.zeros_like(x) 
    for idx in range(x.size):
        # 暂存当前自变量的值
        tmp_val = x[idx]
        # f(x+h) 的计算
        x[idx] = tmp_val + h
        fxh1 = f(x)
        # f(x-h) 的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)
        # 中心差分计算偏导
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 还原
    return grad

### 4.4.4 学习率
## 使用python实现梯度下降法
# f是函数，init_x是初始值，lr是学习率，step_num是梯度法的重复次数
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        # 求梯度
        grad = numerical_gradient(f, x)
        x -= lr *grad
    
    return x

### 4.4.2 神经网络的梯度
## 以一个简单的神经网络为例，实现求梯度的代码
import sys, os
sys.path.append(os.pardir)
import numpy as np
from ch03 import softmax
## 定义一个类
class simpleNet:
    # 该类只有一个实例变量，即权重参数
    def __init__ (self):
        # 用高斯分布进行权重参数初始化
        self.W = np.random.randn(2, 3)
    # 用于预测的方法
    def predict(self, x):
        return np.dot(x, self.W)
    # 用于求损失函数的方法
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss 
## 1.用一下
net = simpleNet()
print(net.W)
#[[-0.97737611  0.01903064  0.80267347]
# [ 0.05686275  0.78809771 -0.14143243]]
x = np.array([0.6, 0.9])
p = net.predict(x)
print(p)
print(np.argmax(p))
t = np.array([0, 0, 1])
print(net.loss(x, t))
## 2.求梯度
# # 定义函数这没懂？？？
# def f(W):
#     return net.loss(x, t)
# # numerical直接运行不对，因为前面定义的是一维数组的函数，源代码在common/gradient.py
# dW = numerical_gradient(f, net.W)
# print(dW)
