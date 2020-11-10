import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic


class TigarCovMatrix(QtWidgets.QWidget):

    def __init__(self):
        super(TigarCovMatrix, self).__init__()
        uic.loadUi('view/tigar_cov_matrix.ui', self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TigarCovMatrix()
    window.show()
    app.exec_()
