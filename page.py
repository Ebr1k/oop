from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from archiveWidget import archiveWidget

class page(QWidget, archiveWidget):
    def __init__(self, archive, parent=None):
        QWidget.__init__(self, parent=parent)
        archiveWidget.__init__(self, archive)
        self.__vbox = QVBoxLayout()
        self.__hbox = QHBoxLayout()
        self.__buttonbox = QVBoxLayout()
        self.__newButton = QPushButton(u"Добавить")
        self.__editButton = QPushButton(u"Изменить")
        self.__delButton = QPushButton(u"Удалить")
        self.__vbox.addLayout(self.__hbox)
        self.__hbox.addLayout(self.__buttonbox)
        self.__buttonbox.addWidget(self.__newButton)
        self.__buttonbox.addWidget(self.__editButton)
        self.__buttonbox.addWidget(self.__delButton)
        self.__buttonbox.addStretch(1)
        self.setLayout(self.__vbox)

    def setTable(self, value):
        self.__table = value
        self.__vbox.insertWidget(0, self.__table)

    def setForm(self, value):
        self.__form = value
        self.__hbox.insertWidget(0, self.__form)

    def newClick(self):
        self.__form.newClick()
        self.__table.update(self.__form.getCurrentCode())

    def editClick(self):
        self.__form.editClick()
        self.__table.update()

    def delClick(self):
        self.__form.delClick()
        self.__table.update()

    def tableClick(self):
        self.__form.setCurrentCode(self.__table.getCurrentCode())

    def setConnect(self):
        self.__newButton.clicked.connect(self.newClick)
        self.__editButton.clicked.connect(self.editClick)
        self.__delButton.clicked.connect(self.delClick)
        self.__table.currentCellChanged.connect(self.tableClick)

    def update(self):
        self.__table.update()