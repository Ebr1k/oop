from PyQt5.QtWidgets import QTableWidgetItem, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from dbTableWidget import dbTableWidget
from pixwidget import pixWidget


class dynamicsTable(dbTableWidget):
    def __init__(self, archive, parent=None):
        dbTableWidget.__init__(self, archive=archive, parent=parent,
                               header=[u'дата', u'значение', u'показатели', u'компания'])

    def setData(self):
        self.setRowCount(len(self.getArchive().getDynamicsCodes()))
        r = 0
        for b in self.getArchive().getDynamicsList():
            date_str = b.getDate().strftime("%Y-%m-%d")
            self.setItem(r, 0, QTableWidgetItem(date_str))
        #    self.setCellWidget(r, 1, pixWidget(b.getImg()))
        #    self.setItem(r, 1, QTableWidgetItem(b.getSense()))
            if b.getIndex():
                self.setItem(r, 2, QTableWidgetItem(b.getIndex().getName()))
            else:
                self.setItem(r, 2, QTableWidgetItem(''))
            if b.getEnterprises():
                self.setItem(r, 3, QTableWidgetItem(b.getEnterprises().getName()))
            else:
                self.setItem(r, 3, QTableWidgetItem(''))
            self.setItem(r, 1, QTableWidgetItem(str(b.getSense())))
            #self.setItem(r, 5, QTableWidgetItem(str(b.getDate())))
            self.appendRowCode(r, b.getCode())
            r += 1