from PyQt5.QtWidgets import QTableWidgetItem
from dbTableWidget import dbTableWidget


class enterpriseTable(dbTableWidget):
    def __init__(self, archive, parent=None):
        dbTableWidget.__init__(self, archive=archive, parent=parent, header=[u'название', u'сокр. название'])

    def setData(self):
        self.setRowCount(len(self.getArchive().getEnterpriseCodes()))
        r = 0
        for p in self.getArchive().getEnterpriseList():
            self.setItem(r, 0, QTableWidgetItem(p.getName()))
        #    self.setItem(r, 1, QTableWidgetItem(p.getReqEnterprise()))
            self.appendRowCode(r, p.getCode())
            r += 1