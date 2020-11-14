import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic


class FusionPostProcessing(QtWidgets.QWidget):

    def __init__(self):
        super(FusionPostProcessing, self).__init__()
        uic.loadUi('view/fusion_post_processing.ui', self)

        self.FPPLAUNCH = self.findChild(QtWidgets.QPushButton, 'FPPLAUNCH')
        self.FPPLAUNCH.clicked.connect(lambda: self.run_FPP())

        self.FPPCHR = self.findChild(QtWidgets.QLineEdit, 'FPPCHR')

        self.FPPINPUTLABEL = self.findChild(QtWidgets.QLabel, 'FPPINPUTLABEL')
        self.FPPINPUT = self.findChild(QtWidgets.QPushButton, 'FPPINPUT')
        self.FPPINPUT.clicked.connect(
            lambda: self.FPPINPUTLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FPPOUTLABEL = self.findChild(QtWidgets.QLabel, 'FPPOUTLABEL')
        self.FPPOUT = self.findChild(QtWidgets.QPushButton, 'FPPOUT')
        self.FPPOUT.clicked.connect(
            lambda: self.FPPOUTLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FPPREFLDCHRLABEL = self.findChild(QtWidgets.QLabel, 'FPPREFLDCHRLABEL')
        self.FPPREFLDCHR = self.findChild(QtWidgets.QPushButton, 'FPPREFLDCHR')
        self.FPPREFLDCHR.clicked.connect(
            lambda: self.FPPREFLDCHRLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))


        self.FPPSUMSTATSLABEL = self.findChild(QtWidgets.QLabel, 'FPPSUMSTATSLABEL')
        self.FPPSUMSTATS = self.findChild(QtWidgets.QPushButton, 'FPPSUMSTATS')
        self.FPPSUMSTATS.clicked.connect(
            lambda: self.FPPSUMSTATSLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FPPLOCUSWIN = self.findChild(QtWidgets.QLineEdit, 'FPPLOCUSWIN')

        self.FPPMINPINPUT = self.findChild(QtWidgets.QLineEdit, 'FPPMINPINPUT')

        self.FPPMINPJOINT = self.findChild(QtWidgets.QLineEdit, 'FPPMINPJOINT')

        self.FPPMAXR2 = self.findChild(QtWidgets.QLineEdit, 'FPPMAXR2')

        self.FPPMINR2 = self.findChild(QtWidgets.QLineEdit, 'FPPMINR2')


        self.FPPVERBOSE = self.findChild(QtWidgets.QComboBox, 'FPPVERBOSE')


        self.FPPOMNIBUSCORR = self.findChild(QtWidgets.QComboBox, 'FPPOMNIBUSCORR')


        self.FPPLDSC = self.findChild(QtWidgets.QCheckBox, 'FPPLDSC')


        self.FPPOMNIBUS = self.findChild(QtWidgets.QCheckBox,'FPPOMNIBUS')


        self.FPPPLOT = self.findChild(QtWidgets.QCheckBox,'FPPPLOT')

        self.FPPPLOTCORR = self.findChild(QtWidgets.QCheckBox,'FPPPLOTCORR')

        self.FPPPLOTEQTL = self.findChild(QtWidgets.QCheckBox,'FPPPLOTEQTL')

        self.FPPPLOTINDIVIDUAL = self.findChild(QtWidgets.QCheckBox,'FPPPLOTINDIVIDUAL')

        self.FPPPLOTLEGEND = self.findChild(QtWidgets.QCheckBox,'FPPPLOTLEGEND')

        self.FPPPLOTSCATTER = self.findChild(QtWidgets.QCheckBox,'FPPPLOTSCATTER')

        self.FPPREPORT = self.findChild(QtWidgets.QCheckBox,'FPPREPORT')

        self.FPPSAVELOCI = self.findChild(QtWidgets.QCheckBox,'FPPSAVELOCI')

    def validateFPP(self):
        print("abc")
        comm = "Rscript FUSION.post_process.R "
        comm = comm + " --chr " + str(self.FPPCHR.text())
        comm = comm + " --sumstats " + str(self.FPPSUMSTATSLABEL.text())
        comm = comm + " --out " + str(self.FPPOUTLABEL.text())
        comm = comm + " --input " + str(self.FPPINPUTLABEL.text())
        comm = comm + " --ref_ld_chr " + str(self.FPPREFLDCHRLABEL.text())
        if (self.FPPPLOT.isChecked()):
            comm = comm + " --plot "
        if (self.FPPPLOTCORR.isChecked()):
            comm = comm + " --plot_corr "
        if (self.FPPPLOTEQTL.isChecked()):
            comm = comm + " --plot_eqtl "
        if (self.FPPPLOTINDIVIDUAL.isChecked()):
            comm = comm + " --plot_individual "
        if (self.FPPPLOTLEGEND.isChecked()):
            comm = comm + " --plot_legend "
        if (self.FPPPLOTSCATTER.isChecked()):
            comm = comm + " --plot_scatter "
        if (self.FPPREPORT.isChecked()):
            comm = comm + " --report "
        if (self.FPPSAVELOCI.isChecked()):
            comm = comm + " --save_loci "
        if (self.FPPLDSC.isChecked()):
            comm = comm + " --ldsc "
#        if (self.FCWNOCLEAN.isChecked()):
#            comm = comm + " --noclean ON "
        comm = comm + " --locus_win "+str(self.FPPLOCUSWIN.text())
        comm = comm + " --minp_input " + str(self.FPPMINPINPUT.text())
        comm = comm + " --minp_joint " + str(self.FPPMINPJOINT.text())
        comm = comm + " --max_r2 " + str(self.FPPMAXR2.text())
        comm = comm + " --min_r2 " + str(self.FPPMINR2.text())
        comm = comm + " --verbose "+ str(self.FPPVERBOSE.currentText())
        #        comm = comm + " --force_model " + str(self.FATFORCEMODEL.currentText())
        return (comm)

    def run_FPP(self):

        command = self.validateFPP()
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
    window = FusionPostProcessing()
    window.show()
    app.exec_()
