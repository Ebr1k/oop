from PyQt5.QtWidgets import QComboBox, QSizePolicy
from PyQt5.QtCore import Qt
from rowCode import rowCode
from archiveWidget import archiveWidget


class dbComboBox(QComboBox, archiveWidget):
    def __init__(self, parent=None, archive=None):

        super().__init__(parent)
        archiveWidget.__init__(self, archive)

        self.__rowCode = rowCode()
        self.__currentRec = None

        # Configure visual properties
        self.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.setFocusPolicy(Qt.StrongFocus)

    def clear(self):
        """Clear all items and associated codes"""
        self.__rowCode.clear()
        super().clear()

    def addItem(self, code, text, userData=None):
        """
        Add an item to the combo box

        Args:
            code: Internal code to associate with item
            text: Display text
            userData: Optional additional user data
        """
        self.__rowCode.appendRowCode(self.count(), code)
        super().addItem(text, userData)

    def removeItem(self, index):
        """
        Remove item at specified index

        Args:
            index: Position of item to remove
        """
        if 0 <= index < self.count():
            self.__rowCode.removeRow(index)
            super().removeItem(index)

    def getCurrentCode(self):
        """Get the code for currently selected item"""
        idx = self.currentIndex()
        return self.__rowCode.getCode(idx) if idx >= 0 else None

    def setCurrentCode(self, code):
        """
        Set current selection by code

        Args:
            code: Code of item to select
        """
        row = self.__rowCode.getRow(code)
        if row is not None and 0 <= row < self.count():
            self.setCurrentIndex(row)

    def setCurrentRec(self, value):
        """Set current record reference and trigger update"""
        self.__currentRec = value
        self.update()

    def getCurrentRec(self):
        """Get current record reference"""
        return self.__currentRec

    def update(self):
        """Update contents - should be overridden in subclasses"""
        pass

    def codes(self):
        """Get all stored codes as a list"""
        return self.__rowCode.getCodes()

    def findCode(self, code):
        """Find if a code exists in the combo box"""
        return self.__rowCode.getRow(code) is not None