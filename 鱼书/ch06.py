##### 第5章2层网络的实现
# region
##### 5.7.2 2层神经网络的实现
import sys, os
sys.path.append(os.pardir)  
import numpy as np
from common.layers import *
from common.gradient import numerical_gradient
from collections import OrderedDict

class TwoLayerNet:
# 1 初始化网络参数和层
    def __init__(self, input_size, hidden_size, output_size, weight_init_std = 0.01):
        # 初始化权重和偏置参数
        self.params = {}
        # 第1层权重：输入层→隐藏层（形状：输入特征数×隐藏层神经元数）
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        # 第1层偏置：隐藏层神经元数（初始化为0）
        self.params['b1'] = np.zeros(hidden_size)
        # 第2层权重：隐藏层→输出层（形状：隐藏层神经元数×输出类别数）
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size) 
        # 第2层偏置：输出类别数（初始化为0）
        self.params['b2'] = np.zeros(output_size)

        # 按顺序定义网络层（OrderedDict保证层的执行顺序）
        self.layers = OrderedDict()
        # 第1个Affine层（线性变换：W1×x + b1）
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        # ReLU激活函数层（引入非线性）
        self.layers['Relu1'] = Relu()
        # 第2个Affine层（线性变换：W2×x + b2）
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])

        # 最后一层：Softmax+交叉熵损失（输出概率并计算损失）
        self.lastLayer = SoftmaxWithLoss()

# 2 前向传播预测        
    def predict(self, x):
        for layer in self.layers.values():  # 按顺序执行各层的前向传播
            x = layer.forward(x)  # 输入x经过每层后更新为输出
        return x  # 返回最终输出（未经过Softmax的原始分数）

# 3 计算损失   
#SoftmaxWithLoss 层的 forward 方法中，cross_entropy_error 函数默认会对批量样本的损失进行平均化处理，所以此处得到的损失已经和批次大小无关了     
    def loss(self, x, t):
        y = self.predict(x)  # 前向传播得到预测值（原始分数）
        return self.lastLayer.forward(y, t)  # 通过Softmax+损失层计算损失

    
# 4 计算识别精度    
    def accuracy(self, x, t):
        y = self.predict(x)  # 得到原始分数
        y = np.argmax(y, axis=1)  # 取分数最大的索引作为预测类别（0-9）
        if t.ndim != 1:  # 若标签是one-hot编码（如t_train是(60000,10)）
            t = np.argmax(t, axis=1)  # 转换为类别索引（0-9）
        # 计算预测正确的样本数占总样本数的比例
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

# 5 数值法计算梯度（用于验证）        
    def accuracy(self, x, t):
        y = self.predict(x)  # 得到原始分数
        y = np.argmax(y, axis=1)  # 取分数最大的索引作为预测类别（0-9）
        if t.ndim != 1:  # 若标签是one-hot编码（如t_train是(60000,10)）
            t = np.argmax(t, axis=1)  # 转换为类别索引（0-9）
        # 计算预测正确的样本数占总样本数的比例
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
        
# 6 误差反向传播法计算梯度（高效）  
    def gradient(self, x, t):
        # 前向传播：计算损失（同时保存各层的中间结果，供反向传播使用）
        self.loss(x, t)

        # 反向传播：从损失层开始传递梯度
        dout = 1  # 损失对自身的导数为1（反向传播的起点）
        dout = self.lastLayer.backward(dout)  # 损失层反向传播，得到传给Affine2的梯度

        # 反向遍历网络层（从后往前传梯度）
        layers = list(self.layers.values())
        layers.reverse()  # 反转层顺序：Affine2 → Relu1 → Affine1
        for layer in layers:
            dout = layer.backward(dout)  # 每层反向传播，更新梯度

        # 从各Affine层提取计算好的权重和偏置梯度
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W2'], grads['b2'] = self.layers['Affine2'].dW, self.layers['Affine2'].db
        return grads

##### 5.7.4 使用误差反向传播法的学习
# coding: utf-8
import sys, os
sys.path.append(os.pardir)

import numpy as np
from dataset.mnist import load_mnist
#from two_layer_net import TwoLayerNet

# 1 数据加载
# 加载MNIST数据集（归一化像素值到[0,1]，标签用one-hot编码）
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

# 2 初始化网络
network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

# 3 训练参数设置
iters_num = 10000  # 训练迭代次数
train_size = x_train.shape[0]  # 训练样本数（60000）
batch_size = 100  # 每次批量训练的样本数
learning_rate = 0.1  # 学习率（控制参数更新幅度）
# 记录训练过程的指标
train_loss_list = []  # 训练损失
train_acc_list = []   # 训练集精度
test_acc_list = []    # 测试集精度
iter_per_epoch = max(train_size / batch_size, 1)  # 每个epoch的迭代次数（60000/100=600）

# 4 训练循环
for i in range(iters_num):
    # 随机抽取批量样本（mini-batch）
    batch_mask = np.random.choice(train_size, batch_size)  
    # 从60000中选100个索引
    x_batch = x_train[batch_mask]  # 批量输入（100×784）
    t_batch = t_train[batch_mask]  # 批量标签（100×10）
    
    # 计算梯度（使用反向传播法，高效）
    grad = network.gradient(x_batch, t_batch)
    
    # 更新参数（梯度下降法）
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]  
        # 参数 = 参数 - 学习率×梯度
    
    # 记录当前批量的损失
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    
    # 每个epoch结束后，计算并记录精度
    if i % iter_per_epoch == 0:  # 每600次迭代（1个epoch）执行一次
        train_acc = network.accuracy(x_train, t_train)#训练集精度
        test_acc = network.accuracy(x_test, t_test)   #测试集精度
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print(train_acc, test_acc)  # 打印当前精度（应逐渐升高）
# endregion


##### 6.1.2 SGD
class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr
    def update(self, params, grads):
    # 参数params和grads依然是字典型变量，保存权重参数和梯度
        for key in params.keys():
            params[key] -= self.lr * grads[key]

# 如何使用上述SGD类进行神经网络参数的更新（伪代码）
network = TwoLayerNet(...)
optimizer = SGD()
# 进行最优化的方式
for i in range(10000):
    ...
    ##### 在ch04_5，补充定义为函数
    def get_mini_batch(x_train, t_train, train_size, batch_size):
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]
        return x_batch, t_batch
    
    x_batch, t_batch = get_mini_batch(...)

    grads = network.gradient(x_batch, t_batch)
    params = network.params
    optimizer.update(params, grads)
    # 通过单独实现进行最优化的类，使功能的模块化更简单
    # 原版如下：
    # # 计算梯度（使用反向传播法，高效）
    # grad = network.gradient(x_batch, t_batch)
    # # 更新参数（梯度下降法）
    # for key in ('W1', 'b1', 'W2', 'b2'):
    #     network.params[key] -= learning_rate * grad[key]  
    #     # 参数 = 参数 - 学习率×梯度
    ...

##### 6.1.3 Momentum
class Momentum:
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None
    def update(self, params, grads):
        if self.v is None:
            self.v = {} # 初始化空字典
            # items()方法返回字典的所有键值对，
            # key是参数名（如W1），val是参数的numpy数组
            for key, val in params.items():
                # 创建与val（参数数组）形状、数据类型完全相同的全0数组
                self.v[key] = np.zeros_like(val)
        
        for key in params.keys():
            self.v[key] = self.momentum*self.v - self.lr*grads[key]
            params[key] +=  self.v[key]

##### 6.1.4 AdaGrad
class AdaGrad:
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.h = None
    def update(self, params, grads):
        if self.h is None:
            self.h = {} # 初始化空字典
            # items()方法返回字典的所有键值对，
            # key是参数名（如W1），val是参数的numpy数组
            for key, val in params.items():
                # 创建与val（参数数组）形状、数据类型完全相同的全0数组
                self.h[key] = np.zeros_like(val)
        
        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
            # 加上微小值，防止self.h[key]中有0，这个微小值也可以设置为参数















