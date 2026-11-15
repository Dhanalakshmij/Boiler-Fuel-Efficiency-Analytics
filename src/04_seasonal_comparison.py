import pandas as pd
from sklearn.metrics import mean_absolute_error
df=pd.read_csv("data/demo.csv");k=int(len(df)*.8)
a,b=df.iloc[:k],df.iloc[k:]
p=b.hour.map(a.groupby("hour").energy_kwh.mean())
print("Hourly baseline MAE",mean_absolute_error(b.energy_kwh,p))
