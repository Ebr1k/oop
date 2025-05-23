from generalCharacter import index, enterprise
import datetime as DT

class dynamics(index, enterprise):
    def __init__(self, code=0, date="", sense=0, indexs=None, enterprises=None):
        self.setCode(code)
        self.setIndex(indexs)
        self.setEnterprises(enterprises)
        self.setDate(date)
        self.setSense(sense)
    def setIndex(self, value):
        if isinstance(value, index):self.__indexs=value
        else:self.__indexs = None
    def setEnterprises(self, value):
        if isinstance(value, enterprise):self.__enterprises = value
        else:
            self.__enterprises = None
    def setDate(self, value):self.__data = DT.datetime.strptime(value, '%d.%m.%Y').date()
    def setSense(self, value):self.__sense = value
    def getIndex(self):return self.__indexs
    def getEnterprises(self):return self.__enterprises
    def getDate(self):return self.__data
    def getSense(self):return self.__sense

    def getEnterpriseCode(self):
        if self.getEnterprises():
            return self.__enterprises.getCode()
        else:
            ent = enterprise()
    def getIndexCode(self):
        if self.getIndex():
            return self.__indexs.getCode()
        else:
            inx = index()
    def printIndicator(self):
        if self.getEnterprises():
            ent = self.getEnterprises()
        else:
            ent = enterprise()
        if self.getIndex():
            inx = self.getIndex()
        else:
            inx = index()
        print(self.getDate(), str(ent.getName()), inx.getName() + " =", self.__sense, inx.getUnit())


class analysis(dynamics):
    def __init__(self, dyn1, dyn2):
        self.setDyn1(dyn1)
        self.setDyn2(dyn2)

    def setDyn1(self, value):
        self.__dyn1 = value

    def setDyn2(self, value):
        self.__dyn2 = value

    def getDyn1(self):
        return self.__dyn1

    def getDyn2(self):
        return self.__dyn2

    def getAnalysis(self):
        if self.getDyn1():
            dyn1 = self.getDyn1()
        else:
            dyn1 = dynamics()
        if self.getDyn2():
            dyn2 = self.getDyn2()
        else:
            dyn2 = dynamics()
        sen1 = dyn1.getSense()
        sen2 = dyn2.getSense()
        if dyn1.getDate() >= dyn2.getDate():
            return -(sen2 - sen1)
        elif dyn1.getDate() < dyn2.getDate():
            return -(sen1 - sen2)
    def printAnalysis(self):
        print("Изменение показателя =", self.getAnalysis())
