from models.fcnn import FCNN
from trainers.fcnn_trainer import FCNNTrainer
from datasets.regression_dataset import RegressionDataset
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from torch import optim, nn

import torch
import numpy as np

# 產生假資料 (可改成讀取真實資料)
x = np.linspace(-1, 1, 200).reshape(-1, 1)  # 生成範圍在 -1 到 1 之間的 200 個數據點，並重塑為列向量
y = x ** 2 + 0.1 * np.random.randn(*x.shape)  # 生成 y = x^2 加上隨機雜訊

# 切割數據集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 標準化
scaler_x = StandardScaler()  # 初始化特徵標準化器
scaler_y = StandardScaler()  # 初始化標籤標準化器

X_train_scaled = scaler_x.fit_transform(x_train)
X_test_scaled = scaler_x.transform(x_test)
y_train_scaled = scaler_y.fit_transform(y_train)
y_test_scaled = scaler_y.transform(y_test)

# 建立資料集
train_set = RegressionDataset(X_train_scaled, y_train_scaled)  # 使用標準化後的數據，建立回歸數據集

# 選擇設備
device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')

# 建立模型與訓練器
model = FCNN(input_dim=1, hidden_dim=32, output_dim=1)  # 初始化單隱藏層全連接神經網路 (FCNN)
model.to(device)

optimizer = optim.SGD(model.parameters(), lr=0.001)  # 使用 SGD 優化器
loss_fn = nn.MSELoss()  # 使用均方誤差損失函數
trainer = FCNNTrainer(model, optimizer, loss_fn, device=device)  # 初始化 FCNN 訓練器

# 開始訓練
trainer.fit(train_set, batch_size=16, epochs=1000)  # 訓練模型，批次大小為 16，訓練 1000 個迭代

# 7. 預測與反標準化
model.eval()
with torch.no_grad():
    train_preds = model(torch.tensor(X_train_scaled, dtype=torch.float32).to(device)).cpu().numpy()
    test_preds = model(torch.tensor(X_test_scaled, dtype=torch.float32).to(device)).cpu().numpy()

train_preds_inv = scaler_y.inverse_transform(train_preds)
test_preds_inv = scaler_y.inverse_transform(test_preds)
y_train_inv = scaler_y.inverse_transform(y_train_scaled)
y_test_inv = scaler_y.inverse_transform(y_test_scaled)

# 8. 精準度評估（使用 MSE）
train_mse = mean_squared_error(y_train_inv, train_preds_inv)
test_mse = mean_squared_error(y_test_inv, test_preds_inv)
print(f"Train MSE: {train_mse:.4f}")
print(f"Test MSE: {test_mse:.4f}")

# 儲存模型
trainer.save_model("experiments/run_2025_04_04/model.pt")  # 將訓練好的模型儲存到指定路徑
