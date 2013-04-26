from models.gui import MainWindow
from models.const import VARS
from PySide import QtGui
import logging
import sys


if __name__ == '__main__':
    logging.basicConfig(filename='pyrcon.log', level=logging.WARNING)
    print(VARS)
    app = QtGui.QApplication(sys.argv)
    WINDOW = MainWindow()
    VARS.window = WINDOW
    WINDOW.show()
    sys.exit(app.exec_())
