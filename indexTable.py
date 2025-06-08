from PyQt5.QtWidgets import QTableWidgetItem
from dbTableWidget import dbTableWidget


class indexTable(dbTableWidget):
    def __init__(self, archive, parent=None):
        dbTableWidget.__init__(self, archive=archive, parent=parent,
                               header=[u'важность', u'измерение'])

    def setData(self):
        self.setRowCount(len(self.getArchive().getIndexCodes()))
        r = 0
        for a in self.getArchive().getIndexList():
            self.setItem(r, 0, QTableWidgetItem(a.getImportance()))
            self.setItem(r, 1, QTableWidgetItem(a.getUnit()))
        #    self.setItem(r, 2, QTableWidgetItem(a.getSecname()))
            self.appendRowCode(r, a.getCode())
            r += 1