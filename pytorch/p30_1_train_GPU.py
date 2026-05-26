import torchvision
import torch
from torch import nn
# from p27_model import *
from torch.utils.tensorboard import SummaryWriter
import time




## 准备数据集
train_data = torchvision.datasets.CIFAR10(root="./dataset", train=True, transform=torchvision.transforms.ToTensor(), download=True)

test_data = torchvision.datasets.CIFAR10(root="./dataset", train=False, transform=torchvision.transforms.ToTensor(), download=True)

train_data_size = len(train_data)
test_data_size = len(test_data)
print("训练数据集的长度为：{}".format(train_data_size))
print("测试数据集的长度为：{}".format(test_data_size))

## 利用dataloader加载数据集
train_dataloader = torch.utils.data.DataLoader(train_data, batch_size=64)
test_dataloader = torch.utils.data.DataLoader(test_data, batch_size=64)

## 10分类搭建神经网络
import torch
import torchvision

## 10分类搭建神经网络
class DU(torch.nn.Module):
    def __init__(self):
        super(DU, self).__init__()
        self.model = torch.nn.Sequential(
            torch.nn.Conv2d(3, 32, 5, 1, 2),
            torch.nn.MaxPool2d(2),
            torch.nn.Conv2d(32, 32, 5, 1, 2),
            torch.nn.MaxPool2d(2),
            torch.nn.Conv2d(32, 64, 5, 1, 2),
            torch.nn.MaxPool2d(2),
            torch.nn.Flatten(),
            torch.nn.Linear(64 * 4 * 4, 64),
            torch.nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.model(x)
        return x
    
du = DU()
du = du.cuda()  # 将模型移动到GPU上进行计算

## 损失函数
loss_fn = nn.CrossEntropyLoss()
loss_fn = loss_fn.cuda()  # 将损失函数移动到GPU上进行计算

## 优化器
# 1e-2 = 10^(-2) = 0.01
learning_rate = 1e-2
optimizer = torch.optim.SGD(du.parameters(), lr=learning_rate)


## 设置训练参数
# 记录训练的次数
total_train_step = 0
# 记录测试的次数
total_test_step = 0
# 训练的轮数
epoch = 10



## 添加tensorboard
writer = SummaryWriter("./logs")

for i in range(epoch):
    print("-------第 {} 轮训练开始-------".format(i + 1))
    start_time = time.time()  # 记录训练开始时间

# dropout和batchnorm在训练和测试阶段的表现不同，训练阶段需要开启，测试阶段需要关闭
    ## 训练步骤开始
    du.train()
    for data in train_dataloader:
        imgs, targets = data
        imgs = imgs.cuda()
        targets = targets.cuda()
        outputs = du(imgs)
        loss = loss_fn(outputs, targets)

        # 优化器优化模型
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_train_step += 1
        # print("训练次数：{}，Loss：{}".format(total_train_step, loss.item()))

        if total_train_step % 100 == 0:
            print("训练次数：{}，Loss：{}".format(total_train_step, loss.item()))
            # scalar(标量) -- 记录训练的次数和loss值
            writer.add_scalar("train_loss", loss.item(), total_train_step)

    ## 测试步骤开始
    du.eval()
    total_test_loss = 0
    total_accuracy = 0

    # torch.no_grad()表示在该代码块中不需要计算梯度，节省内存和计算资源
    with torch.no_grad():
        for data in test_dataloader:
            imgs, targets = data
            imgs = imgs.cuda()
            targets = targets.cuda()
            outputs = du(imgs)
            loss = loss_fn(outputs, targets)
            total_test_loss += loss.item()
            # argmax(1)表示在第1维度上取最大值的索引，即预测的类别标签
            accuracy = (outputs.argmax(1) == targets).sum()
            total_accuracy += accuracy

    print("整体测试集上的Loss：{}".format(total_test_loss))
    print("整体测试集上的正确率：{}".format(total_accuracy / test_data_size))
    total_test_step += 1
    writer.add_scalar("test_loss", total_test_loss, total_test_step)
    writer.add_scalar("test_accuracy", total_accuracy / test_data_size, total_test_step)
    end_time = time.time()  # 记录训练结束时间
    print("第 {} 轮训练的时间为：{}秒".format(i + 1, end_time - start_time))


    ## 保存每一轮训练的模型
    torch.save(du, "du_{}.pth".format(i))
    print("模型已保存")
    # 保存方式2
    # torch.save(du.state_dict(), "du_{}.pth".format(i))

writer.close()
