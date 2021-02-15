# This Python file uses the following encoding: utf-8

# if__name__ == "__main__":
#     pass
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys
from gui import Ui_MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
