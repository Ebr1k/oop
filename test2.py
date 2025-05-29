from PyQt5.QtWidgets import QApplication
from archiveProject import archive
from dataxml import dataxml
from dynamicspage import dynamicsPage
import sys

app = QApplication(sys.argv)
arch = archive()
dat1 = dataxml(arch, 'old.xml')
dat1.read()
tw1 = dynamicsPage(archive=arch)
tw1.show()
sys.exit(app.exec_())