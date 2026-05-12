import numpy as np

##### 5.4.1 乘法层的实现
class MulLar :
    def __init__(self):
        self.x = None
        self.y = None

    def foward(self, x, y):
        self.x = x
        self.y = y
        out = x * y

        return out
    
    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy
#### 乘法层实例
apple = 100
apple_num = 2
tax = 1.1
mul_apple_layer = MulLar()
mul_tax_layer = MulLar()
#foward
apple_price = mul_apple_layer.foward(apple, apple_num)
price = mul_tax_layer.foward(apple_price, tax)
print(price)
# backward
deprice = 1
dapple_price, dtax = mul_tax_layer.backward(deprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)
print(dapple, dapple_num, dtax) #2.2 110 200
##forward 就像 “记账”，把计算时用的 x 和 y 记在自己的小本本（self.x、self.y）上；backward 就像 “查账”，需要根据小本本上的记录来算梯度。如果没记账就查账，小本本是空的，自然算不了，会报错。

##### 5.4.2 加法层的实现
class AddLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y
        return out
    
    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy
#### 实现买2苹果3橘子实例
apple_num = 2
apple = 100
orange_num = 3
orange = 150
tax = 1.1
#layer
mul_apple_layer = MulLar()
mul_orange_layer = MulLar()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLar()
# forward
apple_price = mul_apple_layer.foward(apple, apple_num)
orange_price = mul_orange_layer.foward(orange, orange_num)
all_price = add_apple_orange_layer.forward(apple_price, orange_price)
price = mul_tax_layer.foward(all_price, tax)
# backward
dprice = 1
dall_price, dtax= mul_tax_layer.backward(dprice)
dapple_price, dorange_price = add_apple_orange_layer.backward(dall_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print(price)
print(dapple_num, dapple, dorange_num, dorange, dtax)

##### 5.5.1 ReLU层
# 一般假定forward()和backward()的参数是numpy数组
import numpy as np
# 1. 定义ReLU层
class ReLU:
    def __init__(self):
        self.mask = None
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx
# 2. 定义线性层（带参数，可计算参数梯度）
class Linear:
    def __init__(self, W, b):
        self.W = W  # 权重参数
        self.b = b  # 偏置参数
        self.x = None  # 保存前向输入x
        self.dW = None # 权重梯度
        self.db = None # 偏置梯度
    def forward(self, x):
        self.x = x  # 保存输入，供反向传播用
        out = np.dot(x, self.W) + self.b
        return out
    def backward(self, dout):
        # 用传入的dout（∂Loss/∂y）计算参数梯度,
        # 损失对当前层参数W和b的梯度，后续会用于参数更新
        self.dW = np.dot(self.x.T, dout)  # dW = x.T · dout
        self.db = np.sum(dout, axis=0)    # db = 求和dout（若有多个样本）
        dx = np.dot(dout, self.W.T) # 传给前一层的梯度（∂Loss/∂x）
        return dx
# 3. 初始化参数和数据
np.random.seed(42)
x = np.array([[1.0, 2.0]])  # 输入样本（1个样本，2个特征）
W = np.array([[0.1], [0.2]])# 线性层权重（2×1）
b = np.array([0.3])         # 线性层偏置（1）
learning_rate = 0.01        # 学习率
# 4. 初始化层
linear = Linear(W, b)
relu = ReLU()
# 5. 前向传播
y = linear.forward(x)  # 线性层输出：y = 1*0.1 + 2*0.2 + 0.3 = 0.8
z = relu.forward(y)    # ReLU输出：z = max(0, 0.8) = 0.8
# 6. 模拟损失（假设是回归任务，目标值为1.0）
loss = (z - 1.0)**2         # 损失：(0.8-1.0)² = 0.04
# 7. 反向传播（从损失开始推导dout）
# 第一步：损失对ReLU输出z的梯度（dout = ∂Loss/∂z = 2*(z-1.0)）
dout = 2 * (z - 1.0)        # dout = 2*(0.8-1.0) = -0.4
# 第二步：ReLU层反向，得到∂Loss/∂y
dy = relu.backward(dout)    # dy = -0.4（因为z>0，梯度不变）
# 第三步：线性层反向，计算参数梯度dW、db
dx = linear.backward(dy)    # 此时linear.dW和linear.db已被赋值
# 8. 用参数梯度更新参数（核心步骤）
linear.W -= learning_rate * linear.dW  # W = W - η*dW
linear.b -= learning_rate * linear.db  # b = b - η*db
# 打印结果
print("更新前W：", np.array([[0.1], [0.2]]))
print("更新后W：", linear.W)  # W会从[[0.1],[0.2]]变成[[0.104],[0.208]]
print("更新前b：", np.array([0.3]))
print("更新后b：", linear.b)  # b会从0.3变成0.304

##### 5.5.2 Sigmoid层
class Sigmoid:
    def __init__(self):
        self.out = None
    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out
    def backward(self, dout):
        dx = dout * self.out * (1.0 - self.out)
        return dx
        # forward方法中的局部变量out在backward方法中无法访问，而self.out 是实例变量（对象的 “记忆”），可以在整个类的方法中共享

##### 5.6.2 批版本的Affine层
# 包括一次线性变换和一次平移，将该处理实现为“Affine层”
class Affine:
    def __init__(self):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b
        return out
    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        return dx

### 5.6.3 Softmax-with-Loss层
class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None # 损失
        self.y = None # softmax的输出
        self.t = None # 监督数据形状为 (batch_size, 类别数)
    def forward(self, x, t):
        self.t = t
        self.y = softmax(x) #3.5.2
        self.loss = cross_entropy_error(self.y, self.t) #4.2.4
        return self.loss
    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size
        return dx



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










