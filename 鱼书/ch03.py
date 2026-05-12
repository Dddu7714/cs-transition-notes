import numpy as np
import matplotlib.pyplot as plt
## 阶跃函数
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0
# 但是这里的参数x只能接受实数（浮点数），不允许取numpy数组
# 考虑如下操作
import numpy as np
def step_function(x):
    return np.array(x>0, dtype=np.int_)
    # y = x >0 #得到布尔型数组
    # return y.astype(np.int) #布尔型转换为int型
## 报错原因！最新的numpy已移除.int，应使用.int_

x = np.arange(-5.0, 5.0, 0.1) # 在-5.0到5.0范围内，以0.1为单位
y = step_function(x)
print(y)
plt.plot(x, y)
plt.xlim(-6, 6)
plt.ylim(-0.1, 1.1) #指定y轴范围
plt.show()


## sigmoid函数
def sigmoid(x):
    return 1/(1+np.exp(-x))
x = np.arange(-5.0, 5.0, 0.1) # 在-5.0到5.0范围内，以0.1为单位
y = sigmoid(x)
print(y)
plt.plot(x, y)
plt.xlim(-6, 6)
plt.ylim(-0.1, 1.1) #指定y轴范围
plt.show()


## ReLU函数
def relu(x):
    return np.maximum(0, x)
x = np.arange(-5.0, 5.0, 0.1) 
y = relu(x)
print(y)
plt.plot(x, y)
plt.xlim(-6, 6)
plt.ylim(-0.1, 1.1) 
plt.show()

## softmax函数
# def softmax(a):
#     exp_a = np.exp(a)
#     sum_exp_a = np.sum(exp_a)
#     y = exp_a / sum_exp_a
#     return y
# 改进后
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a 
    return y 

## 3.4.2 各层间信号传递的实现
# region 各层间信号传递的实现
def identity_function(x):
    return x

def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    # 权重矩阵2×3，第一行为第一隐藏层3个神经元-第一个输入
    network['b1'] = np.array([0.1, 0.2, 0.3])
    # 偏置为3个第二层神经元
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    # 权重矩阵3×2，第一行为第二隐藏层2个神经元-第一隐藏层第1个神经元
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)
    return y    
# endregion

##### 手写字母识别
# region 手写数据集
## 导入数据
import numpy as np
import sys
import os
sys.path.append('F:\\blogs\\鱼书')  # 将父目录（dataset所在的目录）添加到系统路径中
'''会添加路径是，要用双斜杠\\'''
# 现在尝试导入
from dataset.mnist import load_mnist
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)
#(60000, 784)
#(60000,)
#(10000, 784)
#(10000,)

## 显示图像
import numpy as np
from PIL import Image
def img_show(img):
    # 参数img是一个NumPy数组格式的图像
    pil_img = Image.fromarray(np.uint8(img))
    # 将输入的img数组转换为无符号8位整数类型
    pil_img.show()
img = x_train[0]
label = t_train[0]
print(label)
print(img.shape)
# (784,)
img = img.reshape(28, 28)
img_show(img)
# endregion


# region 神经网络的推理处理
## neuralnet_mnist.py
def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=True, one_hot_label=False)
    return x_test, t_test
    # 因为只推理不学习，所以不需要训练集，只用测试集获得识别精度

## pkl文件见CSDN
import pickle 
def init_network():
    with open("F:\\blogs\\鱼书\\dataset\\sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return  network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y
# endregion

## 使用以上3个函数实现推理，评价识别精度
'''首先获得数据集，生成网络，然后用for语句逐一取出保存在x中的图像数据，用predict函数进行分类。以numpy数组形式输出各个标签对应的概率，取最高者作为预测标签，与正确标签比较将回答正确的概率作为识别精度'''
# region 实现推理
x, t = get_data()
import numpy as np
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network,x[i])
    p = np.argmax(y)
    # 获取概率最高的索引
    if p == t[i]:
        accuracy_cnt += 1
print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
# endregion

### 批处理 
# region 查看权重形式
x , _ = get_data()
network = init_network()
W1, W2, W3 = network['W1'], network['W2'], network['W3']
x.shape #(10000, 784)
x[0].shape #(784,)
W1.shape #(784, 50)
W2.shape #(50, 100)
W3.shape #(100, 10)
# endregion

# region 批处理代码实现
x, t = get_data()
network = init_network()

batch_size = 100 # 批数量
accuracy_cnt = 0
for i in range(0,len(x), batch_size):
    # range(start, end, step)生成start到end-1
    x_batch = x[i:i+batch_size]
    # 取出[0:100],[100:200]
    y_batch = predict(network,x_batch)
    # 维度为100×10
    p = np.argmax(y_batch, axis=1)
    # 指定在100×10的数组中，沿着第1维方向找值最大的元素的索引
    ## 矩阵第0维是列方向，第1维视行方向
    accuracy_cnt += np.sum(p == t[i:i+batch_size])
# print(y_batch.shape)    
print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
# endregion













