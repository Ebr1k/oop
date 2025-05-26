class general:
    def __init__(self,code=0, name=""):
        self.setCode(code)
        self.setName(name)
    def setCode(self, value):self.__code=value
    def getCode(self):return self.__code
    def setName(self,value):self.__name=value
    def getName(self):return self.__name


class index(general):
    def __init__(self, code=0, name="", importance=0, unit=""):
        general.__init__(self,code,name)
        self.setImportance(importance)
        self.setUnit(unit)

    def setImportance(self, value):
        if value == 1:
            self.__importance = "Высокая"
        elif value == 2:
            self.__importance = "Средняя"
        elif value == 3:
            self.__importance = "Низкая"
        else:
            self.__importance = "Не определённая"
    def setUnit(self,value): self.__unit = value
    def getImportance(self):return self.__importance
    def getUnit(self):return self.__unit
    def printIndex(self):
        print("Показатель: " + self.getName(), "Важность показателя: " + self.getImportance(), "Единица измерения: " + self.getUnit(), sep="\n", end="\n\n")


class requise:
    def __init__(self, inn=0, ogrn=0, adress=""):
        self.setInn(inn)
        self.setOgrn(ogrn)
        self.setAdress(adress)
    def setInn(self, value): self.__inn = value
    def setOgrn(self, value): self.__ogrn = value
    def setAdress(self, value): self.__adress = value
    def getInn(self): return self.__inn
    def getOgrn(self): return self.__ogrn
    def getAdress(self): return self.__adress
    def printValue(self):
        print(self.getInn(), self.getOgrn(), self.getAdress())

class enterprise(requise, general):
    def __init__(self, code=0, name="",requisits=None, phone="", contact=""):
        general.__init__(self, code, name)
        self.setRequis(requisits)
        self.setPhone(phone)
        self.setContact(contact)
    def setRequis(self, value): self.__requisits = value
    def setPhone(self, value): self.__phone = value
    def setContact(self, value): self.__contact = value
    def getRequis(self):return self.__requisits
    def getPhone(self):return self.__phone
    def getContact(self):return self.__contact
    def printEnterprise(self):
        print("Предприятие: " + self.getName(), "Телефон: " + self.getPhone(),"Контактное лицо: " + self.getContact(), sep="\n")
    def getReqEnterprise(self):
        if self.getRequis():
            inn=self.getRequis().getInn()
            orgn=self.getRequis().getOgrn()
            adress=self.getRequis().getAdress()
        else: ""
        print("ИНН: " + str(inn),"ОРГН: " + str(orgn), "Адрес: " + adress, sep="\n", end="\n\n")