class Teacher:
    def __init__(self,id,name,college,title,time,available):
        self.id=id
        self.name=name
        self.college=college
        self.title=title
        self.time=time
        self.available=available

    def __str__(self):
        return "id: "+self.id+" name: "+self.name+" college: "+self.college+" title: "+self.title+" time: "+self.time+" available: "+self.available