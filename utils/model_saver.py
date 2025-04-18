import os
from datetime import datetime


class ModelSaver:
    def __init__(self, base_dir='experiments'):
        """
        初始化 ModelSaver 類

        :param base_dir: 基礎目錄，默認為 "experiments"
        """
        self.base_dir = base_dir

    def save_model(self, trainer):
        """
        保存模型，目錄名稱為當前日期，檔名從 model_1 開始依序排列

        :param trainer: FCNNTrainer 類的實例
        """
        # 獲取當前日期
        current_date = datetime.now().strftime("%Y_%m_%d")
        # 創建目錄路徑
        dir_path = os.path.join(self.base_dir, f"run_{current_date}")
        os.makedirs(dir_path, exist_ok=True)

        # 自動生成模型檔名
        model_index = 1
        while True:
            model_path = os.path.join(dir_path, f"model_{model_index}.pt")
            if not os.path.exists(model_path):
                break
            model_index += 1

        # 保存模型
        trainer.save_model(model_path)
        print(f"模型已保存到: {model_path}")
