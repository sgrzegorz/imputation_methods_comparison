import math

import plotly.express as px
import pandas as pd
# df = px.data.tips()
# fig = px.histogram(df, x="total_bill")


columns = ["gene","before","after"]
dtypes ={"gene": str,"before":float,"after":float}
data = pd.read_csv('pictures/fusion_before_after.csv', usecols=columns,dtype=dtypes,sep='\t',header=(0))

y = []
for index, row in data.iterrows():
    log = abs(math.log(abs(row['before']-row['after'])))
    y.append(log)



fig = px.bar(x=list(data.gene), y =y, labels=dict(x="gene", y="| log| initialPvalue - finalPvalue ||"))
fig.update_xaxes(type='category')
fig.show()


