from PyQt5.QtWidgets import QApplication
from archiveProject import archive
from dataxml import dataxml
from dynamicseditform import dynamicsEditForm
import sys

app = QApplication(sys.argv)
arch = archive()
dat1 = dataxml(arch, 'old.xml')
dat1.read()
tw1 = dynamicsEditForm(archive=arch)
tw1.show()
sys.exit(app.exec_())