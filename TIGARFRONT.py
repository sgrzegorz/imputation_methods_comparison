from PyQt5 import QtWidgets, uic
import sys
import subprocess

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('TIGARUI.ui', self)
        
        self.command_attributes = {}
        self.command_attributes["TIGARTRAIN"]={}
        self.command_attributes["GREX"]={}
        self.command_attributes["RCF"]={}
        self.command_attributes["TWAS"]={}
		
		#TIGAR TRAIN
        self.LaunchButton1 = self.findChild(QtWidgets.QPushButton, 'LaunchButton')
        self.LaunchButton1.clicked.connect(self.printButtonPressed) 
		
        self.display1 = self.findChild(QtWidgets.QLabel, 'display')
        self.display_body1=""
        
        self.ModelComboBox_1= self.findChild(QtWidgets.QComboBox, 'ModelComboBox')
        #self.ModelComboBox_1.activated.connect(self.chooseModel)
        self.command_attributes["TIGARTRAIN"]["--model"] = self.ModelComboBox_1.currentText()
		
        self.GenePathButton1 = self.findChild(QtWidgets.QPushButton, 'GenePathButton') 
        self.GenePathButton1.clicked.connect(self.findGeneButtonPressed)
        self.command_attributes["TIGARTRAIN"]["--Gene_Exp"] = ""
		
        self.SampleIDButton1 = self.findChild(QtWidgets.QPushButton, 'SampleIDButton') 		
        self.GenePathButton1.clicked.connect(self.findGeneButtonPressed)
        self.command_attributes["TIGARTRAIN"]["--sampleID"] = ""

        self.ChromText1=self.findChild(QtWidgets.QTextEdit,'ChromText')
        self.command_attributes["TIGARTRAIN"]["--chr"] = self.ChromText1.toPlainText()

        self.GenofileComboBox_1= self.findChild(QtWidgets.QComboBox, 'GenofileComboBox')
        #self.ModelComboBox_1.activated.connect(self.chooseModel)
        self.command_attributes["TIGARTRAIN"]["--genofile_type"] = self.GenofileComboBox_1.currentText()

        self.GenoFileButton1 = self.findChild(QtWidgets.QPushButton, 'GenofileButton') 
        self.command_attributes["TIGARTRAIN"]["--genofile"] = ""

        self.GenotypeComboBox_1= self.findChild(QtWidgets.QComboBox, 'GenotypeComboBox')
        #self.ModelComboBox_1.activated.connect(self.chooseModel)
        self.command_attributes["TIGARTRAIN"]["--Format"] = ""

        self.MafText1=self.findChild(QtWidgets.QTextEdit,'MafText')
        self.command_attributes["TIGARTRAIN"]["--maf"] = self.MafText1.toPlainText()

        self.HWEText1=self.findChild(QtWidgets.QTextEdit,'HWEText')
        self.command_attributes["TIGARTRAIN"]["--hwe"] = self.HWEText1.toPlainText()

        self.threadText1=self.findChild(QtWidgets.QTextEdit,'threadText')
        self.command_attributes["TIGARTRAIN"]["--thread"] = self.threadText1.toPlainText()

        self.windowText1=self.findChild(QtWidgets.QTextEdit,'windowText')
        self.command_attributes["TIGARTRAIN"]["--window"] = self.windowText1.toPlainText()
		
        self.GroupBox3 = self.findChild(QtWidgets.QGroupBox, 'groupBox_3')
		
        self.DPRComboBox= self.findChild(QtWidgets.QComboBox, 'DPRComboBox')
        #self.ModelComboBox_1.activated.connect(self.chooseModel)
        self.command_attributes["TIGARTRAIN"]["--dpr"] = self.GenofileComboBox_1.currentText()

		
        self.EffectSizeComboBox_1= self.findChild(QtWidgets.QComboBox, 'EffectSizeComboBox')
        #self.ModelComboBox_1.activated.connect(self.chooseModel)
        self.command_attributes["TIGARTRAIN"]["--ES"] = self.EffectSizeComboBox_1.currentText()

        self.GroupBox4 = self.findChild(QtWidgets.QGroupBox, 'groupBox_4')

        self.cvText =self.findChild(QtWidgets.QTextEdit,'cvText')
        self.command_attributes["TIGARTRAIN"]["--cv"] = self.cvText.toPlainText()
        
        self.AlphaText =self.findChild(QtWidgets.QTextEdit,'AlphaText')
        self.command_attributes["TIGARTRAIN"]["--alpha"] = self.AlphaText.toPlainText()
		
        self.BackButton1 = self.findChild(QtWidgets.QPushButton, 'BackButton')
		
		#Grex prediction
		#RCF calculation
		#TWAS
		
        self.GroupBox = self.findChild(QtWidgets.QGroupBox, 'groupBox')
        self.GroupBox2 = self.findChild(QtWidgets.QGroupBox, 'groupBox_2')

        

        self.qb=self.findChild(QtWidgets.QComboBox,'ModelComboBox_3')
        self.qb.activated.connect(self.qcombobox)
		
        
        self.show()

    def findGeneButtonPressed(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\')
        print(fname[0])

    def printButtonPressed(self):
        self.GroupBox.hide()
        result = subprocess.run(['dir', ''],universal_newlines = True, shell = True, stdout=subprocess.PIPE)
        self.display_body1=self.display_body1+self.qb.currentText()
        self.display.setText(str(self.command_attributes["TIGARTRAIN"]))
		
    def qcombobox(self):
        if(self.qb.currentText() =="TWAS with individual-level GWAS data"):
            self.GroupBox.hide()
            self.GroupBox2.show()
        else:
            self.GroupBox.show()
            self.GroupBox2.hide()			
        result = subprocess.run(['dir', ''],universal_newlines = True, shell = True, stdout=subprocess.PIPE)
        self.display_body=self.display_body+self.qb.currentText()
        self.display.setText(self.display_body)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()