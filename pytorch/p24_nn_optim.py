from torch import nn
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear
from torch import torch
from torch.utils.tensorboard import SummaryWriter
import torchvision

dataset = torchvision.datasets.CIFAR10(root="./dataset", train=False, transform=torchvision.transforms.ToTensor(), download=False)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=64)


class DU(nn.Module):
    def __init__(self):
        super(DU, self).__init__()
        self.model1 = nn.Sequential(
            Conv2d(3, 32, 5, stride=1, padding=2),
            MaxPool2d(kernel_size=2, stride=2),
            Conv2d(32, 32, 5, stride=1, padding=2),
            MaxPool2d(kernel_size=2, stride=2),
            Conv2d(32, 64, 5, stride=1, padding=2),
            MaxPool2d(kernel_size=2, stride=2),
            Flatten(),
            Linear(64 * 4 * 4, 64),
            Linear(64, 10)
        )


    def forward(self, x):
        x = self.model1(x)
        return x


loss = nn.CrossEntropyLoss()


du = DU()
optim = torch.optim.SGD(params=du.parameters(), lr=0.01)
for epoch in range(10):
    running_loss = 0.0
    for data in dataloader:
        imgs, targets = data
        outputs = du(imgs)
        result_loss = loss(outputs, targets)
        optim.zero_grad()
        result_loss.backward()
        optim.step()
        running_loss += result_loss.item()
    print(running_loss)