# This code is for generating Fig.2
# The file path needs to be modified to the actual path when reading the file.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16

df = pd.read_excel('Fig2_data.xlsx', sheet_name='Sheet1') 
df.columns = ['Year', 'Coal', 'Gas', 'Biomass', 'Hydro', 'Nuclear', 'Central_PV', 'Detributed PV', 'Onshore Wind', 'Offshore Wind', 'Storage', 'Pump Storage']
df = df[df['Year'].apply(lambda x: str(x).isdigit())].sort_values('Year')

energy_order = ['Coal', 'Gas', 'Biomass', 'Hydro', 'Nuclear', 'Central_PV', 'Detributed PV', 'Onshore Wind', 'Offshore Wind', 'Storage', 'Pump Storage']
colors = {
    'Coal': 'black',
    'Gas' : 'deeppink',
    'Biomass': 'peru',
    'Hydro': 'deepskyblue',
    'Nuclear': 'red',
    'Central_PV': 'gold',
    'Detributed PV': 'yellow',
    'Onshore Wind': 'lime',
    'Offshore Wind' : 'seagreen',
    'Storage' : 'purple',
    'Pump Storage': 'blue'
}
plt.figure(figsize=(14, 7))

bottom = [0] * len(df)

for energy in energy_order:
    plt.bar(
        x=df['Year'], 
        height=df[energy], 
        bottom=bottom,
        color=colors[energy], 
        label=energy,
        width=0.6
    )
    bottom = [i + j for i, j in zip(bottom, df[energy])] 

plt.xlabel('Year', fontsize=16)
plt.ylabel('Installed Capacity (GW)', fontsize=16)
plt.xticks(df['Year'], rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()