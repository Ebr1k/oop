from PyQt5.QtWidgets import QApplication
from mainwindow import mainWindow
import sys
import logging
logging.basicConfig(filename='error.log', level=logging.ERROR)
# Create the Qt application object
def main():
    # ваш код
    app = QApplication(sys.argv)

    # Create and show the main window
    mw = mainWindow()
    mw.show()

    # Start the application event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.exception("Произошла ошибка:")
        print(f"Ошибка: {e}")
        sys.exit(1)