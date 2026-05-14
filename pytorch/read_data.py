import torch
import PIL
import os

from torch.utils.data import Dataset
from PIL import Image

#### 如果就在pytorch目录下，可直接运行该文件
#### 如果还有上一级目录，需要先切换到脚本目录
# # 获取当前脚本文件的绝对路径
# script_path = os.path.abspath(__file__)
# print('当前脚本绝对路径:', script_path)
# # 获取脚本所在的目录
# script_dir = os.path.dirname(script_path)
# print('当前脚本所在目录:', script_dir)
# # 切换工作目录到脚本所在目录
# os.chdir(script_dir)
# print('当前工作目录:', os.getcwd())

class MyDataset(Dataset):
    # 根目录地址+标签目录地址 → 图片名称列表'1095476100_3906d8afde.jpg'
    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.path)

    # 获取所有图片的地址
    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        # 每个图片的相对路径
        img_item_path = os.path.join(self.root_dir, self.label_dir,  img_name)
        # hymenoptera_data\train\ants\1030023514_aad5c608f9.jpg
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_path)

root_dir = "hymenoptera_data\\train"
ants_label_dir="ants"
ants_dataset = MyDataset(root_dir, ants_label_dir)
# img0, label0 = ants_dataset[0]
# img0.show()
# print(label0)
bees_label_dir="bees"
bees_dataset = MyDataset(root_dir, bees_label_dir)

train_dataset = ants_dataset + bees_dataset
