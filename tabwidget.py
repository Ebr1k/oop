from PyQt5.QtWidgets import QTabWidget
import sys, os
from dynamicspage import dynamicsPage
from indexpage import indexPage
from enterprisepage import enterprisePage


class tabWidget(QTabWidget):
    def __init__(self, archive, parent=None):
        QTabWidget.__init__(self, parent)
        self.__dynamicsPage = dynamicsPage(archive=archive)
        self.addTab(self.__dynamicsPage, u"Динамики")
        self.__indexPage = indexPage(archive=archive)
        self.addTab(self.__indexPage, u"Показатели")
        self.__enterprisePage = enterprisePage(archive=archive)
        self.addTab(self.__enterprisePage, u"Компании")
        self.currentChanged.connect(self.update)

    def update(self):
        self.__dynamicsPage.update()
        self.__indexPage.update()
        self.__enterprisePage.update()