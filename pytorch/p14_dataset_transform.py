import torchvision
from torch.utils.tensorboard import SummaryWriter

dataset_transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])

train_set = torchvision.datasets.CIFAR10(root="./dataset", train=True, download=True, transform=dataset_transform)
test_set = torchvision.datasets.CIFAR10(root="./dataset", train=False, download=True, transform=dataset_transform)

# img, target = train_set[0]
# print(img)
# print(target)
# print(train_set.classes[target])
# img.show()

print(train_set[0]) # 输出为tensor数据类型

writer = SummaryWriter("p14")
for i in range(10):
    img, target = train_set[i]
    writer.add_image("train_set", img, i)

writer.close() 



