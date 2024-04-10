import xml.etree.ElementTree as ET

# 解析XML文件
tree = ET.parse('id==1.xml')
root = tree.getroot()

# 遍历每个<fruit>标签
for Aobject in root.findall('object'):
    bndbox = Aobject.find('bndbox')
    xmin = bndbox.find('xmin').text
    ymin = bndbox.find('ymin').text
    xmax = bndbox.find('xmax').text
    ymax = bndbox.find('ymax').text

    # color = Aobject.find('color').text
    # print(f"Name: {name}, Color: {color}")
    print(xmin)