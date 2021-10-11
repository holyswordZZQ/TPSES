import matplotlib.pyplot as plt

def drawPie(x = [222, 42, 455, 664, 454, 334]):
    fig = plt.figure()
    plt.pie(x)
    plt.savefig('C:/Users/lenovo/Desktop/周报素材/新建文件夹/resources/pics/pie.jpg')  # 画饼图，并存储