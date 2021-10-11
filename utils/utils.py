import matplotlib.pyplot as plt

def drawPie(x = [222, 42, 455, 664, 454, 334]):
    fig = plt.figure()
    plt.pie(x)
    plt.savefig('C:/Users/lenovo/Desktop/周报素材/新建文件夹/resources/pics/pie.jpg')  # 画饼图，并存储

# def fuzzyMatch(lists,string,stat):
#     if stat==0:     #stat==0是用来模糊搜索老师信息
#         for specTeacherInfo in lists:
#             if specTeacherInfo.get('name').find!=-1: