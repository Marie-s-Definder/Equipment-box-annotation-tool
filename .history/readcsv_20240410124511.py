import csv

# 打开CSV文件
with open('One.csv', mode='r') as csvfile:
    # 创建CSV阅读器对象
    csvreader = csv.reader(csvfile)
    
    # 读取CSV文件中的每一行
    for row in csvreader:
        # 输出每一行的内容
        print(row)