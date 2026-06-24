# This code is for generating Fig.3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.colors as mcolors

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 20

data = {
    'Province': ['AH', 'BJ', 'CQ', 'FJ', 'GS', 'GD', 
                'GX', 'GZ', 'HaN', 'HeB', 'HLJ', 'HeN', 
                'HuB', 'HuN', 'IM', 'JS', 'JX', 'JL', 
                'LN', 'NX', 'QH', 'SaX', 'SD', 'SH', 
                'SX', 'SC', 'TJ', 'XJ', 'TB', 'YN', 'ZJ'],
    '2011': [122.211, 82.1564, 71.7056, 151.591, 92.3504, 440.424, 111.204, 94.4099, 
            18.5454, 298.501, 80.1923, 265.926, 145.068, 129.334, 186.409, 428.152, 
            83.5118, 63.0113, 186.144, 72.4569, 56.0714, 98.245, 363.488, 133.96, 
            165.051, 175.159, 69.5131, 83.9092, 2.37735, 120.467, 311.705],
    '2015': [164.084, 95.2585, 87.5433, 185.221, 109.87, 531.878, 133.415, 117.428, 
            27.2633, 317.577, 86.8937, 287.971, 166.527, 144.772, 254.269, 511.495, 
            108.735, 65.1921, 198.5, 87.8387, 65.8035, 122.182, 511.736, 140.576, 
            173.735, 199.244, 80.0652, 216.039, 4.0527, 143.952, 355.493],
    '2019': [230.239, 116.575, 115.993, 240.169, 128.804, 670.181, 190.694, 154.105, 
            35.5326, 385.602, 99.598, 336.396, 221.405, 186.396, 365.294, 626.405, 
            153.591, 77.9985, 240.096, 108.394, 71.5959, 191.198, 621.905, 156.906, 
            226.213, 263.592, 87.8005, 286.804, 7.8003, 181.316, 470.592],
    '2024': [343.477, 145.006, 155.18, 329.99, 175.686, 908.777, 261.541, 190.424, 
            51.5258, 508.047, 126.451, 436.803, 289, 243.184, 515.096, 836.564, 
            216.377, 99.1105, 284.408, 148.132, 108.722, 261.66, 850.768, 197.473, 
            308.118, 396.335, 112.247, 408.083, 14.418, 268.542, 661.306]
}

df = pd.DataFrame(data)
df_long = pd.melt(df, id_vars=['Province'], var_name='Year', value_name='Load')

tab20 = plt.cm.tab20(np.linspace(0, 1, 20))
tab20b = plt.cm.tab20b(np.linspace(0, 1, 20))
all_colors = np.vstack([tab20, tab20b])  
province_color_map = {prov: all_colors[i] for i, prov in enumerate(df['Province'])}

years = sorted(df_long['Year'].unique())
year_colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(years)))
year_color_map = {year: color for year, color in zip(years, year_colors)}

fig, ax = plt.subplots(figsize=(18, 10))

vertical_spacing = 2.5

for i, province in enumerate(df['Province']):
    y_pos = i * vertical_spacing
    
    
    province_data = df_long[df_long['Province'] == province]['Load'].values
    
    
    kde = stats.gaussian_kde(province_data, bw_method='scott')  
    x_range = np.linspace(province_data.min() - 50, province_data.max() + 50, 200)
    density = kde(x_range)
    
    
    scaled_density = density / density.max() * 1.0
    
    
    prov_color = province_color_map[province]
    
    
    ax.fill_between(x_range, 
                    y_pos - scaled_density, 
                    y_pos + scaled_density, 
                    color=prov_color, alpha=0.35, edgecolor=None)
    
    ax.plot(x_range, y_pos - scaled_density, color=prov_color, linewidth=1.5, alpha=0.7)
    ax.plot(x_range, y_pos + scaled_density, color=prov_color, linewidth=1.5, alpha=0.7)
    
    province_years = df_long[df_long['Province'] == province]
    for _, row in province_years.iterrows():
        x_val = row['Load']
        density_at_x = kde.evaluate(x_val) 
        if density.max() > 0:
            half_height = (density_at_x / density.max()) * 1.0
        else:
            half_height = 0.3
        jitter = np.random.uniform(-half_height, half_height)
        
        ax.scatter(
            x_val, 
            y_pos + jitter, 
            color=year_color_map[row['Year']], 
            s=120,
            alpha=0.9,
            edgecolors='white',
            linewidth=1.2,
            zorder=6
        )

y_ticks = [i * vertical_spacing for i in range(len(df['Province']))]
ax.set_yticks(y_ticks)
ax.set_yticklabels(df['Province'])
ax.set_ylim(-1.5, len(df['Province']) * vertical_spacing + 0.5)

legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=year_color_map[year], 
               markersize=14, label=year) 
    for year in years
]
ax.legend(handles=legend_elements, loc='upper right', 
          fontsize=18, prop={'family': 'Times New Roman', 'size': 18})

ax.set_xlabel('Load (TWh)', fontsize=24, fontweight='normal')
ax.set_ylabel('Province', fontsize=24, fontweight='normal')
ax.tick_params(axis='both', labelsize=20)
for label in ax.get_xticklabels():
    label.set_fontfamily('Times New Roman')
for label in ax.get_yticklabels():
    label.set_fontfamily('Times New Roman')

ax.grid(True, alpha=0.2, linestyle='--', which='major', axis='x')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)


plt.tight_layout()
plt.show()