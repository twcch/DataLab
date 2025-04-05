import torch
from torch.utils.data import Dataset


class RegressionDataset(Dataset):
    def __init__(self, X, y):
        """
        初始化回歸數據集

        :param X: 特徵數據，應為可轉換為 torch.tensor 的數據結構
        :param dtype=torch.float32: float32 是訓練深度學習模型的「標準數據格式」。特徵數據的數據類型，默認為 float32，如果餵進 float64，PyTorch 會自動降精準度 → 但會損失效能
        :param y: 標籤數據，應為可轉換為 torch.tensor 的數據結構
        """
        self.X = torch.tensor(X, dtype=torch.float32)  # 將特徵數據轉換為 float32 類型的張量
        self.y = torch.tensor(y, dtype=torch.float32).view(-1, 1)  # 將標籤數據轉換為 float32 類型的張量，並調整形狀 (把 y 的 shape 重新調整成「N × 1」的 2D 張量，也就是每個標籤佔一行)

    def __len__(self):
        """
        返回數據集的大小

        :return: 數據集的樣本數量
        """
        return len(self.X)

    def __getitem__(self, idx):
        """
        根據索引返回數據集中的一個樣本

        :param idx: 樣本的索引
        :return: 特徵和標籤的元組 (X[idx], y[idx])
        """
        return self.X[idx], self.y[idx]
