import torch
import torchvision

## 保存和加载自己的模型时
from p26_model_save import *

# # 加载方式1
# model = torch.load('vgg16_method1.pth')
# print(model)

# 加载方式2
vgg16 = torchvision.models.vgg16(pretrained=False)
vgg16.load_state_dict(torch.load('vgg16_method2.pth'))
# model = torch.load('vgg16_method2.pth')
print(vgg16)