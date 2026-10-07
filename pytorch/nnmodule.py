from torch import nn
import torch


class DU(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        output = input + 1
        return output
    
du = DU()
x = torch.tensor(1.0)
y = du(x)
print(y)

