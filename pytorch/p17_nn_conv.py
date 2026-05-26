import torch
import torch.nn.functional as F

input = torch.tensor([[1, 2, 0, 3, 1],
                      [0, 1, 2, 3, 1],
                      [1, 2, 0, 0, 1],  
                      [0, 1, 2, 3, 1],
                      [1, 2, 0, 3, 1]])

kernel = torch.tensor([[1, 2, 1],
                        [0, 1, 0],
                        [2, 1, 0]])

# print(input.shape)  # torch.Size([5, 5])
# print(kernel.shape)  # torch.Size([3, 3])

# 卷积操作要求输入和卷积核都是4维的张量，分别表示(batch_size, channels, height, width)。
input = torch.reshape(input, (1, 1, 5, 5))
kernel = torch.reshape(kernel, (1, 1, 3, 3))

# print(input.shape)
# print(kernel.shape)

output1 = F.conv2d(input, kernel, stride=1, padding=0)
print(output1)

output3 = F.conv2d(input, kernel, stride=1, padding=1)
print(output3)