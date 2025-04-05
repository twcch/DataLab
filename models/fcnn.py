import torch.nn as nn


class FCNN(nn.Module):
    def __init__(self, input_dim, hidden_dim=64, output_dim=1):
        """
        初始化雙隱藏層全連接神經網路 (FCNN)

        :param input_dim: 輸入層的維度
        :param hidden_dim: 隱藏層的神經元數量，默認為 64
        :param output_dim: 輸出層的維度，默認為 1
        """
        super(FCNN, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),  # 輸入層
            nn.ReLU(),  # 隱藏層的 ReLU 激活函數
            nn.Linear(hidden_dim, hidden_dim),  # 隱藏層
            nn.ReLU(),  # 隱藏層的 ReLU 激活函數
            nn.Linear(hidden_dim, output_dim)  # 輸出層
        )

    def forward(self, x):
        """
        前向傳播函數

        :param x: 輸入張量
        :return: 預測張量
        """
        return self.net(x)  # 等價 self.net.__call__(x)
