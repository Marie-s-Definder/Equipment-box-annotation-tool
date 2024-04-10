import xml.etree.ElementTree as ET

# 解析XML文件
tree = ET.parse('id==2.xml')
root = tree.getroot()

# 遍历每个<fruit>标签
for Aobject in root.findall('object'):
    bndbox = Aobject.find('bndbox')
    xmin = int(bndbox.find('xmin').text)
    ymin = int(bndbox.find('ymin').text)
    xmax = int(bndbox.find('xmax').text)
    ymax = int(bndbox.find('ymax').text)
    location = [xmin, ymin, xmax, ymax]

    print(xmin)
