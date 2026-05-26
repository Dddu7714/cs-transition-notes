import torch
import torchvision
from torch.utils.data import DataLoader
from torch import nn
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10(root="./dataset", train=False, transform=torchvision.transforms.ToTensor(), download=True)

dataloader = DataLoader(dataset, batch_size=64)

class DU(nn.Module):
    ## 初始化函数，定义卷积层
    def __init__(self):
        ## super()函数是用来调用父类（在这里是nn.Module）的初始化方法的。它确保了父类的初始化代码被正确执行，从而使得子类能够正确地继承和使用父类的功能。
        super(DU, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)
    ## forward函数定义了前向传播的过程，即输入数据如何通过网络层进行计算并得到输出结果。在这个函数中，我们将输入数据x传递给卷积层conv1，并返回卷积层的输出结果。
    def forward(self, x):
        x = self.conv1(x)
        return x

du = DU()
print(du)
# DU((conv1): Conv2d(3, 6, kernel_size=(3, 3), stride=(1, 1)))

writer = SummaryWriter("logs")
step = 0
for data in dataloader:
    imgs, targets = data # 原尺寸64*3*32*32
    output = du(imgs)
    print(output.shape)  # torch.Size([64, 6, 30, 30])
    writer.add_images("input", imgs, step)
    ## 由于tensorboard无法输出6通道照片，改变batchsize，使其成为3通道
    output = torch.reshape(output, (-1, 3, 30, 30)) #-1表示自动计算维度，3是通道数，30*30是卷积后的尺寸
    writer.add_images("output", output, step)
    step = step+1

