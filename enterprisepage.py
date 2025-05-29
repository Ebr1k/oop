from page import page
from enterpriseTable import enterpriseTable
from enterpriseEditForm import enterpriseEditForm

class enterprisePage(page):
    def __init__(self, archive, parent=None):
        page.__init__(self, archive=archive, parent=parent)
        self.setTable(enterpriseTable(archive=archive, parent=parent))
        self.setForm(enterpriseEditForm(archive=archive, parent=parent))
        self.setConnect()