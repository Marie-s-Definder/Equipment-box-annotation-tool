首先文件结构如下

|--sets--|
|        |空文件夹
|        
|--xml --|
|        |图片保存的xml文件都保存在该文件夹
|
|--boxx2datasets.py

即：
sets为空文件夹，
xml为存放xml的文件夹，所有拉的框都在这里
图片随便存，但是不要放到sets或者xml文件夹当中


第一步：画框顺序：必须固定，对于每个设备箱，第一排灯从左往右123，第二排灯从左往右456，旋钮7，必须按照这个顺序，标签不用打，随便写一个标签就行了，代码不看标签的, 标注工具使用labelimg
第二步：当已经拉好框，xml文件夹中有文件的时候执行 `python boxx2datasets.py txt`，set 中会生成一个个对应xml文件的txt文件
第三步：按照填写示例填写txt文件

#############################################
    填写示例：
        1,旋钮,0,0

        解释：
        第一项 1 表示 device_id
        第二项 旋钮 表示该数据的名称
        第三项 0 正常表示下限
        第四项 0 正常表示上限

        如果数据有单位，填上第五项
        如下填写：
        1,旋钮,0,0,摄氏度


        注意：1.该标注方法只针对设备箱，如有其他待标注数据则需要额外开发
            2.每个txt文件中必须为7行，
            3.从上往下顺序必须为画框的顺序
#############################################

第四步：执行 `python boxx2datasets.py csv`
第五步：boxx2datasets.py同一级目录下会生成一个output.csv文件，把这个文件直接导入数据库，`注意！`第一列的id不要导入。
