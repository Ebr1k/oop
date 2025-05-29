from page import page
from indexTable import indexTable
from indexEditForm import indexEditForm

class indexPage(page):
    def __init__(self, archive, parent=None):
        page.__init__(self, archive=archive, parent=parent)
        self.setTable(indexTable(archive=archive, parent=parent))
        self.setForm(indexEditForm(archive=archive, parent=parent))
        self.setConnect()