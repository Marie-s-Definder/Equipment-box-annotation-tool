import xml.etree.ElementTree as ET

# 解析XML文件
tree = ET.parse('id==1.xml')
root = tree.getroot()

# 遍历每个<fruit>标签
for Aobject in root.findall('object'):
    name = Aobject.find('bndbox').text
    # color = Aobject.find('color').text
    # print(f"Name: {name}, Color: {color}")
    print(name)