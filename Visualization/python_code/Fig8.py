# The code is for generating Fig.8.
# The provincial load profiles are sourced from 'china_demand2024.xlsx'.
# The profiles for each province can be obtained by changing the province name in the code and then running it.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 38

file_path = 'Load/china_demand2024.xlsx'
df = pd.read_excel(file_path)

jiangsu_column = 'Jiangsu'

jiangsu_load = df[jiangsu_column].iloc[0:8760] 
jiangsu_load_gwh = jiangsu_load / 1000 

hours = np.arange(1, 8761)

plt.figure(figsize=(15, 8))
plt.plot(hours, jiangsu_load_gwh.values, linewidth=2, color='royalblue')
plt.xlim(1, 8760)
plt.xticks(
    [1, 1417, 2881, 4345, 5833, 7297], 
    ['Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'],
    fontsize=38,
    fontfamily='Times New Roman'
)

plt.yticks(fontsize=38, fontfamily='Times New Roman')

plt.ylabel('Load (GWh)', fontfamily='Times New Roman', fontsize=38)
plt.tight_layout()
plt.show()