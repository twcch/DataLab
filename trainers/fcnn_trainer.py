from torch.utils.data import DataLoader

import torch
import os


class FCNNTrainer:
    def __init__(self, model, optimizer, loss_fn, device):
        """
        初始化 FCNN 訓練器

        :param model: 要訓練的神經網路模型
        :param optimizer: 用於優化模型的優化器
        :param loss_fn: 損失函數
        :param device: 訓練設備（如 'cpu' 或 'cuda'）
        """
        self.model = model.to(device)
        self.optimizer = optimizer
        self.loss_fn = loss_fn
        self.device = device

    def fit(self, dataset, batch_size=32, epochs=100):
        """
        訓練模型

        :param dataset: 用於訓練的數據集
        :param batch_size: 每個批次的樣本數量，默認為 32
        :param epochs: 訓練的迭代次數，默認為 100
        """
        dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        self.model.train()
        for epoch in range(epochs):
            epoch_loss = 0
            for xb, yb in dataloader:
                xb, yb = xb.to(self.device), yb.to(self.device)
                pred = self.model(xb)
                loss = self.loss_fn(pred, yb)
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                epoch_loss += loss.item()
            if epoch % 10 == 0:
                print(f"Epoch {epoch}, Loss: {epoch_loss:.4f}")

    def save_model(self, path):
        """
        保存訓練好的模型

        :param path: 模型保存的路徑
        """
        os.makedirs(os.path.dirname(path), exist_ok=True)
        torch.save(self.model.state_dict(), path)
