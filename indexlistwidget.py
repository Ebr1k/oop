from dblistwidget import dbListWidget

class indexListWidget(dbListWidget):
    def update(self):
        """Update the list of authors for the current book"""
        self.clear()
        current_dynamics = self.getArchive().getDynamics(self.getCurrentRec())
        if current_dynamics:
            indexs = current_dynamics.getIndexList()
            for index in indexs:
                self.addItem(index.getCode(), index.getImportance())
            if indexs:
                self.setCurrentRow(0)