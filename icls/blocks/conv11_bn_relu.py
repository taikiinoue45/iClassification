import torch.nn as nn
from torch import Tensor
from torch.nn import Module


class Conv11BnReLU(Module):
    def __init__(
        self,
        # nn.Conv2d
        in_channels: int,
        out_channels: int,
        kernel_size: int = 1,
        stride: int = 1,
        padding: int = 0,
        dilation: int = 1,
        groups: int = 1,
        bias: bool = False,
        padding_mode: str = "zeros",
        # nn.BatchNorm2d
        eps: float = 1e-05,
        momentum: float = 0.1,
        affine: bool = True,
        track_running_stats: bool = True,
        # nn.ReLU
        inplace: bool = True,
    ):

        super(Conv11BnReLU, self).__init__()

        self.conv11_bn_relu = nn.Sequential(
            nn.Conv2d(
                in_channels=in_channels,
                out_channels=out_channels,
                kernel_size=kernel_size,
                stride=stride,
                padding=padding,
                dilation=dilation,
                groups=groups,
                bias=bias,
                padding_mode=padding_mode,
            ),
            nn.BatchNorm2d(
                num_features=out_channels,
                eps=eps,
                momentum=momentum,
                affine=affine,
                track_running_stats=track_running_stats,
            ),
            nn.ReLU(inplace=inplace),
        )

    def forward(self, x: Tensor) -> Tensor:

        return self.conv11_bn_relu(x)
