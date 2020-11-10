import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic


class TigarTwas(QtWidgets.QWidget):

    def __init__(self):
        super(TigarTwas, self).__init__()
        uic.loadUi('view/tigar_twas.ui', self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TigarTwas()
    window.show()
    app.exec_()
