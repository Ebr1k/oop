from PyQt5.QtWidgets import QListWidget
from rowCode import rowCode
from archiveWidget import archiveWidget


class dbListWidget(QListWidget, archiveWidget):
    def __init__(self, parent=None, archive=None):
        QListWidget.__init__(self, parent)
        archiveWidget.__init__(self, archive)
        self.__rowCode = rowCode()
        self.__currentRec = None  # Initialize current record

    def clear(self):
        """Clear both the list widget and row codes"""
        self.__rowCode.clear()
        super().clear()

    def addItem(self, code, text):
        """Add item with associated code"""
        self.__rowCode.appendRowCode(self.count(), code)
        super().addItem(text)

    def removeSelected(self):
        """Remove selected items and their codes"""
        if self.currentRow() >= 0:  # Check if any item is selected
            self.__rowCode.removeRow(self.currentRow())
            for item in self.selectedItems():
                self.takeItem(self.row(item))

    def getCurrentCode(self):
        """Get code of currently selected item"""
        return self.__rowCode.getCode(self.currentRow()) if self.currentRow() >= 0 else None

    def setCurrentRec(self, value):
        """Set current record and update view"""
        self.__currentRec = value
        self.update()

    def getCurrentRec(self):
        """Get current record"""
        return self.__currentRec

    def getCodes(self):
        """Get all stored codes"""
        return self.__rowCode.getCodes()

    def update(self):
        """Update method to be overridden by subclasses"""
        pass