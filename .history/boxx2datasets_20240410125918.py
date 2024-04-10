import os
import xml.etree.ElementTree as ET
import csv

def genTxt():
    xmlList = os.listdir('./xml')
    print(xmlList)
    for Axml in xmlList:
        with open(os.path.join('sets',Axml.split('.')[0]+'.txt'), mode='w', encoding='utf-8'):
            pass

def readXML(filename):
    # 解析XML文件
    tree = ET.parse(filename)
    root = tree.getroot()
    locations = []
    # 遍历每个<fruit>标签
    for Aobject in root.findall('object'):
        bndbox = Aobject.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        locations.append([xmin, ymin, xmax, ymax])
    return locations

if __name__ == '__main__':

    # xml = os.listdir(path = 'xmlpath')
    # locations = readXML(filename = 'id==2.xml')
    # print(len(locations))
    genTxt()
