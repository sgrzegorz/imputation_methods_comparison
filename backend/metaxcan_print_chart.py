import math
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import plotly.express as px
import pandas as pd
# df = px.data.tips()
# fig = px.histogram(df, x="total_bill")
#from definitions import ROOT_DIR
import sys




class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)

        vlayout = QtWidgets.QVBoxLayout(self)
        vlayout.addWidget(self.browser)

        self.resize(1000,800)
        self.show_graph()

    def show_graph(self):
        # chart_file=f'{ROOT_DIR}/output/metaxcan_before_after.csv'
        chart_file=sys.argv[1]
        columns = ["gene","before","after"]
        dtypes ={"gene": str,"before":float,"after":float}
        data = pd.read_csv(chart_file, usecols=columns,dtype=dtypes,sep='\t',header=(0))
        data =data.sort_values(by=['gene'])
        y = []
        for index, row in data.iterrows():
            log = abs(math.log(abs(row['before']-row['after'])))
            y.append(log)
        title = 'Metaxcan pvalue comparison'
        labels =dict(x="gene", y="| log| initialPvalue - finalPvalue ||")
        fig = px.bar(x=list(data.gene), y =y, labels=labels,title=title)
        fig.update_xaxes(type='category')
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Widget()
    widget.show()
    app.exec()