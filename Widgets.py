from PyQt5.QtWidgets import QTableWidget

from rowCode import rowCode

class dynamicsWidget:
    def __init__(self, dynamics=None):
        self.__dynamics = dynamics
    def getDynamics(self):
        return self.__dynamics


class dbTableWidget(QTableWidget, dynamicsWidget):
    def __init__(self, dynamics, parent=None, header=[]):
        QTableWidget.__init__(self)
        dynamicsWidget.__init__(self, dynamics)
        self.__rowCode = rowCode()
        self.setHeader(header)
        self.update()

    def setHeader(self, value):
        self.setColumnCount(len(value))
        self.setHorizontalHeaderLabels(value)

    def clearContents(self):
        self.__rowCode.clear()
        QTableWidget.clearContents(self)

    def getCodes(self):
        return self.__rowCode.getCodes()

    def getCurrentCode(self):
        return self.__rowCode.getCode(self.currentRow())

    def setCurrentCode(self, code):
        if code:
            self.setCurrentCell(self.__rowCode.getRow(code), 0)

    def appendRowCode(self, row, code):
        self.__rowCode.appendRowCode(row, code)

    def update(self, code=0):
        self.clearContents()
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCode(code)

    def setData(self):
        pass