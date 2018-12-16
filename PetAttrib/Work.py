class Work:         #不采用单例模式，单例中存放一个dict的方法（可防止重复项，检索方便）的原因是：1.实现简单 2.数据量本身不多且人为操作所以没必要考虑重复
    def __init__(self,WorkType,WorkTime):
        '''worktype工作类型。worktime以小时为单位'''
        self.WorkType=WorkTime
        self.WorkTime=WorkTime

#Tuple of Work
#TODO 完善此列表
works=(Work('wash',1),Work('clean',1))