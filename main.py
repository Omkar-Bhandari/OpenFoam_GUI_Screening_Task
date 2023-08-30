import sys
from PyQt5.QtWidgets import QApplication
from handler import Handler


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Handler()
    win.show()
    sys.exit(app.exec_())
