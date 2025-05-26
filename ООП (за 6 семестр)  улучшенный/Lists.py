from generalCharacter import general, enterprise, index
from dynamicsStat import dynamics



class generalList:
    def __init__(self):self.__list=[]
    def clear(self):self.__list=[]
    def findByCode(self,code):
        for l in self.__list:
            if l.getCode()==code:return l
    def getCodes(self):return [s.getCode() for s in self.__list]
    def getNewCode(self):return max(self.getCodes())+1
    def getItems(self):return [s for s in self.__list]
    def appendItem(self, value):
        if isinstance(value,general):self.__list.append(value)
    def appendList(self,value):self.__list.append(value)
    def removeList(self,code):
       for s in self.__list:
           if s.getCode()==code:self.__list.remove(s)
    def removeItem(self,value):
        if isinstance(value,general):self.__list.remove(value)
        if isinstance(value,int):self.__list.remove(self.findByCode(value))


class dynamicsList(generalList, dynamics):
    def createItem(self, code=0, date="", sense=0, indexs=None, enterprises=None):
        if code in self.getCodes():print("Динамика показателей с кодом %s уже существует")
        else:generalList.appendItem(self, dynamics(code, date, sense, indexs, enterprises))
    def newItem(self, date="", sense=0, indexs=None, enterprises=None):
        generalList.appendItem(self, dynamics(self.getNewCode(), date, sense, indexs, enterprises))

    def appendItem(self, value):
        if isinstance(value, dynamics): generalList.appendItem(self, value)


class enterpriseList(generalList, enterprise):
    def createItem(self, code, name, requisits=None, phone=0, contact=""):
        if code in self.getCodes():print("Предприятие с кодом %s уже существует")
        else:generalList.appendItem(self, enterprise(code, name, requisits, phone, contact))
    def newItem(self, name, requisits=None, phone="", contact=""):
        generalList.appendItem(self, enterprise(self.getNewCode(), name, requisits, phone, contact))
    def appendItem(self, value):
        if isinstance(value, enterprise): generalList.appendItem(self, value)


class indexList(generalList, index):
    def createItem(self, code, name, importance, unit):
        if code in self.getCodes():
            print("Показатель с кодом %s уже существует")
        else:
            generalList.appendItem(self, index(code, name, importance, unit))

    def newItem(self, name, importance, unit):
        generalList.appendItem(self, index(self.getNewCode(), name, importance, unit))
    def appendItem(self, value):
        if isinstance(value, index): generalList.appendItem(self, value)