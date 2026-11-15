import pandas as pd
from sklearn.preprocessing import StandardScaler
df=pd.read_csv("data/demo.csv")
X=df[["hour","temperature_c","activity_index","tariff_per_kwh"]]
print(StandardScaler().fit_transform(X).shape)
