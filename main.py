import sys
from PyQt5.QtWidgets import QApplication

from HideFaceController import HideFaceApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = HideFaceApp()
    MainWindow.show()
    sys.exit(app.exec_())