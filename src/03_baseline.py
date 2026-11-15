import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
df=pd.read_csv("data/demo.csv"); f=["hour","temperature_c","activity_index","tariff_per_kwh"]
k=int(len(df)*.8); a,b=df.iloc[:k],df.iloc[k:]
m=RandomForestRegressor(n_estimators=80,random_state=42).fit(a[f],a.energy_kwh)
print("MAE",mean_absolute_error(b.energy_kwh,m.predict(b[f])))
