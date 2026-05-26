from PIL import Image
import torch
import torchvision
from torch import nn

## 输入的数据
### 一个点！
image_path = './dataset/dog.png'
image = Image.open(image_path)
print(image)    # mode=RGB size=413x320

transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize((32, 32)),
    torchvision.transforms.ToTensor()
])
image = transform(image)
print(image.shape)    # [3, 32, 32]
image = torch.reshape(image, (1, 3, 32, 32))


## 需要先把类导入
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
    


## 因为保存的是模型结构和参数，所以加载的时候直接加载模型就行了
model = torch.load("p27_du_0.pth")
# 因为这两个文件在一个层级，不需要加路径
# print(model)


## 下载GPU版模型,需要指定map_location参数，否则会报错
model_gpu = torch.load("p30_du_9.pth", map_location=torch.device("cpu"))

## 进入测试模式
model.eval()
with torch.no_grad():
    # output = model(image)
    output = model_gpu(image)
print(output)

