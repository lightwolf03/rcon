from PySide import QtGui
from models.gui import MainWindow

class MainObject(QtGui.QApplication):
    def __init__(self):
        QtGui.QApplication.__init__(self)
        self.window = MainWindow()
        self.window.show()
        self.exec_()