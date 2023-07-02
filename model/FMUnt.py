import torch
import torch.nn.functional as F
from torch import nn

from model.SKAttention import SKAttention


class TwoConv_3(nn.Module):
    """(convolution => [BN] => ReLU) * 2"""
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.double_conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1,stride=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1,stride=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.double_conv(x)
class TwoConv_5(nn.Module):
    """(convolution => [BN] => ReLU) * 2"""
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.double_conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=5, padding=2,stride=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=5, padding=2,stride=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.double_conv(x)
class TwoConv_7(nn.Module):
    """(convolution => [BN] => ReLU) * 2"""
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.double_conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=7, padding=3,stride=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=7, padding=3,stride=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.double_conv(x)
class TwoConv(nn.Module):
    """(convolution => [BN] => ReLU) * 2"""
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.double_conv = nn.Sequential(
            nn.Conv2d(in_channels,in_channels//2, kernel_size=3, padding=1),
            nn.BatchNorm2d(in_channels//2),
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels//2, out_channels, kernel_size=3, padding=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.double_conv(x)
class MCM1(nn.Module):
        def __init__(self, in_channels, out_channels):
            super(MCM1, self).__init__()
            self.Branch1x1 = nn.Conv2d(in_channels, out_channels // 4, kernel_size=1)

            self.Branch3x3_1 = nn.Conv2d(in_channels, out_channels // 4, kernel_size=1)
            self.Branch3x3 = nn.Conv2d(out_channels // 4, out_channels // 4, kernel_size=3, padding=1)

            self.Branch5x5_1 = nn.Conv2d(in_channels, out_channels // 4, kernel_size=1)
            self.Branch5x5 = nn.Conv2d(out_channels // 4, out_channels // 4, kernel_size=5, padding=2)

            self.Branchmax1x1 = nn.Conv2d(in_channels, out_channels // 4, kernel_size=1)

            self.bn = nn.BatchNorm2d(out_channels, eps=0.001)

        def forward(self, x):
            branch1x1 = self.Branch1x1(x)

            branch2_1 = self.Branch3x3_1(x)
            branch2_2 = self.Branch3x3(branch2_1)

            branch3_1 = self.Branch5x5_1(x)
            branch3_2 = self.Branch5x5(branch3_1)

            branchpool4_1 = F.max_pool2d(x, kernel_size=3, stride=1, padding=1)
            branchpool4_2 = self.Branchmax1x1(branchpool4_1)

            outputs = [branch1x1, branch2_2, branch3_2, branchpool4_2]
            x = torch.cat(outputs, 1)
            x = self.bn(x)
            return F.relu(x, inplace=True)
class FMUnet(nn.Module):
    def __init__(self, n_channels, n_classes, bilinear=True):
        super(FMUnet, self).__init__()
        self.con3=TwoConv_3(6,64)
        self.con5=TwoConv_5(6,64)
        self.con7=TwoConv_7(6,64)

        self.mcm1=MCM1(64,128)
        self.sk=SKAttention(channel=384,reduction=8)
        self.two=TwoConv(384,256)
        self.two1=TwoConv(256,64)
        self.two2=TwoConv(64,2)
        self.two3=TwoConv(64,1)
        # self.two1=TwoConv(64,1)

    def forward(self, x1, x2):
        x = torch.cat((x1, x2), 1)
        x1=self.con3(x)
        x2=self.con5(x)
        x3=self.con7(x)

        x1=self.mcm1(x1)
        x2=self.mcm1(x2)
        x3=self.mcm1(x3)
        outs=[x1,x2,x3]
        x = torch.cat(outs, 1)
        x=self.sk(x)
        x=self.two(x)
        x=self.two1(x)
        x=self.two2(x)
        # x=self.two3(x)


        return x


if __name__ == '__main__':
    input1 = torch.randn(1, 3, 28,28)
    input2 = torch.randn(1, 3, 28,28)
    net=FMUnet(1,1)
    out=net(input1,input2)
    print(out.shape)
