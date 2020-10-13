from PyQt5 import QtWidgets, uic
import sys
import subprocess


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('App_View.ui', self)
        self.show()
        self.initFCW()
        self.initFAT()
        self.initFPP()

    def initFCW(self):
        self.FCWLaunch = self.findChild(QtWidgets.QPushButton, 'FCWLAUNCH')
        self.FCWLaunch.clicked.connect(lambda: self.run_FCW())

        self.FCWBFILELABEL= self.findChild(QtWidgets.QLabel,'FCWBFILELABEL')
        self.FCWBFILE = self.findChild(QtWidgets.QPushButton, 'FCWBFILE')
        self.FCWBFILE.clicked.connect(lambda: self.FCWBFILELABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FCWOUTLABEL= self.findChild(QtWidgets.QLabel,'FCWOUTLABEL')
        self.FCWOUT = self.findChild(QtWidgets.QPushButton, 'FCWOUT')
        self.FCWOUT.clicked.connect(lambda: self.FCWOUTLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FCWTMPLABEL= self.findChild(QtWidgets.QLabel,'FCWTMPLABEL')
        self.FCWTMP = self.findChild(QtWidgets.QPushButton, 'FCWTMP')
        self.FCWTMP.clicked.connect(lambda: self.FCWTMPLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FCWCOVARLABEL= self.findChild(QtWidgets.QLabel,'FCWCOVARLABEL')
        self.FCWCOVAR = self.findChild(QtWidgets.QPushButton, 'FCWCOVAR')
        self.FCWCOVAR.clicked.connect(lambda: self.FCWCOVARLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FCWPATHGCTALABEL= self.findChild(QtWidgets.QLabel,'FCWPATHGCTALABEL')
        self.FCWPATHGCTA = self.findChild(QtWidgets.QPushButton, 'FCWPATHGCTA')
        self.FCWPATHGCTA.clicked.connect(lambda: self.FCWPATHGCTALABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FCWPATHGEMMALABEL= self.findChild(QtWidgets.QLabel,'FCWPATHGEMMALABEL')
        self.FCWPATHGEMMA = self.findChild(QtWidgets.QPushButton, 'FCWPATHGEMMA')
        self.FCWPATHGEMMA.clicked.connect(lambda: self.FCWPATHGEMMALABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FCWPATHPLINKLABEL= self.findChild(QtWidgets.QLabel,'FCWPATHPLINKLABEL')
        self.FCWPATHPLINK = self.findChild(QtWidgets.QPushButton, 'FCWPATHPLINK')
        self.FCWPATHPLINK.clicked.connect(lambda: self.FCWPATHPLINKLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FCWPATHPHENOLABEL= self.findChild(QtWidgets.QLabel,'FCWPATHPHENOLABEL')
        self.FCWPATHPHENO = self.findChild(QtWidgets.QPushButton, 'FCWPATHPHENO')
        self.FCWPATHPHENO.clicked.connect(lambda: self.FCWPATHPHENOLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FCWVERBOSE = self.findChild(QtWidgets.QComboBox,'FCWVERBOSE')

        self.FCWNOCLEAN = self.findChild(QtWidgets.QCheckBox,'FCWNOCLEAN')

        self.FCWRN = self.findChild(QtWidgets.QCheckBox,'FCWRN')

        self.FCWSAVEHSQ = self.findChild(QtWidgets.QCheckBox,'FCWSAVEHSQ')

        self.FCWVERBOSE = self.findChild(QtWidgets.QComboBox,'FCWVERBOSE')

        self.FCWCROSSVAL = self.findChild(QtWidgets.QLineEdit,'FCWCROSSVAL')

        self.FCWHSQP = self.findChild(QtWidgets.QLineEdit,'FCWHSQP')

        self.FCWHSQSET = self.findChild(QtWidgets.QLineEdit,'FCWHSQSET')

        self.FCWBLUP = self.findChild(QtWidgets.QCheckBox, 'FCWBLUP')

        self.FCWBSLMM = self.findChild(QtWidgets.QCheckBox, 'FCWBSLMM')

        self.FCWENET = self.findChild(QtWidgets.QCheckBox, 'FCWENET')

        self.FCWLASSO = self.findChild(QtWidgets.QCheckBox, 'FCWLASSO')

        self.FCWTOP1 = self.findChild(QtWidgets.QCheckBox, 'FCWTOP1')

    def validateFCW(self):
        comm = "Rscript FUSION.compute_weights.R "
        comm = comm + " --bwfile "+str(self.FCWBFILELABEL.text())
        comm = comm + " --out "+str(self.FCWOUTLABEL.text())
        comm = comm + " --tmp "+str(self.FCWTMPLABEL.text())
        if(str(self.FCWCOVARLABEL.text()) not in ["","OPTIONAL"]):
            comm = comm + " --covar "+str(self.FCWCOVARLABEL.text())
        comm = comm + " --crossval " + str(self.FCWCROSSVAL.text())
        comm = comm + " --hsq_p " + str(self.FCWHSQP.text())
        if (str(self.FCWHSQSET.text()) not in ["", "OPTIONAL"]):
            comm = comm + " --hsq_set " + str(self.FCWHSQSET.text())
        comm = comm + self.getmodels()
        if (self.FCWNOCLEAN.isChecked()):
            comm = comm + " --noclean ON "
        comm = comm + " --path_gcta "+str(self.FCWPATHGCTALABEL.text())
        comm = comm + " --path_gemma " + str(self.FCWPATHGEMMALABEL.text())
        comm = comm + " --path_plink " + str(self.FCWPATHPLINKLABEL.text())
        if (str(self.FCWPATHPHENOLABEL.text()) not in ["", "OPTIONAL"]):
            comm = comm + " --covar " + str(self.FCWCOVARLABEL.text())
        if (self.FCWRN.isChecked()):
            comm = comm + " --rn ON "
        if (self.FCWSAVEHSQ.isChecked()):
            comm = comm + " --save_hsq ON "
        comm = comm + " --verbose "+ str(self.FCWVERBOSE.currentText())
        return(comm)

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

    def initFAT(self):
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

    def initFPP(self):
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


    def run_FAT(self):

        command = self.validateFAT()
        print(command)

        with open('./methods/fusion_twas-master/SRC/fusion_tmp.sh', 'w+') as file:
            file.write('#!/bin/bash\n')
            file.write('cd ..\n')
            file.write(command)

        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()

    def run_FCW(self):

        command = self.validateFCW()
        print(command)

        with open('./methods/fusion_twas-master/SRC/fusion_tmp.sh', 'w+') as file:
            file.write('#!/bin/bash\n')
            file.write('cd ..\n')
            file.write(command)

        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()

    def run_FPP(self):

        command = self.validateFPP()
        print(command)

        with open('./methods/fusion_twas-master/SRC/fusion_tmp.sh', 'w+') as file:
            file.write('#!/bin/bash\n')
            file.write('cd ..\n')
            file.write(command)

        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()