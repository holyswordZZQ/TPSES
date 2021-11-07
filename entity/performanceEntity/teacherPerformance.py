class teacherPerformance():
    def __init__(self,paperTitle,paperAuthor,paperMoneyAmount,paperJournals,paperIF,\
                 monographName,monographBelonged,monographMoneyAmount,\
                 prizeName,prizeAwardingCompany,prizeWinner,prizeAmount,\
                 projectName,projectRequester,projectPrincipal,projectMoneyAmount,\
                 performanceID,type,credit,teacherID,lastUpdateTime,performanceHappenTime,relatedPic,note):
        self.paperTitle=paperTitle                      #业绩对应的论文名字
        self.paperAuthor=paperAuthor                    #业绩对应的论文作者（是一个字典，有多人）
        self.paperMoneyAmount=paperMoneyAmount          #业绩对应的金额
        self.paperJournals=paperJournals                #业绩对应的论文期刊
        self.paperIF=paperIF                            #业绩对应的论文影响因子
        self.monographName=monographName                #业绩对应专著名
        self.monographBelonged=monographBelonged        #业绩对应专著作者
        self.monographMoneyAmount=monographMoneyAmount  #业绩对应的专著金额
        self.prizeName = prizeName                      #业绩对应的奖项名字
        self.prizeAwardingCompany = prizeAwardingCompany     # 业绩对应的赞助商
        self.prizeWinner = prizeWinner                  # 业绩对应的获奖者
        self.prizeAmount = prizeAmount                  # 业绩对应的奖金
        self.projectName=projectName                    #业绩对应项目名字
        self.projectRequester=projectRequester          #业绩对应的委托单位
        self.projectPrincipal=projectPrincipal          #业绩对应的项目负责人
        self.projectMoneyAmount=projectMoneyAmount      #业绩对应的项目经费

        self.performanceID = performanceID              # 业绩ID
        self.type=type                                  #业绩种类
        self.credit = credit                            # 业绩公分
        self.teacherID = teacherID                      # 业绩对应的老师ID
        self.lastUpdateTime=lastUpdateTime              # 最后一次更新的时间
        self.performanceHappenTime=performanceHappenTime#业绩产生的时间
        self.relatedPic=relatedPic                      #相关的图片
        self.note=note                                  #备注