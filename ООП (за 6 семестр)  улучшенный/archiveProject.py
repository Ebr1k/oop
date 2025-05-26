from Lists import enterpriseList, indexList, dynamicsList

class archive(enterpriseList, indexList, dynamicsList):
    def __init__(self):
        self.__enterpriseList=enterpriseList()
        self.__indexList=indexList()
        self.__dynamicsList=dynamicsList()
    def clear(self):
        self.__enterpriseList.clear()
        self.__indexList.clear()
        self.__dynamicsList.clear()

    def createEnterprise(self, code, name, requisits=None, phone="", contact=""):
        self.__enterpriseList.createItem(code, name, requisits, phone, contact)
    def newEnterprise(self, name, requisits=None, phone="", contact=""):
        self.__enterpriseList.newItem(name, requisits, phone, contact)
    def removeEnterprise(self, value):
        self.__enterpriseList.removeItem(value)
    def getEnterprise(self, code):return self.__enterpriseList.findByCode(code)
    def getEnterpriseList(self): return self.__enterpriseList.getItems()
    def getEnterpriseCodes(self): return self.__enterpriseList.getCodes()

    def createIndex(self, code=0, name="", importance=0, unit=""):
        self.__indexList.createItem(code, name, importance, unit)
    def newIndex(self, name, importance, unit):
        self.__enterpriseList.newItem(name, importance, unit)
    def removeIndex(self, value):
        self.__indexList.removeItem(value)
    def getIndex(self, code):return self.__indexList.findByCode(code)
    def getIndexList(self): return self.__indexList.getItems()
    def getIndexCodes(self): return self.__indexList.getCodes()

    def createDynamics(self, code=0, date="", sense=0, index=None, enterprise=None):
        self.__dynamicsList.createItem(code,date,sense, index, enterprise)
    def newDynamics(self, date,sense, index=None, enterprise=None):
        self.__dynamicsList.newItem(date, sense, index, enterprise)
    def removeDynamics(self, value):
        self.__dynamicsList.removeItem(value)
    def getDynamics(self, code):return self.__dynamicsList.findByCode(code)
    def getDynamicsList(self): return self.__dynamicsList.getItems()
    def getDynamicsCodes(self): return self.__dynamicsList.getCodes()

    def appendIndex(self, value):self.__indexList.appendItem(value)
    def appendEnterprise(self, value):self.__enterpriseList.appendItem(value)
