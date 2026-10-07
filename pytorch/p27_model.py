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
    
# 验证输出尺寸
if __name__ == "__main__":
    du = DU()
    input = torch.randn(64, 3, 32, 32)
    output = du(input)
    print(output.shape)