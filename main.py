from PyQt5 import QtWidgets, uic
import sys
import subprocess
import fusion_compute_weights
import fusion_association_test
import fusion_post_processing
import tigar_twas
import tigar_cov_matrix
import tigar_grx_prediction
import tigar_model_training

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('view/App_View.ui', self)

        # widget.ui powinien miec rozmiary 1277 x 728 ustaw je recznie w QT Designer

        self.tab_11 = fusion_compute_weights.FusionComputeWeights()
        self.tabWidget_2.addTab(self.tab_11, "Compute Weights")

        self.tab_12 = fusion_association_test.FusionAssociationTest()
        self.tabWidget_2.addTab(self.tab_12, "Association Test")

        self.tab_13 = fusion_post_processing.FusionPostProcessing()
        self.tabWidget_2.addTab(self.tab_13, "Post Processing")


        self.tab_16 = tigar_model_training.TigarModelTraining()
        self.tabWidget_3.addTab(self.tab_16, "Model Training")

        self.tab_9 = tigar_grx_prediction.TigarGrxPrediction()
        self.tabWidget_3.addTab(self.tab_9, "GReX Prediction")

        self.tab_17 = tigar_twas.TigarTwas()
        self.tabWidget_3.addTab(self.tab_17, "TWAS")

        self.tab_18 = tigar_cov_matrix.TigarCovMatrix()
        self.tabWidget_3.addTab(self.tab_18, "Covariance Matrix Calculation")


        self.show()



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
