import pandas as pd
df=pd.read_csv("data/demo.csv")
print(df.describe().round(2))
print(df.groupby("hour").energy_kwh.mean())
