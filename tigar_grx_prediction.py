import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic


class TigarGrxPrediction(QtWidgets.QWidget):

    def __init__(self):
        super(TigarGrxPrediction, self).__init__()
        uic.loadUi('view/tigar_grx_prediction.ui', self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TigarGrxPrediction()
    window.show()
    app.exec_()
