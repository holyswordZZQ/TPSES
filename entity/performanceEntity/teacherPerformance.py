class teacherPerformance():
    def __init__(self,paperTitle,paperAuthor,paperTime,paperJournals,\
                 monographName,monographBelonged,monographNumber,monographTime,\
                 prizeName,prizeAwardingCompany,prizeProject,\
                 projectName,projectType,projectSource,projectIncharge,projectApplyerRole,projectTime,\
                 bookName,bookPublisher,bookISBN,bookTime,\
                 performanceID,type,credit,teacherID,lastUpdateTime,relatedPic,note):
        self.paperTitle=paperTitle                      #业绩对应的论文名字
        self.paperAuthor=paperAuthor                    #业绩对应的论文作者（是一个字典，有多人）
        self.paperTime=paperTime                        #论文时间
        self.paperJournals=paperJournals                #业绩对应的论文期刊

        self.monographName=monographName                #业绩对应专著名
        self.monographBelonged=monographBelonged        #业绩对应专著作者
        self.monographNumber=monographNumber            #业绩对应软著编号
        self.monographTime=monographTime                #软著时间

        self.prizeName = prizeName                      #业绩对应的奖项名字
        self.prizeAwardingCompany = prizeAwardingCompany# 业绩对应的赞助商
        self.prizeProject= prizeProject                 # 获奖的项目


        self.projectName=projectName                    #业绩对应项目名字
        self.projectType=projectType                    #项目类型(包括大创)
        self.projectSource=projectSource                #业绩对应的委托单位
        self.projectIncharge=projectIncharge          #业绩对应的项目负责人
        self.projectApplyerRole=projectApplyerRole      #申请工分的老师再项目中担任角色
        self.projectTime=projectTime                    #项目的时间

        self.bookName=bookName                          #教材名
        self.bookPublisher=bookPublisher                #出版商
        self.bookISBN=bookISBN                          #ISBN号
        self.bookTime=bookTime                          #出版时间

        self.performanceID = performanceID              # 业绩ID
        self.type=type                                  #业绩种类
        self.credit = credit                            # 业绩公分
        self.teacherID = teacherID                      # 业绩对应的老师ID
        self.lastUpdateTime=lastUpdateTime              # 最后一次更新的时间
        self.relatedPic=relatedPic                      #相关的图片
        self.note=note                                  #备注