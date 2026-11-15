import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("data/demo.csv")
df.groupby("hour").energy_kwh.mean().plot(title="Illustrative hourly demand")
plt.ylabel("kWh");plt.tight_layout();plt.savefig("energy_profile.png")
