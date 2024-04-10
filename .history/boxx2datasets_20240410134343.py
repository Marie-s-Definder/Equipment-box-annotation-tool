import os
import xml.etree.ElementTree as ET
import csv

import argparse

def genTxt():
    xmlList = os.listdir('./xml')
    # print(xmlList)
    for Axml in xmlList:
        with open(os.path.join('sets',Axml.split('.')[0]+'.txt'), mode='w', encoding='utf-8'):
            pass
    with open(os.path.join('sets','填写示例.txt'), mode='w', encoding='utf-8') as file:
        file.write('''
1,旋钮,0,0

解释：
第一项 1 表示 device_id
第二项 旋钮 表示该数据的名称
第三项 0 正常表示下限
第四项 0 正常表示上限

如果数据有单位，填上第五项
如下填写：
1,旋钮,0,0,摄氏度


注意：该标注方法只针对设备箱，如有其他待标注数据则需要额外开发，联系开发者！
                ''')

def readXML(filename):
    # 解析
    tree = ET.parse(filename)
    root = tree.getroot()
    locations = []
    for Aobject in root.findall('object'):
        bndbox = Aobject.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        locations.append([xmin, ymin, xmax, ymax])
    return locations

def genCSV():
    xmlList = os.listdir('./xml')
    
    # xmlList = [x for x in xmlList if x != '填写示例.txt']
    # print(xmlList)
    writeInCSV = []
    for Axml in xmlList:
        locations = readXML(os.path.join('xml', Axml))
        # print(os.path.join('sets',Axml.split('.')[0]+'.txt'))
        # sets\id==1.txt
        # with open('sets\id==1.txt', mode='r', encoding='utf-8') as file:
        #     # 逐行读取文件内容
        #     for line in file:
        #         # 打印每一行的内容（注意：每行末尾会有换行符）
        #         print(line, end='')
        with open(os.path.join(os.getcwd(),'sets',Axml.split('.')[0]+'.txt'), mode='r', encoding='utf-8') as file:
            # print(file.read())
            for index, line in enumerate(file):
                elements = line.strip().split(',')
                # print(len(elements) == 4)
                
                if len(elements) == 4:
                    writeInCSV.append([elements[0],elements[1],elements[2],elements[3],
                                       ','.join(map(str, locations[index])),
                                       '',
                                       'light'])
                elif len(elements) == 5:
                    writeInCSV.append([elements[0],elements[1],elements[2],elements[3],
                                       ','.join(map(str, locations[index])),
                                       elements[4],
                                       'light'])
                else:
                    raise ValueError(f'{Axml.split('.')[0]}.txt文件有误，检查是否是英文逗号，行数是否为7行')

    with open('output.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        # print(writeInCSV)
        for row in writeInCSV:
            
            csvwriter.writerow(row)

if __name__ == '__main__':

    # 创建解析器对象
    parser = argparse.ArgumentParser(description='第一步先生成txt,第二步再生成csv,因此第一次参数为txt,第二次参数为csv')

    # 添加命令行参数
    parser.add_argument('type')

    args = parser.parse_args()

    # 输出打招呼的内容
    if args.type == 'txt':
        genTxt()
    elif args.type == 'csv':
        genCSV()
    else:
        raise ValueError('第一步先生成txt,第二步再生成csv,因此第一次参数为txt,第二次参数为csv')
