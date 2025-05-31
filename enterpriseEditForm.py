from PyQt5.QtWidgets import QLineEdit
from editform import editForm


class enterpriseEditForm(editForm):
    def __init__(self, parent=None, archive=None):
        editForm.__init__(self, archive=archive, parent=parent)
        self.__nameEdit = QLineEdit()
    #    self.__shortnameEdit = QLineEdit()
        self.addLabel(u'название', 0, 0)
        self.addNewWidget(self.__nameEdit, 0, 1)
    #    self.addLabel(u'сокр. название', 1, 0)
    #    self.addNewWidget(self.__shortnameEdit, 1, 1)

        if self.getArchive().getEnterpriseList():
            self.setCurrentCode(self.getArchive().getEnterpriseList()[0].getCode())

    def update(self):
        if self.getCurrentCode() in self.getArchive().getEnterpriseCodes():
            self.__nameEdit.setText(self.getArchive().getEnterprise(self.getCurrentCode()).getName())
        #    self.__shortnameEdit.setText(self.getArchive().getPubl(self.getCurrentCode()).getShortname())

    def editClick(self):
        self.getArchive().getEnterprise(self.getCurrentCode()).setName(self.__nameEdit.text())
    #    self.getArchive().getEnterprise(self.getCurrentCode()).setShortname(self.__shortnameEdit.text())

    def newClick(self):
        p = self.getArchive().newEnterprise("", "")
        self.setCurrentCode(p.getCode())

    def delClick(self):
        self.getArchive().removeEnterprise(self.getCurrentCode())