import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic


class FusionAssociationTest(QtWidgets.QWidget):

    def __init__(self):
        super(FusionAssociationTest, self).__init__()
        uic.loadUi('view/fusion_association_test.ui', self)

        self.FATLaunch = self.findChild(QtWidgets.QPushButton, 'FATLAUNCH')
        self.FATLaunch.clicked.connect(lambda: self.run_FAT())

        self.FATCHR = self.findChild(QtWidgets.QLineEdit, 'FATCHR')

        self.FATOUTLABEL = self.findChild(QtWidgets.QLabel, 'FATOUTLABEL')
        self.FATOUT = self.findChild(QtWidgets.QPushButton, 'FATOUT')
        self.FATOUT.clicked.connect(
            lambda: self.FATOUTLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FATREFLDCHRLABEL = self.findChild(QtWidgets.QLabel, 'FATREFLDCHRLABEL')
        self.FATREFLDCHR = self.findChild(QtWidgets.QPushButton, 'FATREFLDCHR')
        self.FATREFLDCHR.clicked.connect(
            lambda: self.FATREFLDCHRLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))


        self.FATSUMSTATSLABEL = self.findChild(QtWidgets.QLabel, 'FATSUMSTATSLABEL')
        self.FATSUMSTATS = self.findChild(QtWidgets.QPushButton, 'FATSUMSTATS')
        self.FATSUMSTATS.clicked.connect(
            lambda: self.FATSUMSTATSLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FATWEIGHTSLABEL = self.findChild(QtWidgets.QLabel, 'FATWEIGHTSLABEL')
        self.FATWEIGHTS = self.findChild(QtWidgets.QPushButton, 'FATWEIGHTS')
        self.FATWEIGHTS.clicked.connect(
            lambda: self.FATWEIGHTSLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FATWEIGHTSDIRLABEL = self.findChild(QtWidgets.QLabel, 'FATWEIGHTSDIRLABEL')
        self.FATWEIGHTSDIR = self.findChild(QtWidgets.QPushButton, 'FATWEIGHTSDIR')
        self.FATWEIGHTSDIR.clicked.connect(
            lambda: self.FATWEIGHTSDIRLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Open directory')))

        self.FATCOLOCP = self.findChild(QtWidgets.QLineEdit, 'FATCOLOCP')

        self.FATGWASN = self.findChild(QtWidgets.QLineEdit, 'FATGWASN')

        self.FATMAXIMPUTE = self.findChild(QtWidgets.QLineEdit, 'FATMAXIMPUTE')

        self.FATMINR2PRED = self.findChild(QtWidgets.QLineEdit, 'FATMINR2PRED')

        self.FATPERM = self.findChild(QtWidgets.QLineEdit, 'FATPERM')

        self.FATPERMMINP = self.findChild(QtWidgets.QLineEdit, 'FATPERMMINP')

        self.FATPANELN = self.findChild(QtWidgets.QLineEdit, 'FATPANELN')

        self.FATFORCEMODEL = self.findChild(QtWidgets.QComboBox, 'FATFORCEMODEL')


    def validateFAT(self):
        comm = "Rscript FUSION.assoc_test.R "
        comm = comm + " --sumstats " + str(self.FATSUMSTATSLABEL.text())
        comm = comm + " --out " + str(self.FATOUTLABEL.text())
        comm = comm + " --weights " + str(self.FATWEIGHTSLABEL.text())
        comm = comm + " --weights_dir " + str(self.FATWEIGHTSDIRLABEL.text())
        comm = comm + " --ref_ld_chr " + str(self.FATREFLDCHRLABEL.text())
        comm = comm + " --chr " + str(self.FATCHR.text())
        comm = comm + " --coloc_P " + str(self.FATCOLOCP.text())
        comm = comm + " --force_model " + str(self.FATFORCEMODEL.currentText())
        comm = comm + " --GWASN " + str(self.FATGWASN.text())
        comm = comm + " --max_impute " + str(self.FATMAXIMPUTE.text())
        comm = comm + " --min_r2pred " + str(self.FATMINR2PRED.text())
        comm = comm + " --PANELN " + str(self.FATPANELN.text())
        comm = comm + " --perm " + str(self.FATPERM.text())
        comm = comm + " --perm_minp " + str(self.FATPERMMINP.text())
        return (comm)

    def run_FAT(self):

        command = self.validateFAT()
        print(command)

        with open('./methods/FUSION/SRC/fusion_tmp.sh', 'w+') as file:
            file.write('#!/bin/bash\n')
            file.write('cd ..\n')
            file.write(command)

        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = FusionAssociationTest()
    window.show()

    app.exec_()
