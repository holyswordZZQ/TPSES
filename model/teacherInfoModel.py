import os
import json
from entity.teacherEntity.Teacher import Teacher


class teacherInfoModel:

    def __init__(self):
        return
# 返回字典数组[{id:'' name:'','college:'','title':'',performance:'','time:''},{...}]
    def readALLTeacherInfo(self):
        dict_list = []
        teachers=[]
        # 当打开二级页面时就自动打开所有文件并把文件内容存储到程序变量中
        file_list = os.listdir('resources/teacherData')  # 获取文件夹中的所有json文件
        for item in file_list:
            if item.find('a') == -1:
                with open('resources/teacherData/' + str(item), 'r', encoding='utf-8') as f:
                    load_dict = json.load(f)  # 把文件打开，并转化为字典元素
                    id=load_dict.get("id")
                    name=load_dict.get("name")
                    college=load_dict.get("college")
                    title=load_dict.get("title")
                    time=load_dict.get("time")
                    available=load_dict.get("available")
                    teacher=Teacher(id,name,college,title,time,available)
                    teachers.append(teacher)

        return teachers

    def readAllTeacherID(self):
        return os.listdir('resources/teacherData')

    def getAllTeacherID(self):
        fileList = os.listdir('resources/teacherData')
        list = []
        for item in fileList:
            list.append(item.split('.', 1)[0])
        return list

    def getTeacherInfo(self,id):
        with open('resources/teacherData/{}'.format(id + '.json'), 'r', encoding='utf-8') as rfile:
            d = json.load(rfile)
            id=d.get("id")
            name=d.get("name")
            college=d.get("college")
            title=d.get("title")
            time=d.get("time")
            available=d.get("available")
            teacher=Teacher(id,name,college,title,time,available)
        return teacher

    def writeTeacherInfo(self,dict):
        with open('resources/teacherData/{}'.format(dict.get("id")) + '.json', 'w', encoding='utf-8') as wfile:
            json.dump(dict, wfile, ensure_ascii=False)

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