from dbcombobox import dbComboBox


class indexCombo(dbComboBox):
    def update(self):
        """Update the combo box with authors not already assigned to current book"""
        self.clear()
        current_dynamics = self.getArchive().getDynamics(self.getCurrentRec())

        if current_dynamics:
            assigned_index = current_dynamics.getIndexList()
            for index in self.getLibrary().getIndexList():
                if index not in assigned_index:
                    self.addItem(index.getCode(), index.getImportance())