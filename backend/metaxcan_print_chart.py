import math

import plotly.express as px
import pandas as pd
# df = px.data.tips()
# fig = px.histogram(df, x="total_bill")


columns = ["gene","before","after"]
dtypes ={"gene": str,"before":float,"after":float}
data = pd.read_csv('pictures/metaxcan_before_after.csv', usecols=columns,dtype=dtypes,sep='\t',header=(0))

data =data.sort_values(by=['gene'])

y = []
for index, row in data.iterrows():
    log = abs(math.log(abs(row['before']-row['after'])))
    y.append(log)


title = 'Metaxcan pvalue comparison'
labels =dict(x="gene", y="| log| initialPvalue - finalPvalue ||")
fig = px.bar(x=list(data.gene), y =y, labels=labels,title=title)
fig.update_xaxes(type='category')
fig.show()

