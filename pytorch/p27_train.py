import torchvision
import torch
from torch import nn
from p27_model import *
from torch.utils.tensorboard import SummaryWriter

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
du = DU()

## 损失函数
loss_fn = nn.CrossEntropyLoss()

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

# dropout和batchnorm在训练和测试阶段的表现不同，训练阶段需要开启，测试阶段需要关闭
    ## 训练步骤开始
    du.train()
    for data in train_dataloader:
        imgs, targets = data
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


    ## 保存每一轮训练的模型
    torch.save(du, "p27_du_{}.pth".format(i))
    print("模型已保存")
    # 保存方式2
    # torch.save(du.state_dict(), "p27_du_{}.pth".format(i))

writer.close()
