import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# --- 1. 讀取資料 ---
# 將 'sales_data.csv' 讀取到 DataFrame 中
df = pd.read_csv('sales_data.csv')

# --- 2. 資料預處理 ---
# 檢查要用哪個欄位作為分組的 key
# 計算 '投保的編號' 和 '商品名稱' 的唯一值數量
if len(df['投保的編號'].unique()) <= len(df['商品名稱'].unique()):
    # 如果 '投保的編號' 的唯一值數量較少，則表示一個 '投保的編號' 對應多個 '商品名稱'
    # 因此以 '投保的編號' 作為分組 key
    grouping_key = '投保的編號'
else:
    # 否則以 '商品名稱' 作為分組 key
    grouping_key = '商品名稱'

# 如果 grouping_key 是 '商品名稱'，則需要將 '商品名稱' 轉換為數值 ID
if grouping_key == '商品名稱':
    # 建立一個字典，將每個唯一的 '商品名稱' 映射到一個數值 ID
    product_mapping = {product_name: idx for idx, product_name in enumerate(df['商品名稱'].unique())}
    # 使用這個字典，將 DataFrame 中的 '商品名稱' 轉換為 'product_id'
    df['product_id'] = df['商品名稱'].map(product_mapping)

# 根據 grouping_key 分組，並將 'product_id' 聚合成一個列表
grouped_df = df.groupby(grouping_key)['product_id'].agg(list).reset_index()

# 過濾掉 'product_id' 列表長度小於 2 的分組，因為 Apriori 算法需要至少 2 個商品才能找到關聯規則
transactions = grouped_df[grouped_df['product_id'].apply(lambda x: len(x) >= 2)]['product_id'].astype(str)

# 將 transactions 中的每個 'product_id' 列表轉換為字串列表
transactions = transactions.apply(lambda x: x.strip('').replace(' ', '').split(','))

# --- 3. Apriori 算法 ---
# 使用 TransactionEncoder 將 transactions 轉換為 one-hot 編碼
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# 使用 apriori 算法找到頻繁的商品組合，設定最小支持度為 5%
frequent_itemsets = apriori(df_encoded, min_support=0.05, use_colnames=True)

# 使用 association_rules 函數從頻繁的商品組合中產生關聯規則，設定最小置信度為 50%
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# 根據 lift 值對規則進行排序，並顯示前 5 個規則
print(rules.sort_values('lift', ascending=False).head(5).to_markdown(index=False, numalign="left", stralign="left"))