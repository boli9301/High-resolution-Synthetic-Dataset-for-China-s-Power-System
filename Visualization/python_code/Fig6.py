# The code is for generating Fig.6

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

file_path = "Fig6_data.xlsx"
sheet_name = "Sheet1"
df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

load_col = 0 
coal_col = 2 

unit_sections = {
    "Subcritical 300MW": (1, 21),
    "Supercritical 300MW": (22, 44),
    "Subcritical 600MW": (45, 64),
    "Supercritical 600MW": (65, 84),
    "Ultra-supercritical 600MW": (85, 109),
    "Ultra-supercritical 1000MW": (110, 130)
}

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 18

plt.figure(figsize=(12, 8))

colors = {
    "Subcritical 300MW": "blue",
    "Supercritical 300MW": "red",
    "Subcritical 600MW": "green",
    "Supercritical 600MW": "orange",
    "Ultra-supercritical 600MW": "blueviolet",
    "Ultra-supercritical 1000MW": "brown"
}

for unit, (start, end) in unit_sections.items():
    load_values = df.iloc[start:end, load_col].astype(float)
    coal_values = df.iloc[start:end, coal_col].astype(float)
    plt.plot(load_values, coal_values, label=unit, color=colors[unit], linewidth=2)

plt.xlabel("Load (MW)")
plt.ylabel("Coal Consumption Rate (g/kWh)")
plt.legend()

plt.tight_layout()
plt.show()