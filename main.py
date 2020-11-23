import io

from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys
import subprocess
from backend import monitor
from threading import Thread

FUSION_DIR = './methods/FUSION'
TIGAR_DIR ='./methods/TIGAR'
METAXCAN_DIR= './methods/METAXCAN/software'


class Ui(QtWidgets.QMainWindow):
    errorSignal = QtCore.pyqtSignal(str)
    outputSignal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('view/App_View.ui', self)
        self.show()
        #FUSION
        self.initFCW()
        self.initFAT()
        self.initFPP()
        #TIGAR
        self.initTMT()
        self.initTGR()
        self.initTTW()
        self.initTCM()
        #PREDIXCAN
        self.initMPX()
        self.initMSP()
        self.initMUL()
        self.initSMX()
        #CONSOLE
        self.initCONS()
        #Proces which is running imputation commands
        self.errorSignal.connect(lambda error: print(error))
        self.outputSignal.connect(lambda output: print(output))
        self.process = QtCore.QProcess()
        self.process.readyReadStandardError.connect(self.onReadyReadStandardError)
        self.process.readyReadStandardOutput.connect(self.onReadyReadStandardOutput)

    def onReadyReadStandardError(self):
        error = self.process.readAllStandardError().data().decode()
        self.CONSSCREEN.appendPlainText(error)
        self.errorSignal.emit(error)

    def onReadyReadStandardOutput(self):
        result = self.process.readAllStandardOutput().data().decode()
        self.CONSSCREEN.appendPlainText(result)
        self.outputSignal.emit(result)

    def __del__(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def initFCW(self):
        self.FCWLaunch = self.findChild(QtWidgets.QPushButton, 'FCWLAUNCH')
        self.FCWLaunch.clicked.connect(lambda: self.run_FCW())

        self.FCWBFILELABEL= self.findChild(QtWidgets.QLabel,'FCWBFILELABEL')
        self.FCWBFILE = self.findChild(QtWidgets.QPushButton, 'FCWBFILE')
        self.FCWBFILE.clicked.connect(lambda: self.FCWBFILELABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.FCWOUTLABEL = self.findChild(QtWidgets.QLabel, 'FCWOUTLABEL')
        self.FCWOUT = self.findChild(QtWidgets.QPushButton, 'FCWOUT')
        self.FCWOUT.clicked.connect(lambda: self.FCWOUTLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

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
        comm = "Rscript ./FUSION.compute_weights.R "
        comm = comm + " --bwfile "+str(self.FCWBFILELABEL.text())
        comm = comm + " --out "+str(self.FCWOUTLABEL.text())+"/"+str(self.FCWOUTFILE.text())
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
            lambda: self.FATOUTLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

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
        comm = "Rscript ./FUSION.assoc_test.R "
        comm = comm + " --sumstats " + str(self.FATSUMSTATSLABEL.text())
        comm = comm + " --out " + str(self.FATOUTLABEL.text())+"/"+str(self.FATOUTFILE.text())
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
            lambda: self.FPPOUTLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

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
        comm = "Rscript ./FUSION.post_process.R "
        comm = comm + " --chr " + str(self.FPPCHR.text())
        comm = comm + " --sumstats " + str(self.FPPSUMSTATSLABEL.text())
        comm = comm + " --out " + str(self.FPPOUTLABEL.text())+"/"+str(self.FPPOUTFILE.text())
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

    def initTMT(self):
        self.TMTLAUNCH = self.findChild(QtWidgets.QPushButton, 'TMTLAUNCH')
        self.TMTLAUNCH.clicked.connect(lambda: self.runTMT())

        self.TMTGEXPLABEL = self.findChild(QtWidgets.QLabel, 'TMTGEXPLABEL')
        self.TMTGEXP = self.findChild(QtWidgets.QPushButton, 'TMTGEXP')
        self.TMTGEXP.clicked.connect(
            lambda: self.TMTGEXPLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.TMTIDLABEL = self.findChild(QtWidgets.QLabel, 'TMTIDLABEL')
        self.TMTID = self.findChild(QtWidgets.QPushButton, 'TMTID')
        self.TMTID.clicked.connect(
            lambda: self.TMTIDLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))


        self.TMTGENFILELABEL = self.findChild(QtWidgets.QLabel, 'TMTGENFILELABEL')
        self.TMTGENFILE = self.findChild(QtWidgets.QPushButton, 'TMTGENFILE')
        self.TMTGENFILE.clicked.connect(
            lambda: self.TMTGENFILELABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))


        self.TMTOUTLABEL = self.findChild(QtWidgets.QLabel, 'TMTOUTLABEL')
        self.TMTOUT = self.findChild(QtWidgets.QPushButton, 'TMTOUT')
        self.TMTOUT.clicked.connect(
            lambda: self.TMTOUTLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.TMTMODEL = self.findChild(QtWidgets.QComboBox, 'TMTMODEL')

        self.TMTGENTYPE = self.findChild(QtWidgets.QComboBox, 'TMTGENTYPE')

        self.TMTDPR = self.findChild(QtWidgets.QComboBox, 'TMTDPR')

        self.TMTES = self.findChild(QtWidgets.QComboBox, 'TMTES')

        self.TMTGENFORMAT = self.findChild(QtWidgets.QComboBox, 'TMTGENFORMAT')

        self.TMTCHR = self.findChild(QtWidgets.QLineEdit, 'TMTCHR')
        self.TMTCV = self.findChild(QtWidgets.QLineEdit, 'TMTCV')
        self.TMTALPHA = self.findChild(QtWidgets.QLineEdit, 'TMTALPHA')
        self.TMTMAF = self.findChild(QtWidgets.QLineEdit, 'TMTMAF')
        self.TMTHWE = self.findChild(QtWidgets.QLineEdit, 'TMTHWE')
        self.TMTTHREAD = self.findChild(QtWidgets.QLineEdit, 'TMTTHREAD')
        self.TMTWINDOW = self.findChild(QtWidgets.QLineEdit, 'TMTWINDOW')
        self.TMTOUTFILE = self.findChild(QtWidgets.QLineEdit, 'TMTOUTFILE')

    def validateTMT(self):
        comm = "./TIGAR_Model_Train.sh "
        comm = comm + " --model " + str(self.TMTMODEL.currentText())
        comm = comm + " --Format " + str(self.TMTGENFORMAT.currentText())
        #DPF
        if (self.TMTMODEL.currentText() == "DPR"):
            comm = comm + " --dpr " + str(self.TMTDPR.currentText())
            comm = comm + " --ES " + str(self.TMTES.currentText())

        #Elastic net
        if (self.TMTMODEL.currentText() == "elastic_net"):
            comm = comm + " --cv " + str(self.TMTCV.text())
            comm = comm + " --alpha " + str(self.TMTALPHA.text())

        comm = comm + " --maf " + str(self.TMTMAF.text())
        comm = comm + " --hwe " + str(self.TMTHWE.text())
        comm = comm + " --thread " + str(self.TMTTHREAD.text())
        comm = comm + " --window " + str(self.TMTWINDOW.text())
        comm = comm + " --genofile_type " + str(self.TMTGENTYPE.currentText())
        comm = comm + " --chr " + str(self.TMTCHR.text())
        comm = comm + " --Gene_Exp " + str(self.TMTGEXPLABEL.text())
        comm = comm + " --sampleID " + str(self.TMTIDLABEL.text())
        comm = comm + " --genofile " + str(self.TMTGENFILELABEL.text())
        comm = comm + " --out " + str(self.TMTOUTLABEL.text())+"/"+str(self.TMTOUTFILE.text())

        return (comm)

    def initTGR(self):
        self.TGRLAUNCH = self.findChild(QtWidgets.QPushButton, 'TGRLAUNCH')
        self.TGRLAUNCH.clicked.connect(lambda: self.runTGR())

        self.TGRWEIGHTLABEL = self.findChild(QtWidgets.QLabel, 'TGRWEIGHTLABEL')
        self.TGRWEIGHT = self.findChild(QtWidgets.QPushButton, 'TGRWEIGHT')
        self.TGRWEIGHT.clicked.connect(
            lambda: self.TGRWEIGHTLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.TGRIDLABEL = self.findChild(QtWidgets.QLabel, 'TGRIDLABEL')
        self.TGRID = self.findChild(QtWidgets.QPushButton, 'TGRID')
        self.TGRID.clicked.connect(
            lambda: self.TGRIDLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.TGRINFOLABEL = self.findChild(QtWidgets.QLabel, 'TGRINFOLABEL')
        self.TGRINFO = self.findChild(QtWidgets.QPushButton, 'TGRINFO')
        self.TGRINFO.clicked.connect(
            lambda: self.TGRINFOLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))


        self.TGRGENLABEL = self.findChild(QtWidgets.QLabel, 'TGRGENLABEL')
        self.TGRGEN = self.findChild(QtWidgets.QPushButton, 'TGRGEN')
        self.TGRGEN.clicked.connect(
            lambda: self.TGRGENLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.TGROUTLABEL = self.findChild(QtWidgets.QLabel, 'TGROUTLABEL')
        self.TGROUT = self.findChild(QtWidgets.QPushButton, 'TGROUT')
        self.TGROUT.clicked.connect(
            lambda: self.TGROUTLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.TGRMODEL = self.findChild(QtWidgets.QComboBox, 'TGRMODEL')

        self.TGRGENTYPE = self.findChild(QtWidgets.QComboBox, 'TGRGENTYPE')

        self.TGRFORMAT = self.findChild(QtWidgets.QComboBox, 'TGRFORMAT')

        self.TGRCHR = self.findChild(QtWidgets.QLineEdit, 'TGRCHR')
        self.TGRMAF = self.findChild(QtWidgets.QLineEdit, 'TGRMAF')
        self.TGRTHREAD = self.findChild(QtWidgets.QLineEdit, 'TGRTHREAD')
        self.TGRWINDOW = self.findChild(QtWidgets.QLineEdit, 'TGRWINDOW')
        self.TGROUTFILE = self.findChild(QtWidgets.QLineEdit, 'TGROUTFILE')

    def validateTGR(self):
        comm = "./TIGAR_Model_Pred.sh "
        comm = comm + " --model " + str(self.TGRMODEL.currentText())
        comm = comm + " --Format " + str(self.TGRFORMAT.currentText())
        comm = comm + " --genofile_type " + str(self.TGRGENTYPE.currentText())


        comm = comm + " --maf_diff " + str(self.TGRMAF.text())
        comm = comm + " --thread " + str(self.TGRTHREAD.text())
        comm = comm + " --window " + str(self.TGRWINDOW.text())
        comm = comm + " --chr " + str(self.TGRCHR.text())

        comm = comm + " --train_weight_path " + str(self.TGRWEIGHTLABEL.text())
        comm = comm + " --sampleID " + str(self.TGRIDLABEL.text())
        comm = comm + " --train_info_path " + str(self.TGRINFOLABEL.text())
        comm = comm + " --genofile " + str(self.TGRGENLABEL.text())

        comm = comm + " --out " + str(self.TGROUTLABEL.text()) + "/" + str(self.TGROUTFILE.text())

        return (comm)

    def initTTW(self):
        self.TTWLAUNCH = self.findChild(QtWidgets.QPushButton, 'TTWLAUNCH')
        self.TTWLAUNCH.clicked.connect(lambda: self.runTTW())

        self.TTWWEIGHTLABEL = self.findChild(QtWidgets.QLabel, 'TTWWEIGHTLABEL')
        self.TTWWEIGHT = self.findChild(QtWidgets.QPushButton, 'TTWWEIGHT')
        self.TTWWEIGHT.clicked.connect(
            lambda: self.TTWWEIGHTLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.TTWCOVARLABEL = self.findChild(QtWidgets.QLabel, 'TTWCOVARLABEL')
        self.TTWCOVAR = self.findChild(QtWidgets.QPushButton, 'TTWCOVAR')
        self.TTWCOVAR.clicked.connect(
            lambda: self.TTWCOVARLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.TTWZSCORELABEL = self.findChild(QtWidgets.QLabel, 'TTWZSCORELABEL')
        self.TTWZSCORE= self.findChild(QtWidgets.QPushButton, 'TTWZSCORE')
        self.TTWZSCORE.clicked.connect(
            lambda: self.TTWZSCORELABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.TTWGENLABEL = self.findChild(QtWidgets.QLabel, 'TTWGENLABEL')
        self.TTWGEN = self.findChild(QtWidgets.QPushButton, 'TTWGEN')
        self.TTWGEN.clicked.connect(
            lambda: self.TTWGENLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.TTWASSOLABEL = self.findChild(QtWidgets.QLabel, 'TTWASSOLABEL')
        self.TTWASSO = self.findChild(QtWidgets.QPushButton, 'TTWASSO')
        self.TTWASSO.clicked.connect(
            lambda: self.TTWASSOLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.TTWPEDLABEL = self.findChild(QtWidgets.QLabel, 'TTWPEDLABEL')
        self.TTWPED = self.findChild(QtWidgets.QPushButton, 'TTWPED')
        self.TTWPED.clicked.connect(
            lambda: self.TTWPEDLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.TTWOUTLABEL = self.findChild(QtWidgets.QLabel, 'TTWOUTLABEL')
        self.TTWOUT = self.findChild(QtWidgets.QPushButton, 'TTWOUT')
        self.TTWOUT.clicked.connect(
            lambda: self.TTWOUTLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))



        self.TTWASSOC = self.findChild(QtWidgets.QComboBox, 'TTWASSOC')

        self.TTWMETHOD = self.findChild(QtWidgets.QComboBox, 'TTWMETHOD')

        self.TTWCHR = self.findChild(QtWidgets.QLineEdit, 'TTWCHR')
        self.TTWTHREAD = self.findChild(QtWidgets.QLineEdit, 'TTWTHREAD')
        self.TTWWINDOW = self.findChild(QtWidgets.QLineEdit, 'TTWWINDOW')
        self.TTWOUTFILE = self.findChild(QtWidgets.QLineEdit, 'TTWOUTFILE')

    def validateTTW(self):
        comm = "./TIGAR_TWAS.sh "
        comm = comm + " --asso " + str(self.TTWASSOC.currentText())
        comm = comm + " --thread " + str(self.TTWTHREAD.text())
        comm = comm + " --Gene_Exp " + str(self.TTWGENLABEL.text())
        comm = comm + " --out " + str(self.TTWOUTLABEL.text()) + "/" + str(self.TTWOUTFILE.text())

        if (self.TTWASSOC.currentText() == "1"):
            comm = comm + " --method " + str(self.TTWMETHOD.currentText())
            comm = comm + " --PED " + str(self.TTWWEIGHTLABEL.text())
            comm = comm + " --Asso_Info " + str(self.TTWCOVARLABEL.text())

        #Elastic net
        if (self.TTWASSOC.currentText() == "2"):
            comm = comm + " --Weight " + str(self.TTWWEIGHTLABEL.text())
            comm = comm + " --Covar " + str(self.TTWCOVARLABEL.text())
            comm = comm + " --Zscore" + str(self.TTWZSCORELABEL.text())
            comm = comm + " --window " + str(self.TTWWINDOW.text())
            comm = comm + " --chr " + str(self.TTWCHR.text())


        return (comm)

    def initTCM(self):
        self.TCMLAUNCH = self.findChild(QtWidgets.QPushButton, 'TCMLAUNCH')
        self.TCMLAUNCH.clicked.connect(lambda: self.runTCM())

        self.TCMBLOCKLABEL = self.findChild(QtWidgets.QLabel, 'TCMBLOCKLABEL')
        self.TCMBLOCK = self.findChild(QtWidgets.QPushButton, 'TCMBLOCK')
        self.TCMBLOCK.clicked.connect(
            lambda: self.TCMBLOCKLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.TCMGENFILELABEL = self.findChild(QtWidgets.QLabel, 'TCMGENFILELABEL')
        self.TCMGENFILE = self.findChild(QtWidgets.QPushButton, 'TCMGENFILE')
        self.TCMGENFILE.clicked.connect(
            lambda: self.TCMGENFILELABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.TCMOUTLABEL = self.findChild(QtWidgets.QLabel, 'TCMOUTLABEL')
        self.TCMOUT = self.findChild(QtWidgets.QPushButton, 'TCMOUT')
        self.TCMOUT.clicked.connect(
            lambda: self.TCMOUTLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.TCMGENTYPE = self.findChild(QtWidgets.QComboBox, 'TCMGENTYPE')

        self.TCMCHR = self.findChild(QtWidgets.QLineEdit, 'TCMCHR')

        self.TCMOUTFILE = self.findChild(QtWidgets.QLineEdit, 'TCMOUTFILE')

        self.TCMGENFORMAT = self.findChild(QtWidgets.QComboBox, 'TCMGENFORMAT')

        self.TCMMAF = self.findChild(QtWidgets.QLineEdit, 'TCMMAF')

    def validateTCM(self):
        comm = "./TIGAR_Covar.sh "
        comm = comm + " --block " + str(self.TCMBLOCKLABEL.text())
        comm = comm + " --genofile " + str(self.TCMGENFILELABEL.text())
        comm = comm + " --out " + str(self.TCMOUTLABEL.text()) + "/" + str(self.TCMOUTFILE.text())

        comm = comm + " --Format " + str(self.TCMGENFORMAT.currentText())
        comm = comm + " --maf " + str(self.TCMMAF.text())
        comm = comm + " --genofile_type " + str(self.TCMGENTYPE.currentText())
        comm = comm + " --chr " + str(self.TCMCHR.text())

        return (comm)

    def initMPX(self):
        self.MPXLAUNCH = self.findChild(QtWidgets.QPushButton, 'MPXLAUNCH')
        self.MPXLAUNCH.clicked.connect(lambda: self.runMPX())

        self.MPXDBKEY = self.findChild(QtWidgets.QLineEdit, 'MPXDBKEY')
        self.MPXGENERATE = self.findChild(QtWidgets.QLineEdit, 'MPXGENERATE')
        self.MPXPREDOUTFILE = self.findChild(QtWidgets.QLineEdit, 'MPXPREDOUTFILE')
        self.MPXSUMOUTFILE = self.findChild(QtWidgets.QLineEdit, 'MPXSUMOUTFILE')
        self.MPXPHENCOL = self.findChild(QtWidgets.QLineEdit, 'MPXPHENCOL')
        self.MPXCOVAR = self.findChild(QtWidgets.QLineEdit, 'MPXCOVAR')
        self.MPXVER = self.findChild(QtWidgets.QLineEdit, 'MPXVER')
        self.MPXOUTFILE = self.findChild(QtWidgets.QLineEdit, 'MPXOUTFILE')

        self.MPXVCFMODE = self.findChild(QtWidgets.QComboBox, 'MPXVCFMODE')

        self.MPXMODE = self.findChild(QtWidgets.QComboBox, 'MPXMODE')


        self.MPXDBPATHLABEL = self.findChild(QtWidgets.QLabel, 'MPXDBPATHLABEL')
        self.MPXDBPATH = self.findChild(QtWidgets.QPushButton, 'MPXDBPATH')
        self.MPXDBPATH.clicked.connect(
            lambda: self.MPXDBPATHLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MPXLIFTLABEL = self.findChild(QtWidgets.QLabel, 'MPXLIFTLABEL')
        self.MPXLIFT = self.findChild(QtWidgets.QPushButton, 'MPXLIFT')
        self.MPXLIFT.clicked.connect(
            lambda: self.MPXLIFTLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MPXVCFLABEL = self.findChild(QtWidgets.QLabel, 'MPXVCFLABEL')
        self.MPXVCF = self.findChild(QtWidgets.QPushButton, 'MPXVCF')
        self.MPXVCF.clicked.connect(
            lambda: self.MPXVCFLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MPXTXTLABEL = self.findChild(QtWidgets.QLabel, 'MPXTXTLABEL')
        self.MPXTXT = self.findChild(QtWidgets.QPushButton, 'MPXTXT')
        self.MPXTXT.clicked.connect(
            lambda: self.MPXTXTLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MPXPHENLABEL = self.findChild(QtWidgets.QLabel, 'MPXPHENLABEL')
        self.MPXPHEN = self.findChild(QtWidgets.QPushButton, 'MPXPHEN')
        self.MPXPHEN.clicked.connect(
            lambda: self.MPXPHENLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MPXCOVLABEL = self.findChild(QtWidgets.QLabel, 'MPXCOVLABEL')
        self.MPXCOV = self.findChild(QtWidgets.QPushButton, 'MPXCOV')
        self.MPXCOV.clicked.connect(
            lambda: self.MPXCOVLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MPXTXTIDLABEL = self.findChild(QtWidgets.QLabel, 'MPXTXTIDLABEL')
        self.MPXTXTID = self.findChild(QtWidgets.QPushButton, 'MPXTXTID')
        self.MPXTXTID.clicked.connect(
            lambda: self.MPXTXTIDLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MPXBGENLABEL = self.findChild(QtWidgets.QLabel, 'MPXBGENLABEL')
        self.MPXBGEN = self.findChild(QtWidgets.QPushButton, 'MPXBGEN')
        self.MPXBGEN.clicked.connect(
            lambda: self.MPXBGENLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MPXPREDOUTLABEL = self.findChild(QtWidgets.QLabel, 'MPXPREDOUTLABEL')
        self.MPXPREDOUT = self.findChild(QtWidgets.QPushButton, 'MPXPREDOUT')
        self.MPXPREDOUT.clicked.connect(
            lambda: self.MPXPREDOUTLABEL.setText(
                QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.MPXSUMOUTLABEL = self.findChild(QtWidgets.QLabel, 'MPXSUMOUTLABEL')
        self.MPXSUMOUT = self.findChild(QtWidgets.QPushButton, 'MPXSUMOUT')
        self.MPXSUMOUT.clicked.connect(
            lambda: self.MPXSUMOUTLABEL.setText(
                QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.MPXOUTLABEL = self.findChild(QtWidgets.QLabel, 'MPXOUTLABEL')
        self.MPXOUT = self.findChild(QtWidgets.QPushButton, 'MPXOUT')
        self.MPXOUT.clicked.connect(
            lambda: self.MPXOUTLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.MPXZEROPOS = self.findChild(QtWidgets.QCheckBox, 'MPXZEROPOS')
        self.MPXSKIP = self.findChild(QtWidgets.QCheckBox, 'MPXSKIP')
        self.MPXCOLON = self.findChild(QtWidgets.QCheckBox, 'MPXCOLON')
        self.MPXMAPPED = self.findChild(QtWidgets.QCheckBox, 'MPXMAPPED')
        self.MPXBGENRSID = self.findChild(QtWidgets.QCheckBox, 'MPXBGENRSID')
        self.MPXTHROW = self.findChild(QtWidgets.QCheckBox, 'MPXTHROW')

    def validateMPX(self):
        comm = "./PrediXcan.py "
        comm = comm + " --model_db_path " + str(self.MPXDBPATHLABEL.text())
        if(str(self.MPXLIFTLABEL.text()) not in [""]):
            comm = comm + " --liftover " + str(self.MPXLIFTLABEL.text())
        if(str(self.MPXDBKEY.text()) not in [""]):
            comm = comm + " --model_db_snp_key " + str(self.MPXDBKEY.text())
        if (self.MPXZEROPOS.isChecked()):
            comm = comm + " --zero_based_positions "
        if (self.MPXSKIP.isChecked()):
            comm = comm + " --skip_palindromic "
        if (str(self.MPXBGENLABEL.text()) not in [""]):
            comm = comm + " --bgen_genotypes " + str(self.MPXBGENLABEL.text())
            if (self.MPXBGENRSID.isChecked()):
                comm = comm + " --bgen_use_rsid "
        if (str(self.MPXVCFLABEL.text()) not in [""]):
            comm = comm + " --vcf_genotypes " + str(self.MPXVCFLABEL.text())
            comm = comm + " --vcf_mode "+str(self.MPXVCFMODE.currentText())
        if (self.MPXMAPPED.isChecked()):
            comm = comm + " --force_mapped_metadata "
        if (self.MPXCOLON.isChecked()):
            comm = comm + " --force_colon "
        if (str(self.MPXTXTLABEL.text()) not in [""]):
            comm = comm + " --text_genotypes " + str(self.MPXTXTLABEL.text())
            if (str(self.MPXTXTIDLABEL.text()) not in [""]):
                comm = comm + " --text_sample_ids " + str(self.MPXTXTIDLABEL.text())
        if (str(self.MPXGENERATE.text()) not in [""]):
            comm = comm + " --generate_sample_ids " + str(self.MPXTXTLABEL.text())

        if (str(self.MPXPREDOUTFILE.text()) not in [""]):
            comm = comm + " --prediction_output " + str(self.MPXPREDOUTLABEL.text()) + "/" + str(
                self.MPXPREDOUTFILE.text())

        if (str(self.MPXSUMOUTFILE.text()) not in [""]):
            comm = comm + " --prediction_summary_output " + str(self.MPXSUMOUTLABEL.text()) + "/" + str(
                self.MPXSUMOUTFILE.text())

        comm = comm + " --input_phenos_file " + str(self.MPXPHENLABEL.text())
        comm = comm + " --input_phenos_column " + str(self.MPXPHENCOL.text())

        comm = comm + " --covariates_file " + str(self.MPXCOVLABEL.text())
        comm = comm + " --covariates " + str(self.MPXCOVAR.text())

        comm = comm + " --output " + str(self.MPXOUTLABEL.text())+ "/" + str(self.MPXOUTFILE.text())
        comm = comm + " --verbosity " + str(self.MPXVER.text())
        comm = comm + " --mode " + str(self.MPXMODE.currentText())
        if (self.MPXTHROW.isChecked()):
            comm = comm + " --throw "

        return (comm)

    def initMSP(self):
        self.MSPLAUNCH = self.findChild(QtWidgets.QPushButton, 'MSPLAUNCH')
        self.MSPLAUNCH.clicked.connect(lambda: self.runMSP())

        self.MSPDBKEY = self.findChild(QtWidgets.QLineEdit, 'MSPDBKEY')
        self.MSPGWASPAT = self.findChild(QtWidgets.QLineEdit, 'MSPGWASPAT')
        self.MSPMAXR = self.findChild(QtWidgets.QLineEdit, 'MSPMAXR')
        self.MSPVER = self.findChild(QtWidgets.QLineEdit, 'MSPVER')
        self.MSPOUTFILE = self.findChild(QtWidgets.QLineEdit, 'MSPOUTFILE')

        self.MSPSNP = self.findChild(QtWidgets.QLineEdit, 'MSPSNP')
        self.MSPEFF = self.findChild(QtWidgets.QLineEdit, 'MSPEFF')
        self.MSPNON = self.findChild(QtWidgets.QLineEdit, 'MSPNON')
        self.MSPBETA = self.findChild(QtWidgets.QLineEdit, 'MSPBETA')
        self.MSPSIGN = self.findChild(QtWidgets.QLineEdit, 'MSPSIGN')
        self.MSPOR = self.findChild(QtWidgets.QLineEdit, 'MSPOR')
        self.MSPZSCORE = self.findChild(QtWidgets.QLineEdit, 'MSPZSCORE')
        self.MSPPVAL = self.findChild(QtWidgets.QLineEdit, 'MSPPVAL')
        self.MSPSEP = self.findChild(QtWidgets.QLineEdit, 'MSPSEP')

        self.MSPDBPATHLABEL = self.findChild(QtWidgets.QLabel, 'MSPDBPATHLABEL')
        self.MSPDBPATH = self.findChild(QtWidgets.QPushButton, 'MSPDBPATH')
        self.MSPDBPATH.clicked.connect(
            lambda: self.MSPDBPATHLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MSPGWASFILELABEL = self.findChild(QtWidgets.QLabel, 'MSPGWASFILELABEL')
        self.MSPGWASFILE = self.findChild(QtWidgets.QPushButton, 'MSPGWASFILE')
        self.MSPGWASFILE.clicked.connect(
            lambda: self.MSPGWASFILELABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MSPCOVLABEL = self.findChild(QtWidgets.QLabel, 'MSPCOVLABEL')
        self.MSPCOV = self.findChild(QtWidgets.QPushButton, 'MSPCOV')
        self.MSPCOV.clicked.connect(
            lambda: self.MSPCOVLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MSPGWASFOLDERLABEL = self.findChild(QtWidgets.QLabel, 'MSPGWASFOLDERLABEL')
        self.MSPGWASFOLDER = self.findChild(QtWidgets.QPushButton, 'MSPGWASFOLDER')
        self.MSPGWASFOLDER.clicked.connect(
            lambda: self.MSPGWASFOLDERLABEL.setText(
                QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.MSPOUTLABEL = self.findChild(QtWidgets.QLabel, 'MSPOUTLABEL')
        self.MSPOUT = self.findChild(QtWidgets.QPushButton, 'MSPOUT')
        self.MSPOUT.clicked.connect(
            lambda: self.MSPOUTLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.MSPSINGLE = self.findChild(QtWidgets.QCheckBox, 'MSPSINGLE')
        self.MSPREMOVE = self.findChild(QtWidgets.QCheckBox, 'MSPREMOVE')
        self.MSPOERWRITE = self.findChild(QtWidgets.QCheckBox, 'MSPOERWRITE')
        self.MSPADDITIONAL = self.findChild(QtWidgets.QCheckBox, 'MSPADDITIONAL')
        self.MSPSTREAM = self.findChild(QtWidgets.QCheckBox, 'MSPSTREAM')
        self.MSPTHROW = self.findChild(QtWidgets.QCheckBox, 'MSPTHROW')

    def validateMSP(self):
            comm = "./SPrediXcan.py "
            comm = comm + " --model_db_path " + str(self.MSPDBPATHLABEL.text())
            if (str(self.MSPGWASFILELABEL.text()) not in [""]):
                comm = comm + " --gwas_file " + str(self.MSPGWASFILELABEL.text())
            if (str(self.MSPDBKEY.text()) not in [""]):
                comm = comm + " --model_db_snp_key " + str(self.MSPDBKEY.text())
            if (self.MSPSINGLE.isChecked()):
                comm = comm + " --single_snp_model "
            if (self.MSPREMOVE.isChecked()):
                comm = comm + " --remove_ens_version "
            if (self.MSPSTREAM.isChecked()):
                comm = comm + " --stream_covariance "
            if (str(self.MSPCOVLABEL.text()) not in [""]):
                comm = comm + " --covariance " + str(self.MSPCOVLABEL.text())
            if (self.MSPADDITIONAL.isChecked()):
                comm = comm + " --additional_output "
            if (self.MSPOERWRITE.isChecked()):
                comm = comm + " --overwrite "
            if (str(self.MSPMAXR.text()) not in [""]):
                comm = comm + " --MAX_R " + str(self.MSPMAXR.text())
            if (str(self.MSPGWASFOLDERLABEL.text()) not in [""]):
                comm = comm + " --gwas_folder " + str(self.MSPGWASFOLDERLABEL.text())
                if (str(self.MSPGWASPAT.text()) not in [""]):
                    comm = comm + " --gwas_file_pattern " + str(self.MSPGWASPAT.text())
            comm = comm + " --output " + str(self.MSPOUTLABEL.text()) + "/" + str(self.MSPOUTFILE.text())
            comm = comm + " --verbosity " + str(self.MSPVER.text())
            if (self.MSPTHROW.isChecked()):
                comm = comm + " --throw "
            if (str(self.MSPSNP.text()) not in [""]):
                comm = comm + " --snp_column " + str(self.MSPSNP.text())
            if (str(self.MSPEFF.text()) not in [""]):
                comm = comm + " --effect_allele_column " + str(self.MSPEFF.text())
            if (str(self.MSPNON.text()) not in [""]):
                comm = comm + " --non_effect_allele_column " + str(self.MSPNON.text())
            if (str(self.MSPBETA.text()) not in [""]):
                comm = comm + " --beta_column " + str(self.MSPBETA.text())
            if (str(self.MSPSIGN.text()) not in [""]):
                comm = comm + " --beta_sign_column " + str(self.MSPSIGN.text())
            if (str(self.MSPOR.text()) not in [""]):
                comm = comm + " --or_column " + str(self.MSPOR.text())
            if (str(self.MSPZSCORE.text()) not in [""]):
                comm = comm + " --zscore_column " + str(self.MSPZSCORE.text())
            if (str(self.MSPPVAL.text()) not in [""]):
                comm = comm + " --pvalue_column " + str(self.MSPPVAL.text())
            if (str(self.MSPSEP.text()) not in [""]):
                comm = comm + " --separator " + str(self.MSPSEP.text())

            return (comm)

    def initCONS(self):
        self.CONSCANCEL = self.findChild(QtWidgets.QPushButton, 'CONSCANCEL')
        self.CONSCANCEL.clicked.connect(lambda: self.runCancel())
        self.CONSSCREEN = self.findChild(QtWidgets.QPlainTextEdit, 'CONSSCREEN')
        self.cancel_command = 'None'



    def initMUL(self):
        self.MULLAUNCH = self.findChild(QtWidgets.QPushButton, 'MULLAUNCH')
        self.MULLAUNCH.clicked.connect(lambda: self.runMUL())

        self.MULPAT = self.findChild(QtWidgets.QLineEdit, 'MULPAT')
        self.MULPHENVAL = self.findChild(QtWidgets.QLineEdit, 'MULPHENVAL')
        self.MULCOEFFFILE = self.findChild(QtWidgets.QLineEdit, 'MULCOEFFFILE')
        self.MULLOADFILE = self.findChild(QtWidgets.QLineEdit, 'MULLOADFILE')
        self.MULPHENCOL = self.findChild(QtWidgets.QLineEdit, 'MULPHENCOL')
        self.MULCOVAR = self.findChild(QtWidgets.QLineEdit, 'MULCOVAR')
        self.MULVER = self.findChild(QtWidgets.QLineEdit, 'MULVER')
        self.MULOUTFILE = self.findChild(QtWidgets.QLineEdit, 'MULOUTFILE')

        self.MULPHENVAL = self.findChild(QtWidgets.QLineEdit, 'MULPHENVAL')
        self.MULMAXM = self.findChild(QtWidgets.QLineEdit, 'MULMAXM')
        self.MULCOND = self.findChild(QtWidgets.QLineEdit, 'MULCOND')
        self.MULEIG = self.findChild(QtWidgets.QLineEdit, 'MULEIG')

        self.MULMODE = self.findChild(QtWidgets.QComboBox, 'MULMODE')

        self.MULPHENLABEL = self.findChild(QtWidgets.QLabel, 'MULPHENLABEL')
        self.MULPHEN = self.findChild(QtWidgets.QPushButton, 'MULPHEN')
        self.MULPHEN.clicked.connect(
            lambda: self.MULPHENLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MULCOVLABEL = self.findChild(QtWidgets.QLabel, 'MULCOVLABEL')
        self.MULCOV = self.findChild(QtWidgets.QPushButton, 'MULCOV')
        self.MULCOV.clicked.connect(
            lambda: self.MULCOVLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.MULCOEFFLABEL = self.findChild(QtWidgets.QLabel, 'MULCOEFFLABEL')
        self.MULCOEFF = self.findChild(QtWidgets.QPushButton, 'MULCOEFF')
        self.MULCOEFF.clicked.connect(
            lambda: self.MULCOEFFLABEL.setText(
                QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.MULLOADLABEL = self.findChild(QtWidgets.QLabel, 'MULLOADLABEL')
        self.MULLOAD = self.findChild(QtWidgets.QPushButton, 'MULLOAD')
        self.MULLOAD.clicked.connect(
            lambda: self.MULLOADLABEL.setText(
                QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.MULOUTLABEL = self.findChild(QtWidgets.QLabel, 'MULOUTLABEL')
        self.MULOUT = self.findChild(QtWidgets.QPushButton, 'MULOUT')
        self.MULOUT.clicked.connect(
            lambda: self.MULOUTLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.MULEXLABEL = self.findChild(QtWidgets.QLabel, 'MULEXLABEL')
        self.MULEX = self.findChild(QtWidgets.QPushButton, 'MULEX')
        self.MULEX.clicked.connect(
            lambda: self.MULEXLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.MULHDFLABEL = self.findChild(QtWidgets.QLabel, 'MULHDFLABEL')
        self.MULHDF = self.findChild(QtWidgets.QPushButton, 'MULHDF')
        self.MULHDF.clicked.connect(
            lambda: self.MULHDFLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.MULMEM = self.findChild(QtWidgets.QCheckBox, 'MULMEM')
        self.MULSTAND = self.findChild(QtWidgets.QCheckBox, 'MULSTAND')
        self.MULCODE = self.findChild(QtWidgets.QCheckBox, 'MULCODE')
        self.MULTHROW = self.findChild(QtWidgets.QCheckBox, 'MULTHROW')

    def validateMUL(self):
        comm = "./MulTiXcan.py "
        if (str(self.MULEXLABEL.text()) not in [""]):
            comm = comm + " --expression_folder " + str(self.MULEXLABEL.text())
        if (str(self.MULHDFLABEL.text()) not in [""]):
            comm = comm + " --hdf5_expression_folder " + str(self.MULHDFLABEL.text())
        if (str(self.MULPAT.text()) not in [""]):
            comm = comm + " --expression_pattern " + str(self.MULPAT.text())
        if (self.MULMEM.isChecked()):
            comm = comm + " --memory_efficient "
        if (self.MULSTAND.isChecked()):
            comm = comm + " --standardize_expression "
        if (self.MULCODE.isChecked()):
            comm = comm + " --code_999 "
        if (str(self.MULCOEFFFILE.text()) not in [""]):
            comm = comm + " --coefficient_output " + str(self.MULCOEFFLABEL.text()) + "/" + str(
                self.MULCOEFFFILE.text())
        if (str(self.MULLOADFILE.text()) not in [""]):
            comm = comm + " --loadings_output " + str(self.MULLOADLABEL.text()) + "/" + str(
                self.MULLOADFILE.text())

        comm = comm + " --output " + str(self.MULOUTLABEL.text()) + "/" + str(self.MULOUTFILE.text())

        comm = comm + " --input_phenos_file " + str(self.MULPHENLABEL.text())
        comm = comm + " --input_phenos_column " + str(self.MULPHENCOL.text())
        if (str(self.MULPHENVAL.text()) not in [""]):
            comm = comm + " --input_phenos_na_values " + str(self.MULPHENVAL.text())


        comm = comm + " --covariates_file " + str(self.MULCOVLABEL.text())
        comm = comm + " --covariates " + str(self.MULCOVAR.text())

        if (str(self.MULMAXM.text()) not in [""]):
            comm = comm + " --MAX_M " + str(self.MULMAXM.text())
        if (str(self.MULCOND.text()) not in [""]):
            comm = comm + " --pc_condition_number " + str(self.MULCOND.text())
        if (str(self.MULEIG.text()) not in [""]):
            comm = comm + " --pc_eigen_ratio " + str(self.MULEIG.text())

        comm = comm + " --verbosity " + str(self.MULVER.text())
        comm = comm + " --mode " + str(self.MULMODE.currentText())
        if (self.MULTHROW.isChecked()):
            comm = comm + " --throw "

        return (comm)

    def initSMX(self):
        self.SMXLAUNCH = self.findChild(QtWidgets.QPushButton, 'SMXLAUNCH')
        self.SMXLAUNCH.clicked.connect(lambda: self.runSMX())

        self.SMXDBKEY = self.findChild(QtWidgets.QLineEdit, 'SMXDBKEY')
        self.SMXGWASPAT = self.findChild(QtWidgets.QLineEdit, 'SMXGWASPAT')
        self.SMXMAXM = self.findChild(QtWidgets.QLineEdit, 'SMXMAXM')
        self.SMXVER = self.findChild(QtWidgets.QLineEdit, 'SMXVER')
        self.SMXOUTFILE = self.findChild(QtWidgets.QLineEdit, 'SMXOUTFILE')
        self.SMXFILTER = self.findChild(QtWidgets.QLineEdit, 'SMXFILTER')
        self.SMXPAT = self.findChild(QtWidgets.QLineEdit, 'SMXPAT')
        self.SMXMETAXFILTER = self.findChild(QtWidgets.QLineEdit, 'SMXMETAXFILTER')
        self.SMXMETAXPATTERN = self.findChild(QtWidgets.QLineEdit, 'SMXMETAXPATTERN')
        self.SMXREG = self.findChild(QtWidgets.QLineEdit, 'SMXREG')
        self.SMXCOND = self.findChild(QtWidgets.QLineEdit, 'SMXCOND')
        self.SMXEIGEN = self.findChild(QtWidgets.QLineEdit, 'SMXEIGEN')
        self.SMXTRAC = self.findChild(QtWidgets.QLineEdit, 'SMXTRAC')
        self.SMXTHR = self.findChild(QtWidgets.QLineEdit, 'SMXTHR')

        self.SMXSNP = self.findChild(QtWidgets.QLineEdit, 'SMXSNP')
        self.SMXEFF = self.findChild(QtWidgets.QLineEdit, 'SMXEFF')
        self.SMXNON = self.findChild(QtWidgets.QLineEdit, 'SMXNON')
        self.SMXBETA = self.findChild(QtWidgets.QLineEdit, 'SMXBETA')
        self.SMXSIGN = self.findChild(QtWidgets.QLineEdit, 'SMXSIGN')
        self.SMXOR = self.findChild(QtWidgets.QLineEdit, 'SMXOR')
        self.SMXZSCORE = self.findChild(QtWidgets.QLineEdit, 'SMXZSCORE')
        self.SMXPVAL = self.findChild(QtWidgets.QLineEdit, 'SMXPVAL')
        self.SMXSEP = self.findChild(QtWidgets.QLineEdit, 'SMXSEP')

        self.SMXCLEARLABEL = self.findChild(QtWidgets.QLabel, 'SMXCLEARLABEL')
        self.SMXCLEAR = self.findChild(QtWidgets.QPushButton, 'SMXCLEAR')
        self.SMXCLEAR.clicked.connect(
            lambda: self.SMXCLEARLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))


        self.SMXPRODUCTLABEL = self.findChild(QtWidgets.QLabel, 'SMXPRODUCTLABEL')
        self.SMXPRODUCT = self.findChild(QtWidgets.QPushButton, 'SMXPRODUCT')
        self.SMXPRODUCT.clicked.connect(
            lambda: self.SMXPRODUCTLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.SMXGWASLABEL = self.findChild(QtWidgets.QLabel, 'SMXGWASLABEL')
        self.SMXGWAS = self.findChild(QtWidgets.QPushButton, 'SMXGWAS')
        self.SMXGWAS.clicked.connect(
            lambda: self.SMXGWASLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))

        self.SMXCOVLABEL = self.findChild(QtWidgets.QLabel, 'SMXCOVLABEL')
        self.SMXCOV = self.findChild(QtWidgets.QPushButton, 'SMXCOV')
        self.SMXCOV.clicked.connect(
            lambda: self.SMXCOVLABEL.setText(QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]))


        self.SMXMODELLABEL = self.findChild(QtWidgets.QLabel, 'SMXMODELLABEL')
        self.SMXMODEL = self.findChild(QtWidgets.QPushButton, 'SMXMODEL')
        self.SMXMODEL.clicked.connect(
        lambda: self.SMXMODELLABEL.setText(
            QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.SMXGWASFOLDERLABEL = self.findChild(QtWidgets.QLabel, 'SMXGWASFOLDERLABEL')
        self.SMXGWASFOLDER = self.findChild(QtWidgets.QPushButton, 'SMXGWASFOLDER')
        self.SMXGWASFOLDER.clicked.connect(
            lambda: self.SMXGWASFOLDERLABEL.setText(
                QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.SMXMETAXLABEL = self.findChild(QtWidgets.QLabel, 'SMXMETAXLABEL')
        self.SMXMETAX = self.findChild(QtWidgets.QPushButton, 'SMXMETAX')
        self.SMXMETAX.clicked.connect(
            lambda: self.SMXMETAXLABEL.setText(
                QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.SMXOUTLABEL = self.findChild(QtWidgets.QLabel, 'SMXOUTLABEL')
        self.SMXOUT = self.findChild(QtWidgets.QPushButton, 'SMXOUT')
        self.SMXOUT.clicked.connect(
            lambda: self.SMXOUTLABEL.setText(QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose directory', '')))

        self.SMXTRIMM = self.findChild(QtWidgets.QCheckBox, 'SMXTRIMM')
        self.SMXPERM = self.findChild(QtWidgets.QCheckBox, 'SMXPERM')
        self.SMXTHROW = self.findChild(QtWidgets.QCheckBox, 'SMXTHROW')

    def validateSMX(self):
        comm = "./SMulTiXcan.py "
        if (str(self.SMXCLEARLABEL.text()) not in [""]):
            comm = comm + " --cleared_snps " + str(self.SMXCLEARLABEL.text())
        if (str(self.SMXGWASLABEL.text()) not in [""]):
            comm = comm + " --gwas_file " + str(self.SMXGWASLABEL.text())
        if (str(self.SMXMODELLABEL.text()) not in [""]):
            comm = comm + " --models_folder " + str(self.SMXMODELLABEL.text())
            if (str(self.SMXDBKEY.text()) not in [""]):
                comm = comm + " --model_db_snp_key " + str(self.SMXDBKEY.text())
            if (str(self.SMXFILTER.text()) not in [""]):
                comm = comm + " --models_name_filter " + str(self.SMXFILTER.text())
            if (str(self.SMXPAT.text()) not in [""]):
                comm = comm + " --models_name_pattern " + str(self.SMXPAT.text())
            if (str(self.SMXGWASFOLDERLABEL.text()) not in [""]):
                comm = comm + " --gwas_folder " + str(self.SMXGWASFOLDERLABEL.text())
            if (str(self.SMXGWASPAT.text()) not in [""]):
                comm = comm + " --gwas_file_pattern " + str(self.SMXGWASPAT.text())
        if (str(self.SMXMETAXLABEL.text()) not in [""]):
            comm = comm + " --metaxcan_folder " + str(self.SMXMETAXLABEL.text())
            if (str(self.SMXMETAXFILTER.text()) not in [""]):
                comm = comm + " --metaxcan_filter " + str(self.SMXMETAXFILTER.text())
            if (str(self.SMXMETAXPAT.text()) not in [""]):
                comm = comm + " --metaxcan_file_name_parse_pattern " + str(self.SMXMETAXPAT.text())
        if (str(self.SMXMODELLABEL.text()) not in [""]):
            comm = comm + " --model_product " + str(self.SMXMODELLABEL.text())

        if (self.SMXTRIMM.isChecked()):
            comm = comm + " --trimmed_ensemble_id "
        if (str(self.SMXCOVLABEL.text()) not in [""]):
            comm = comm + " --snp_covariance " + str(self.SMXCOVLABEL.text())
        if (str(self.SMXREG.text()) not in [""]):
            comm = comm + " --regularization " + str(self.SMXREG.text())
        if (str(self.SMXCOND.text()) not in [""]):
            comm = comm + " --cutoff_condition_number " + str(self.SMXCOND.text())
        if (str(self.SMXEIGEN.text()) not in [""]):
            comm = comm + " --cutoff_eigen_ratio " + str(self.SMXEIGEN.text())
        if (str(self.SMXTHR.text()) not in [""]):
            comm = comm + " --cutoff_threshold " + str(self.SMXTHR.text())
        if (str(self.SMXTRAC.text()) not in [""]):
            comm = comm + " --cutoff_trace_ratio " + str(self.SMXTRAC.text())
        if (self.SMXPERM.isChecked()):
            comm = comm + " --permissive_model_product "
        if (str(self.SMXMAXM.text()) not in [""]):
            comm = comm + " --MAX_M " + str(self.SMXMAXM.text())
        comm = comm + " --output " + str(self.SMXOUTLABEL.text()) + "/" + str(self.SMXOUTFILE.text())
        comm = comm + " --verbosity " + str(self.SMXVER.text())
        if (self.SMXTHROW.isChecked()):
            comm = comm + " --throw "

        if (str(self.SMXSNP.text()) not in [""]):
            comm = comm + " --snp_column " + str(self.SMXSNP.text())
        if (str(self.SMXEFF.text()) not in [""]):
            comm = comm + " --effect_allele_column " + str(self.SMXEFF.text())
        if (str(self.SMXNON.text()) not in [""]):
            comm = comm + " --non_effect_allele_column " + str(self.SMXNON.text())
        if (str(self.SMXBETA.text()) not in [""]):
            comm = comm + " --beta_column " + str(self.SMXBETA.text())
        if (str(self.SMXSIGN.text()) not in [""]):
            comm = comm + " --beta_sign_column " + str(self.SMXSIGN.text())
        if (str(self.SMXOR.text()) not in [""]):
            comm = comm + " --or_column " + str(self.SMXOR.text())
        if (str(self.SMXZSCORE.text()) not in [""]):
            comm = comm + " --zscore_column " + str(self.SMXZSCORE.text())
        if (str(self.SMXPVAL.text()) not in [""]):
            comm = comm + " --pvalue_column " + str(self.SMXPVAL.text())
        if (str(self.SMXSEP.text()) not in [""]):
            comm = comm + " --separator " + str(self.SMXSEP.text())

        return (comm)

    def runCancel(self):
        # print(self.process.pid())

        self.CONSSCREEN.clear()
        if self.process.pid()>0: #If its running, the pid will be > 0
            print('Canceled')
            self.process.terminate()
            self.process.waitForFinished()



    def runSMX(self):
        command = self.validateSMX()
        print(command)
        cwd = METAXCAN_DIR

        self.runCancel()
        self.CONSSCREEN.appendPlainText(command)
        self.process.setWorkingDirectory(cwd)
        self.process.start(command)
        # monitor.execute(command,cwd)
        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()

    def runMUL(self):
        command = self.validateMUL()
        print(command)
        cwd = METAXCAN_DIR

        self.runCancel()
        self.CONSSCREEN.appendPlainText(command)
        self.process.setWorkingDirectory(cwd)
        self.process.start(command)

        # monitor.execute(self, command, cwd)
        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()

    def runMSP(self):
        command = self.validateMSP()
        print(command)
        cwd = METAXCAN_DIR

        self.runCancel()
        self.CONSSCREEN.appendPlainText(command)
        self.process.setWorkingDirectory(cwd)
        self.process.start(command)

        # monitor.execute(self,command, cwd)
        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()

    def runMPX(self):

        command = self.validateMPX()
        print(command)
        cwd = METAXCAN_DIR

        self.runCancel()
        self.CONSSCREEN.appendPlainText(command)
        self.process.setWorkingDirectory(cwd)
        self.process.start(command)

    def runTCM(self):
        command = self.validateTCM()
        print(command)
        cwd = './methods/TIGAR/TWAS/Covar'

        self.runCancel()
        self.CONSSCREEN.appendPlainText(command)
        self.process.setWorkingDirectory(cwd)
        self.process.start(command)

        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()

    def runTTW(self):
        command = self.validateTTW()
        print(command)
        cwd = TIGAR_DIR

        self.runCancel()
        self.CONSSCREEN.appendPlainText(command)
        self.process.setWorkingDirectory(cwd)
        self.process.start(command)

        # monitor.execute(self,command, cwd)
        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()

    def runTGR(self):
        command = self.validateTGR()
        print(command)
        cwd = TIGAR_DIR

        self.runCancel()
        self.CONSSCREEN.appendPlainText(command)
        self.process.setWorkingDirectory(cwd)
        self.process.start(command)

        # monitor.execute(self,command, cwd)
        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()

    def runTMT(self):
        command = self.validateTMT()
        print(command)
        cwd = TIGAR_DIR

        self.runCancel()
        self.CONSSCREEN.appendPlainText(command)
        self.process.setWorkingDirectory(cwd)
        self.process.start(command)
        # monitor.execute(self,command, cwd)
        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()

    def run_FAT(self):

        command = self.validateFAT()
        print(command)
        cwd = FUSION_DIR

        self.runCancel()
        self.CONSSCREEN.appendPlainText(command)
        self.process.setWorkingDirectory(cwd)
        self.process.start(command)

        # monitor.execute(self,command, cwd)
        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()

    def run_FCW(self):

        command = self.validateFCW()
        print(command)
        cwd = FUSION_DIR

        self.runCancel()
        self.CONSSCREEN.appendPlainText(command)
        self.process.setWorkingDirectory(cwd)
        self.process.start(command)

        # monitor.execute(command, cwd)

        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()

    def run_FPP(self):

        command = self.validateFPP()
        print(command)
        cwd = FUSION_DIR

        self.runCancel()
        self.CONSSCREEN.appendPlainText(command)
        self.process.setWorkingDirectory(cwd)
        self.process.start(command)

        # monitor.execute(self,command, cwd)

        # monitor.print_cpu_chart()
        # monitor.print_write_read_operations_chart()
        # monitor.print_rss_chart()



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()