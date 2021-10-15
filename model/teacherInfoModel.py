import os
import json



class teacherInfoModel:

    def __init__(self):
        return
# 返回字典数组[{id:'' name:'','college:'','title':'',performance:'','time:''},{...}]
    def readALLTeacherInfo(self):
        dict_list = []
        # 当打开二级页面时就自动打开所有文件并把文件内容存储到程序变量中
        file_list = os.listdir('resources/jsons')  # 获取文件夹中的所有json文件
        for item in file_list:
            if item.find('a') == -1:
                with open('resources/jsons/' + str(item), 'r', encoding='utf-8') as f:
                    load_dict = json.load(f)  # 把文件打开，并转化为字典元素
                    dict_list.append(load_dict)  # 将信息添加到列表中
        print(dict_list)
        return dict_list

    def readAllTeacherID(self):
        return os.listdir('resources/jsons')

    def getTeacherInfo(self,id):
        with open('resources/jsons/{}'.format(id + '.json'), 'r', encoding='utf-8') as rfile:
            d = json.load(rfile)
        return d

    def writeTeacherInfo(self,id):
        with open('resources/jsons/{}'.format(id['id']) + '.json', 'w', encoding='utf-8') as wfile:
            json.dump(id, wfile, ensure_ascii=False)

    def readPerforAndCredit(self):
        with open('resources/material/perfor and credit.json', 'r', encoding='utf-8') as rfile:
            dict = json.load(rfile)
        return dict

    def readPerforID(self):
        with open('resources/txt/perforID.txt', 'r', encoding='utf-8') as rfile:
            a = rfile.read()
        print(a)
        return int(a)

    def readPerforAndCredit(self):
        with open('resources/material/perfor and credit.json', 'r', encoding='utf-8') as rfile:
            dict = json.load(rfile)
        return dict