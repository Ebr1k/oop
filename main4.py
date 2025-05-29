from PyQt5.QtWidgets import QApplication
from mainwindow import mainWindow
import sys

# Create the Qt application object
app = QApplication(sys.argv)

# Create and show the main window
mw = mainWindow()
mw.show()

# Start the application event loop
sys.exit(app.exec_())