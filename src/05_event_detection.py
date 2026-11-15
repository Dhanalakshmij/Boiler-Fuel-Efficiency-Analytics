import pandas as pd
df=pd.read_csv("data/demo.csv");threshold=df.energy_kwh.quantile(.95)
print("High-use events",int((df.energy_kwh>threshold).sum()))
