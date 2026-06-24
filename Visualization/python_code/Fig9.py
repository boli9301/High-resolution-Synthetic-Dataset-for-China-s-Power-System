# The code is for generating Fig.9.
# The data used for generating the figure is the same as the data used for generating Fig.6.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'Fig6_data.xlsx'
sheet_name = 'Sheet1'
df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

data = []
current_unit = None
for index, row in df.iterrows():
    if pd.notna(row[0]) and isinstance(row[0], str) and 'MW' in row[0]:
        current_unit = row[0]
    elif isinstance(row[0], (int, float)) and pd.notna(row[0]):
        load = row[0]
        cost_b = row[1]/7140 
        cost_d = row[3]/7140  
        if pd.notna(cost_b) and pd.notna(cost_d):
            data.append({
                'Unit': current_unit,
                'Load': load,
                'Cost_B': cost_b,
                'Cost_D': cost_d
            })

df_plot = pd.DataFrame(data)

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 24
plt.rcParams['axes.linewidth'] = 1.5

units = df_plot['Unit'].unique()
b_data = [df_plot[df_plot['Unit'] == unit]['Cost_B'].values for unit in units]
d_data = [df_plot[df_plot['Unit'] == unit]['Cost_D'].values for unit in units]

fig, ax = plt.subplots(figsize=(16, 10))
positions = np.arange(len(units))
width = 0.35

bp_b = ax.boxplot(b_data, positions=positions - width/2, widths=width, 
                 patch_artist=True, showfliers=False)
bp_d = ax.boxplot(d_data, positions=positions + width/2, widths=width, 
                 patch_artist=True, showfliers=False)

for box in bp_b['boxes']:
    box.set(facecolor='lightblue', alpha=0.7)
for box in bp_d['boxes']:
    box.set(facecolor='lightcoral', alpha=0.7)

for i, unit in enumerate(units):
    unit_data = df_plot[df_plot['Unit'] == unit]
    x_positions = np.random.normal(i - width/2, 0.05, len(unit_data))
    ax.scatter(x_positions, unit_data['Cost_B'], color='blue', alpha=0.6, s=50)
    x_positions = np.random.normal(i + width/2, 0.05, len(unit_data))
    ax.scatter(x_positions, unit_data['Cost_D'], color='red', alpha=0.6, s=50)

ax.set_xlabel('Generator Type', fontsize=24)
ax.set_ylabel('Costs (thousand dollars)', fontsize=24)
units_wr = [u.replace(' ', '\n ') if ' ' in str(u) else u for u in units]
ax.set_xticks(positions)
ax.set_xticklabels(units_wr, rotation=10)

from matplotlib.patches import Patch
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='lightblue', edgecolor='k', label='Fitting results'),
    Patch(facecolor='lightcoral', edgecolor='k', label='Calculation results')
]
ax.legend(handles=legend_elements, loc='best', fontsize=24)

plt.tight_layout()
plt.show()