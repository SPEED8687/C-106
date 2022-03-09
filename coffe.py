import pandas as pd
import numpy as np
df=pd.read_csv('cups of coffee vs hours of sleep.csv')
coffe=df['Coffee in ml'].tolist()
sleep=df['sleep in hours'].tolist()
d={'x':coffe,'y':sleep}
correlation=np.corrcoef(d['x'],d['y'])
print(correlation)