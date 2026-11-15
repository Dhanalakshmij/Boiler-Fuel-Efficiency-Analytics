import pandas as pd
df=pd.read_csv("data/demo.csv")
for pct in [-.1,0,.1]:print(pct,round((df.energy_kwh*(1+pct)).sum(),2))
