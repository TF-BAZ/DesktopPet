
class PetAttrib:
    def __init__(self,nameP,levelP,dayP):
        '''初始化：名字name，目前等级level，已使用天数day'''
        self.name=nameP
        self.level=levelP
        self.day=dayP

    def levelUp(self):
        '''levelUp'''
        self.level+=1

    def workBegin(self,work):
        self.working = True
        self.work = work
        self.workBeginTime = 0  # TODO 获得调用此函数的时间
