from PyQt5.QtWidgets import QLineEdit
from editform import editForm


class indexEditForm(editForm):
    def __init__(self, parent=None, archive=None):
        editForm.__init__(self, archive=archive, parent=parent)
        self.__nameEdit = QLineEdit()
        self.__importanceEdit = QLineEdit()
        self.__unitEdit = QLineEdit()
    #    self.__secnameEdit = QLineEdit()

        # Add labels and input fields
        self.addLabel(u'показатель', 0, 0)
        self.addNewWidget(self.__importanceEdit, 0, 1)
        self.addLabel(u'единица', 1, 0)
        self.addNewWidget(self.__unitEdit, 1, 1)
        self.addLabel(u'показатель', 2, 0)
        self.addNewWidget(self.__nameEdit, 2, 1)

        # Select first author if any exist
        if self.getArchive().getIndexList():
            self.setCurrentCode(self.getArchive().getIndexList()[0].getCode())

    def update(self):
        if self.getCurrentCode() in self.getArchive().getIndexCodes():
            index = self.getArchive().getIndex(self.getCurrentCode())
            self.__importanceEdit.setText(index.getImportance())
            self.__unitEdit.setText(index.getUnit())
            self.__nameEdit.setText(index.getName())

    def editClick(self):
        index = self.getArchive().getIndex(self.getCurrentCode())
        index.setImportance(self.__importanceEdit.text())
        index.setUnit(self.__unitEdit.text())
        index.setName(self.__nameEdit.text())

    def newClick(self):
        a = self.getArchive().newIndex("", "", "")
        self.setCurrentCode(a.getCode())

    def delClick(self):
        self.getArchive().removeIndex(self.getCurrentCode())