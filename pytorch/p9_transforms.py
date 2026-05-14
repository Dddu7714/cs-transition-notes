from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter


# 通过transforms.ToTensor()把PIL图片转换成tensor数据类型
# 1. transforms如何使用
# 2. tensor数据类型

# 绝对路径 F:\csnotes\pytorch\hymenoptera_data\train\ants\0013035.jpg
# 相对路径 hymenoptera_data\train\ants\0013035
img_path = r"hymenoptera_data\train\ants\0013035.jpg"
img = Image.open(img_path)
# print(img)
# # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=768x512 at 0x1856BF2F2E8>

writer = SummaryWriter("logs2")

# # 1. transforms如何使用
# # 先实例化一个类
tensor_trans = transforms.ToTensor()
# 再调用实例化的对象
tensor_img = tensor_trans(img)
# print(tensor_img)
# print(tensor_img.shape)
# # torch.Size([3, 512, 768])

# # 2. tensor数据类型
# # 包括了神经网络所需要的数据类型和维度
# import cv2
# cv_img = cv2.imread(img_path)

writer.add_image("Tensor_img", tensor_img)
writer.close()