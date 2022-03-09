import pandas as pd
import numpy as np
df=pd.read_csv('Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv')
coldDrinks=df['Cold drink sales( ₹ )'].tolist()
temprature=df['Temperature'].tolist()
d={'x':temprature,'y':coldDrinks}
correlation=np.corrcoef(d['x'],d['y'])
print(correlation)