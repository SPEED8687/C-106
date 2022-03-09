import pandas as pd
import numpy as np
import plotly.express as px
df=pd.read_csv('Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv')
iceCream=df['Ice-cream Sales( ₹ )'].tolist()
temprature=df['Temperature'].tolist()
# graph=px.scatter(df,x=temprature,y=iceCream)
# graph.show
d={'x':temprature,'y':iceCream}
correlation=np.corrcoef(d['x'],d['y'])
print(correlation)