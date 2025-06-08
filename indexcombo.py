from dbcombobox import dbComboBox


class indexCombo(dbComboBox):
    def update(self):

        self.clear()

        # Populate with all publishers
        for index in self.getArchive().getIndexList():
            self.addItem(index.getCode(), index.getName())

        # Set current selection if applicable
        current_dynamics = self.getArchive().getDynamics(self.getCurrentRec())
        if current_dynamics and current_dynamics.getIndex():
            self.setCurrentCode(current_dynamics.getIndex().getCode())