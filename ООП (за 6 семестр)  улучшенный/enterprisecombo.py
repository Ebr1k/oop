from dbcombobox import dbComboBox


class enterpriseCombo(dbComboBox):
    def update(self):

        self.clear()

        # Populate with all publishers
        for enterprise in self.getArchive().getEnterpriseList():
            self.addItem(enterprise.getCode(), enterprise.getName())

        # Set current selection if applicable
        current_dynamics = self.getLibrary().getDynamics(self.getCurrentRec())
        if current_dynamics and current_dynamics.getEnterprise():
            self.setCurrentCode(current_dynamics.getEnterprise().getCode())