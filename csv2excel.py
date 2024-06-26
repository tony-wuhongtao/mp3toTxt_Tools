import pandas as pd

# 输入文件路径
csv_file = input("请输入CSV文件路径: ")
excel_file = csv_file.rsplit('.', 1)[0] + '.xlsx'

# 读取CSV文件
df = pd.read_csv(csv_file, encoding='utf-8')  # 如果是其他编码，替换 'utf-8'

# 将数据写入Excel文件
df.to_excel(excel_file, index=False)

print(f"已将CSV文件转换为Excel文件: {excel_file}")