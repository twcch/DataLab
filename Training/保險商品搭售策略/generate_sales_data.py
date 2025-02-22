import random
import string
import csv
from datetime import datetime, timedelta

def random_product_code(length=5):
    """商品代號: 產生 length 碼英文 (A-Z)"""
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def random_member_id(length=10):
    """會員ID: 產生 length 碼英文+數字"""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

def random_order_id():
    """投保的編號: 前綴 ORD + 6碼亂數英文數字"""
    chars = string.ascii_uppercase + string.digits
    return 'ORD' + ''.join(random.choices(chars, k=6))

def random_insurance_name():
    """隨機生成保險商品名稱: 簡單地把前後綴組合在一起"""
    prefix_list = ["安心", "幸福", "健康", "無憂", "滿福", "希望", "長青", "永保", "安康", "祥和"]
    suffix_list = ["人生", "保險", "保障", "福祉", "無憂"]
    return random.choice(prefix_list) + random.choice(suffix_list)

def random_datetime_within_10_years():
    """在最近 10 年內隨機產生日期和時間"""
    end = datetime.now()
    start = end - timedelta(days=365*10)  # 往前 10 年
    random_date = start + (end - start) * random.random()
    return random_date.strftime("%Y-%m-%d %H:%M:%S")

def get_channel_and_pushsource(category):
    """
    根據商品分類決定可用通路，再由通路決定推銷來源
    傷害保險: [保險公司, 銀行, 保經代, 網路投保]
    其他(人壽, 健康, 年金): [保險公司, 銀行, 保經代]
    推銷來源:
        保險公司 → (官網 or 業務員)
        銀行 → (銀行理專)
        保經代 → (業務員)
        網路投保 → (官網)
    """
    if category == "傷害保險":
        possible_channels = ["保險公司", "銀行", "保經代", "網路投保"]
    else:
        possible_channels = ["保險公司", "銀行", "保經代"]

    channel = random.choice(possible_channels)

    if channel == "保險公司":
        push_source = random.choice(["官網", "業務員"])
    elif channel == "銀行":
        push_source = "銀行理專"
    elif channel == "保經代":
        push_source = "業務員"
    else:  # 網路投保
        push_source = "官網"

    return channel, push_source

def build_products(num_products=2000):
    """
    預先生成最多 2000 筆唯一商品資訊(商品代號、商品名稱、分類、通路、推銷來源、單價)。
    """
    categories = ["人壽保險", "健康保險", "傷害保險", "年金保險"]
    product_list = []
    used_codes = set()

    while len(product_list) < num_products:
        code = random_product_code()
        if code in used_codes:
            continue
        used_codes.add(code)

        name = random_insurance_name()
        category = random.choice(categories)
        channel, push_source = get_channel_and_pushsource(category)
        price = random.randint(100, 1000000)

        product_list.append({
            "code": code,
            "name": name,
            "category": category,
            "channel": channel,
            "push_source": push_source,
            "price": price
        })

    return product_list

def generate_sales_data(num_records=20000, output_file="sales_data.csv"):
    """
    生成銷售資料:
      - 共約 num_records 筆 (預設 20000)
      - 每個會員模擬多個購買時段，每個時段同一投保時間下購買 1~10 個商品
      - 每筆訂單隨機購買 1~100 個單位, 總保費 = 商品單價 x 購買數量
      - 成本 = 商品單價 x (隨機成本百分比，介於50%~80%)
      - 若投保時間相同，則投保的編號一致
      - 寫出 CSV 檔
    """
    products = build_products(num_products=2000)
    time_to_order_id = {}  # 紀錄已出現的投保時間對應的投保編號
    total_records = 0

    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "商品代號",
            "商品名稱",
            "通路",
            "商品分類",
            "商品單價",
            "推銷來源",
            "會員ID",
            "會員性別",
            "會員投保年齡",
            "投保時間",
            "投保的編號",
            "總保費",
            "成本"
        ])

        num_members = 3000
        for _ in range(num_members):
            member_id = random_member_id()
            member_gender = random.choice(["男", "女"])
            member_age = random.randint(1, 65)

            # 每個會員模擬1~10個購買時段
            session_count = random.randint(1, 10)
            for _ in range(session_count):
                # 每個購買時段產生一個投保時間及對應的訂單編號
                insured_time = random_datetime_within_10_years()
                if insured_time in time_to_order_id:
                    order_id = time_to_order_id[insured_time]
                else:
                    order_id = random_order_id()
                    time_to_order_id[insured_time] = order_id

                # 在同一時段中，該會員購買 1~10 個商品
                products_in_session = random.randint(1, 10)
                for _ in range(products_in_session):
                    if total_records >= num_records:
                        break

                    product = random.choice(products)
                    quantity = random.randint(1, 100)
                    total_premium = product["price"] * quantity

                    cost_percent = random.randint(50, 80)
                    cost = int(product["price"] * cost_percent / 100)

                    writer.writerow([
                        product["code"],
                        product["name"],
                        product["channel"],
                        product["category"],
                        product["price"],
                        product["push_source"],
                        member_id,
                        member_gender,
                        member_age,
                        insured_time,
                        order_id,
                        total_premium,
                        cost
                    ])
                    total_records += 1

                if total_records >= num_records:
                    break
            if total_records >= num_records:
                break

    print(f"已生成 {total_records} 筆測試資料至 {output_file} 檔案中。")

if __name__ == "__main__":
    generate_sales_data(num_records=900000999990000, output_file="sales_data.csv")