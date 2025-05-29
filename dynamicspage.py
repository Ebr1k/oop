from page import page
from dynamicsTable import dynamicsTable
from dynamicseditform import dynamicsEditForm

class dynamicsPage(page):
    def __init__(self, archive, parent=None):
        page.__init__(self, archive=archive, parent=parent)
        self.setTable(dynamicsTable(archive=archive, parent=parent))
        self.setForm(dynamicsEditForm(archive=archive, parent=parent))
        self.setConnect()