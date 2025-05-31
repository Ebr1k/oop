from PyQt5.QtWidgets import (QVBoxLayout, QLineEdit, QPushButton, QLabel,
                             QSpinBox, QFileDialog)
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from editform import editForm
from dblistwidget import dbListWidget
from dbcombobox import dbComboBox
from enterprisecombo import enterpriseCombo
from indexcombo import indexCombo
from indexlistwidget import indexListWidget


class dynamicsEditForm(editForm):
    def __init__(self, parent=None, archive=None):
        """Initialize book editing form with all widgets and connections"""
        super().__init__(archive=archive, parent=parent)

        # Create widgets

    #    self.__nameEdit = QLineEdit()
    #    self.__imgEdit = QLineEdit()
    #   self.__imgButton = QPushButton(u'найти')
    #    self.__indexListWidget = indexListWidget(archive=archive) #скорее всего не понадобится, так как не нужно отображать спикос показателей отельно
    #    self.__removeButton = QPushButton(u'удалить')

    #    self.__appendButton = QPushButton(u'добавить')
        self.__indexCombo = indexCombo(archive=archive)
        self.__enterpriseCombo = enterpriseCombo(archive=archive)
        self.__indexLabel = QLabel()
        self.__senseSpin = QSpinBox()
        self.__senseSpin.setRange(0,100000)
        # Configure spin boxes
    #    self.__yearSpin = QSpinBox()
    #    self.__yearSpin.setRange(-3000, QtCore.QDate.currentDate().year())

    # Добавить сюда дату
        # Setup form layout
        self._setup_form_layout()

        # Connect signals
        #self._connect_signals()

        # Initialize with first book if available
        if self.getArchive().getDynamicsList():
            self.setCurrentCode(self.getArchive().getDynamicsList()[0].getCode())

    def _setup_form_layout(self):
        """Configure the form's widget layout"""
        self.addLabel(u"показатель", 0, 0)
        self.addNewWidget(self.__indexCombo, 0, 1)
        self.addLabel(u"компания", 1, 0)
        self.addNewWidget(self.__enterpriseCombo, 1, 1)
        self.addLabel(u"значение", 2, 0)
        self.addNewWidget(self.__senseSpin, 2, 1)
    #    self.addLabel('название', 0, 0)
    #    self.addNewWidget(self.__nameEdit, 0, 1)
    """ self.addLabel(u'обложка', 1, 0)
        self.addNewWidget(self.__imgEdit, 1, 1)
        self.addNewWidget(self.__imgButton, 1, 2)
        self.addLabel(u'авторы', 2, 0)
        self.addNewWidget(self.__authorListWidget, 2, 1)
        self.addNewWidget(self.__removeButton, 2, 2)
        self.addNewWidget(self.__authorCombo, 3, 1)
        self.addNewWidget(self.__appendButton, 3, 2)
        self.addLabel(u'издательство', 4, 0)
        self.addNewWidget(self.__publCombo, 4, 1)
        self.addLabel(u'год', 5, 0)
        self.addNewWidget(self.__yearSpin, 5, 1)
        self.addLabel(u'страницы', 6, 0)
        self.addNewWidget(self.__pagesSpin, 6, 1)"""
    """
        # Image preview layout
        self.__pixVBox = QVBoxLayout()
        self.__pixVBox.addWidget(self.__pixlabel)
        self.__pixVBox.addStretch(1)
        self.addLeftLayout(self.__pixVBox)"""


    #def _connect_signals(self):
    #    """Connect widget signals to their handlers"""
    #    self.__removeButton.clicked.connect(self.removeAuthor)
    #    self.__appendButton.clicked.connect(self.appendAuthor)
    #    self.__imgButton.clicked.connect(self.openImg)

    """def openImg(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            'Open file',
            './',
            "Image files (*.jpg *.png *.gif)"
        )
        if filename:
            self.__imgEdit.setText(filename)
            self.__pixlabel.setPixmap(
                QPixmap(filename).scaled(200, 300, QtCore.Qt.KeepAspectRatio)
            )"""

    def update(self):
        if self.getCurrentCode() in self.getArchive().getDynamicsCodes():
        #    self.__nameEdit.setText(self.getArchive().getDynamics(self.getCurrentCode()).getName())
        #    self.__imgEdit.setText(self.getArchive().getDynamics(self.getCurrentCode()).getImg())
            self.__enterpriseCombo.setCurrentRec(self.getCurrentCode())
            self.__indexCombo.setCurrentRec(self.getCurrentCode())
            self.__senseSpin.setValue(self.getArchive().getDynamics(self.getCurrentCode()).getSense())

    def editClick(self):
        self.getArchive().getDynamics(self.getCurrentCode()).setName(self.__nameEdit.text())
    #    self.getArchive().getDynamics(self.getCurrentCode()).setImg(self.__imgEdit.text())
    #    self.getArchive().getDynamics(self.getCurrentCode()).clearAuthorList()
    #    for c in self.__authorListWidget.getCodes():
    #        self.getArchive().getDynamics(self.getCurrentCode()).appendAuthor(self.getLibrary().getAuthor(c))
    #    self.getArchive().getDynamics(self.getCurrentCode()).setPubl(self.getLibrary().getPubl(self.__publCombo.getCurrentCode()))
        self.getArchive().getDynamics(self.getCurrentCode()).setSense(self.__senseSpin.value())
    #    self.getArchive().getDynamics(self.getCurrentCode()).setPages(self.__pagesSpin.value())
    def newClick(self):
        b=self.getArchive().newDynamics("31.05.2025",0,None,None)
        self.setCurrentCode(b.getCode())
    def delClick(self):
        self.getArchive().removeDynamics(self.getCurrentCode())
    """def removeAuthor(self):
        code=self.__authorListWidget.getCurrentCode()
        if code:
            self.__authorListWidget.removeSelected()
            self.__authorCombo.addItem(code,self.getLibrary().getAuthor(code).getBiblioStr())
    def appendAuthor(self):
        code=self.__authorCombo.getCurrentCode()
        if code:
            self.__authorCombo.removeItem(self.__authorCombo.currentIndex())
            self.__authorListWidget.addItem(code,self.getLibrary().getAuthor(code).getBiblioStr())
"""