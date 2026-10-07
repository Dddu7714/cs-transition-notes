import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


test_data = torchvision.datasets.CIFAR10(root="./dataset", train=False, transform = torchvision.transforms.ToTensor())

# test_loader = DataLoader(dataset = test_data, batch_size=4, shuffle=True, num_workers=0, drop_last=False)

# # 测试集中第一张图片
# img, target = test_data[0]
# print(img)
# print(img.shape)    # torch.Size([3, 32, 32])
# print(target)

test_loader = DataLoader(dataset = test_data, batch_size=64, shuffle=True, num_workers=0, drop_last=False)

writer = SummaryWriter("dataloader")
for epoch in range(2):
    step = 0
    for data in test_loader:
        imgs, targets = data
        writer.add_images("Epoch:{}".format(epoch), imgs, step)   
        step += 1

writer.close()