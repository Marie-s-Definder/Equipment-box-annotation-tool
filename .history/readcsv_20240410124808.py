# import csv

# # 打开CSV文件
# with open('2Save.csv', mode='r', encoding='utf-8') as csvfile:
#     # 创建CSV阅读器对象
#     csvreader = csv.reader(csvfile)
    
#     # 读取CSV文件中的每一行
#     for row in csvreader:
#         # 输出每一行的内容
#         print(row)
import csv

# 要保存的数据
data = [
    ['Name', 'Age', 'Country'],
    ['Alice', '25', 'USA'],
    ['Bob', '30', 'Canada'],
    ['Charlie', '22', 'UK'],
    ['David', '28', 'Australia']
]

# 将数据写入CSV文件
with open('output.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    for row in data:
        csvwriter.writerow(row)

print("CSV文件保存成功")