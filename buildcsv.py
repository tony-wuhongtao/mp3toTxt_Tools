import os
import csv

# 设置文件夹路径
folder_path = input("请输入文件夹路径: ")

# 创建一个新的CSV文件
output_file = os.path.join(folder_path, 'output.csv')

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # 写入表头
    writer.writerow(['num', 'name', 'grade', 'sub', 'teacher', 'school', 'script'])

    # 遍历文件夹中的文件
    num = 1
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            
            # 从文件名中提取信息
            parts = file_name.split('_')
            name = parts[4][1:-1]  # 去掉书名号
            grade = parts[3][0:3]
            sub = parts[3][3:5]
            teacher = parts[5]
            school = parts[6]
            
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                script = file.read()
            
            # 写入CSV文件
            writer.writerow([num, name, grade, sub, teacher, school, script])
            
            num += 1

print(f"数据已成功写入 {output_file}")