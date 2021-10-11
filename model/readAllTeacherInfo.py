import os
import json

#返回字典数组[{id:'' name:'','college:'','title':'',performance:'','time:''},{...}]
def readALLTeacherInfo():
    dict_list=[]
    # 当打开二级页面时就自动打开所有文件并把文件内容存储到程序变量中
    file_list = os.listdir('resources/jsons')  # 获取文件夹中的所有json文件
    for item in file_list:
        if item.find('a')==-1:
            with open('C:/Users/lenovo/Desktop/周报素材/新建文件夹/resources/jsons/' + str(item), 'r',encoding='utf-8') as f:
              load_dict = json.load(f)  # 把文件打开，并转化为字典元素
              dict_list.append(load_dict)  # 将信息添加到列表中
    return dict_list

def readAllTeacherID():
    return os.listdir('resources/jsons')