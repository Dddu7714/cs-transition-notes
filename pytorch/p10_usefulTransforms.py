from PIL import Image
from torchvision import transforms 
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs3")

img = Image.open(r'hymenoptera_data\train\bees\16838648_415acd9e3f.jpg')
# print(img)

# 1.Totensor的使用
trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
writer.add_image("totensor", img_tensor)

# 2.Normalize的使用
# (自己训练时不是算一张图片的均值和标准差，而是算整个训练集的每个通道均值和标准差)
trans_norm = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]) #这里是随便设置的
img_norm = trans_norm(img_tensor)
writer.add_image("normalize", img_norm)

# 3.Resize的使用
# print(img.size)
trans_resize = transforms.Resize((512, 512))
# (512, 512)会把图片调整成正方形，可能会变形，(512)会保持比例不变，短边调整成512，长边根据比例调整
img_resize = trans_resize(img)
# print(img_resize)
img_resize_tensor = trans_totensor(img_resize)
writer.add_image("resize", img_resize_tensor, 0)

# 4. Compose的使用
trans_resize_2 = transforms.Resize(512)
# PIL-> PIL->tensor
trans_compose = transforms.Compose([trans_resize_2, trans_totensor])
# compose需要参数列表
img_resize_2 = trans_compose(img)
writer.add_image("resize", img_resize_2, 1)

# 5.RandomCrop的使用
trans_random = transforms.RandomCrop(224)
trans_compose_2 = transforms.Compose([trans_random, trans_totensor])
# 展示随机裁剪结果,对img分别随机裁剪10次，
for i in range(10):
    img_crop =  trans_compose_2(img)
    writer.add_image("randomcrop", img_crop, i)


writer.close()

