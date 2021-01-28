import json
import pandas as pd
import numpy as np
import csv

def readjsonfile(filename):
    a = []

    f = open(filename, "r")  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法

    while line:
        s = json.loads(line)  # 把json变成python字典
        a.append(s)
        line = f.readline()

    f.close()
    return a


def readtxtfile(filename):
    a = []
    f = open(filename, "r")  # 返回一个文件对象
    for line in f.readlines():
        x = []
        sub_str = line.split(',')
        for s in sub_str:
            if s != '\n':
                x.append(s)
        a.append(x)
    f.close()
    return a


def writejsonfile(filename, list):
    # list=listToJson(list)
    file1 = open(filename, 'w')
    # 循环写入
    for l in list:
        for s in l:
            json.dump(s, file1)
            file1.write('\n')

    file1.close()


# list 转成Json格式数据
def listToJson(lst):
    import json
    import numpy as np
    keys = [str(x) for x in np.arange(len(lst))]
    list_json = dict(zip(keys, lst))
    str_json = json.dumps(list_json, indent=2, ensure_ascii=False)  # json转为string
    return str_json


def writetxtfile(filename, list):
    file1 = open(filename, 'w')
    # 循环写入
    for x in list:
        if isinstance(x, str):
            file1.writelines(str(x) + ",")
            file1.write("\n")
        else:
            for y in x:
                file1.writelines(str(y) + ",")
            file1.write("\n")
    file1.close()


def writecsvfile(filename, list):
    ##name = ['one', 'two', 'three']
    # test = pd.DataFrame(columns=name, data=list)  # 数据有三列，列名分别为one,two,three
    csvFile = open(filename, "w", newline='')  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    # 先写入columns_name
    # 写入多行用writerows                                #写入多行
    writer.writerows(list)
    csvFile.close()


def readcsvfile(filename):
    f = csv.reader(open(filename, 'r'))
    x=list(f)

    return x
