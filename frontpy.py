from PyQt5 import QtWidgets, uic
import sys
import subprocess

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('front.ui', self)
		
        command_attributes = {}

        self.LaunchButton = self.findChild(QtWidgets.QPushButton, 'LaunchButton')
        self.LaunchButton.clicked.connect(self.printButtonPressed) 
		
        self.GenePathButton = self.findChild(QtWidgets.QPushButton, 'GenePathButton') 
        self.GenePathButton.clicked.connect(self.findGeneButtonPressed) 
		
		
        self.display = self.findChild(QtWidgets.QLabel, 'display')
        self.display_body=""

        self.show()

    def findGeneButtonPressed(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\')
        print(fname[0])
		
    def printButtonPressed(self):
        result = subprocess.run(['dir', ''],universal_newlines = True, shell = True, stdout=subprocess.PIPE)
        self.display_body=self.display_body+result.stdout
        self.display.setText(self.display_body)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()