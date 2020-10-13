import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic


class TigarModelTraining(QtWidgets.QWidget):

    def __init__(self):
        super(TigarModelTraining, self).__init__()
        uic.loadUi('view/tigar_model_training.ui', self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TigarModelTraining()
    window.show()
    app.exec_()
