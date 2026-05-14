from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image


# 先创建一个实例
writer = SummaryWriter("logs")
# y = 2x
for i in range(100):
    writer.add_scalar("y=2x", 2*i, i)
## 想要新画一个图，需要确保图名不同！


image_path = r"hymenoptera_data\train\ants\0013035.jpg"
# image_path = r"hymenoptera_data\train\bees\16838648_415acd9e3f.jpg"

img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)   # (512, 768, 3)
writer.add_image("test", img_array, 2, dataformats="HWC")  # dataformats参数指定输入图片的格式


writer.close()