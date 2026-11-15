import pandas as pd
df=pd.read_csv("data/demo.csv")
print("Illustrative cost",(df.energy_kwh*df.tariff_per_kwh).sum())
