import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic


class FusionComputeWeights(QtWidgets.QWidget):

    def __init__(self):
        super(FusionComputeWeights, self).__init__()
        uic.loadUi('view/fusion_compute_weights.ui', self)

        self.FCWLaunch = self.findChild(QtWidgets.QPushButton, 'FCWLAUNCH')
        self.FCWLaunch.clicked.connect(lambda: self.run_FCW())

        self.FCWBFILELABEL = self.findChild(QtWidgets.QLabel,
                                            'FCWBFILELABEL')
        self.FCWBFILE = self.findChild(QtWidgets.QPushButton, 'FCWBFILE')
        self.FCWBFILE.clicked.connect(lambda: self.FCWBFILELABEL.setText(
            QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[
                0]))

        self.FCWOUTLABEL = self.findChild(QtWidgets.QLabel, 'FCWOUTLABEL')
        self.FCWOUT = self.findChild(QtWidgets.QPushButton, 'FCWOUT')
        self.FCWOUT.clicked.connect(lambda: self.FCWOUTLABEL.setText(
            QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[
                0]))

        self.FCWTMPLABEL = self.findChild(QtWidgets.QLabel, 'FCWTMPLABEL')
        self.FCWTMP = self.findChild(QtWidgets.QPushButton, 'FCWTMP')
        self.FCWTMP.clicked.connect(lambda: self.FCWTMPLABEL.setText(
            QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[
                0]))

        self.FCWCOVARLABEL = self.findChild(QtWidgets.QLabel,
                                            'FCWCOVARLABEL')
        self.FCWCOVAR = self.findChild(QtWidgets.QPushButton, 'FCWCOVAR')
        self.FCWCOVAR.clicked.connect(lambda: self.FCWCOVARLABEL.setText(
            QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[
                0]))

        self.FCWPATHGCTALABEL = self.findChild(QtWidgets.QLabel,
                                               'FCWPATHGCTALABEL')
        self.FCWPATHGCTA = self.findChild(QtWidgets.QPushButton,
                                          'FCWPATHGCTA')
        self.FCWPATHGCTA.clicked.connect(
            lambda: self.FCWPATHGCTALABEL.setText(
                QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                      '')[0]))

        self.FCWPATHGEMMALABEL = self.findChild(QtWidgets.QLabel,
                                                'FCWPATHGEMMALABEL')
        self.FCWPATHGEMMA = self.findChild(QtWidgets.QPushButton,
                                           'FCWPATHGEMMA')
        self.FCWPATHGEMMA.clicked.connect(
            lambda: self.FCWPATHGEMMALABEL.setText(
                QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                      '')[0]))

        self.FCWPATHPLINKLABEL = self.findChild(QtWidgets.QLabel,
                                                'FCWPATHPLINKLABEL')
        self.FCWPATHPLINK = self.findChild(QtWidgets.QPushButton,
                                           'FCWPATHPLINK')
        self.FCWPATHPLINK.clicked.connect(
            lambda: self.FCWPATHPLINKLABEL.setText(
                QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                      '')[0]))

        self.FCWPATHPHENOLABEL = self.findChild(QtWidgets.QLabel,
                                                'FCWPATHPHENOLABEL')
        self.FCWPATHPHENO = self.findChild(QtWidgets.QPushButton,
                                           'FCWPATHPHENO')
        self.FCWPATHPHENO.clicked.connect(
            lambda: self.FCWPATHPHENOLABEL.setText(
                QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                      '')[0]))

        self.FCWVERBOSE = self.findChild(QtWidgets.QComboBox, 'FCWVERBOSE')

        self.FCWNOCLEAN = self.findChild(QtWidgets.QCheckBox, 'FCWNOCLEAN')

        self.FCWRN = self.findChild(QtWidgets.QCheckBox, 'FCWRN')

        self.FCWSAVEHSQ = self.findChild(QtWidgets.QCheckBox, 'FCWSAVEHSQ')

        self.FCWVERBOSE = self.findChild(QtWidgets.QComboBox, 'FCWVERBOSE')

        self.FCWCROSSVAL = self.findChild(QtWidgets.QLineEdit,
                                          'FCWCROSSVAL')

        self.FCWHSQP = self.findChild(QtWidgets.QLineEdit, 'FCWHSQP')

        self.FCWHSQSET = self.findChild(QtWidgets.QLineEdit, 'FCWHSQSET')

        self.FCWBLUP = self.findChild(QtWidgets.QCheckBox, 'FCWBLUP')

        self.FCWBSLMM = self.findChild(QtWidgets.QCheckBox, 'FCWBSLMM')

        self.FCWENET = self.findChild(QtWidgets.QCheckBox, 'FCWENET')

        self.FCWLASSO = self.findChild(QtWidgets.QCheckBox, 'FCWLASSO')

        self.FCWTOP1 = self.findChild(QtWidgets.QCheckBox, 'FCWTOP1')

    def validateFCW(self):
        comm = "Rscript FUSION.compute_weights.R "
        comm = comm + " --bwfile " + str(self.FCWBFILELABEL.text())
        comm = comm + " --out " + str(self.FCWOUTLABEL.text())
        comm = comm + " --tmp " + str(self.FCWTMPLABEL.text())
        if (str(self.FCWCOVARLABEL.text()) not in ["", "OPTIONAL"]):
            comm = comm + " --covar " + str(self.FCWCOVARLABEL.text())
        comm = comm + " --crossval " + str(self.FCWCROSSVAL.text())
        comm = comm + " --hsq_p " + str(self.FCWHSQP.text())
        if (str(self.FCWHSQSET.text()) not in ["", "OPTIONAL"]):
            comm = comm + " --hsq_set " + str(self.FCWHSQSET.text())
        comm = comm + self.getmodels()
        if (self.FCWNOCLEAN.isChecked()):
            comm = comm + " --noclean ON "
        comm = comm + " --path_gcta " + str(self.FCWPATHGCTALABEL.text())
        comm = comm + " --path_gemma " + str(self.FCWPATHGEMMALABEL.text())
        comm = comm + " --path_plink " + str(self.FCWPATHPLINKLABEL.text())
        if (str(self.FCWPATHPHENOLABEL.text()) not in ["", "OPTIONAL"]):
            comm = comm + " --covar " + str(self.FCWCOVARLABEL.text())
        if (self.FCWRN.isChecked()):
            comm = comm + " --rn ON "
        if (self.FCWSAVEHSQ.isChecked()):
            comm = comm + " --save_hsq ON "
        comm = comm + " --verbose " + str(self.FCWVERBOSE.currentText())
        return (comm)

    def run_FCW(self):

        command = self.validateFCW()
        print(command)

        with open('./methods/FUSION/SRC/fusion_tmp.sh', 'w+') as file:
            file.write('#!/bin/bash\n')
            file.write('cd ..\n')
            file.write(command)

        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()

    def getmodels(self):
        models=[]
        if (self.FCWBLUP.isChecked()):
            models.append('blup')
        if (self.FCWBSLMM.isChecked()):
            models.append('bslmm')
        if (self.FCWENET.isChecked()):
            models.append('enet')
        if (self.FCWLASSO.isChecked()):
            models.append('lasso')
        if (self.FCWTOP1.isChecked()):
            models.append('top1')
        return " --models " + ", ".join(models)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = FusionComputeWeights()
    window.show()
    app.exec_()
