# The code is for generating Fig.4.
# The china's map is sourced from https://datav.aliyun.com/portal/school/atlas/area_selector

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from io import BytesIO
import numpy as np
import matplotlib
from matplotlib.transforms import Bbox
from matplotlib.patches import Rectangle

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16

energy_df = pd.read_excel('Fig4_data.xlsx', sheet_name='Sheet1')
coord_df = pd.read_excel('Fig4_data.xlsx', sheet_name='Sheet2')
coord_df['Province'] = coord_df['Province'].str.replace(r'（.*?）', '', regex=True)
china = gpd.read_file('china.shp')

trans_df = pd.read_excel('Fig4_data.xlsx', sheet_name='Sheet3')
trans_df = trans_df[trans_df["CATE"].isin(["AC", "DC"])][["Farea", "Tarea", "Cap", "CATE"]]
trans_df['Farea'] = trans_df['Farea'].str.replace(r'（.*?）', '', regex=True)
trans_df['Tarea'] = trans_df['Tarea'].str.replace(r'（.*?）', '', regex=True)

coord_dict = coord_df.set_index('Province')[['Lon', 'Lat']].to_dict(orient='index')

fig, ax = plt.subplots(figsize=(15, 9))

ax.set_facecolor('w')

china.plot(ax=ax, edgecolor='k', linewidth=0.5, facecolor='w')

def line_style(cate, capacity):

    base_colors = {
        'AC': 'm', 
        'DC': 'mediumblue',
    }
    base_color = base_colors.get(cate, 'gray')
    

    if cate == 'DC':
        
        lw_min, lw_max = 1, 5
       
        cap_min, cap_max = trans_df[trans_df['CATE'] == 'DC']['Cap'].min(), trans_df[trans_df['CATE'] == 'DC']['Cap'].max()
        if cap_max == cap_min:
            lw = (lw_min + lw_max) / 2
        else:
           
            normalized_cap = (capacity - cap_min) / (cap_max - cap_min)
            exp_factor = 2.5 
            lw = lw_min + (lw_max - lw_min) * (normalized_cap ** exp_factor)
    else:
        lw_min, lw_max = 1, 5
        cap_min, cap_max = trans_df['Cap'].min(), trans_df['Cap'].max()
        if cap_max == cap_min:
            lw = (lw_min + lw_max) / 2
        else:
            lw = lw_min + (capacity - cap_min) / (cap_max - cap_min) * (lw_max - lw_min)
    
    return base_color, lw

for _, row in trans_df.iterrows():
    start = coord_dict.get(row['Farea'])
    end   = coord_dict.get(row['Tarea'])
    if start and end:
        color, lw = line_style(row['CATE'], row['Cap'])
        ax.plot([start['Lon'], end['Lon']],
                [start['Lat'], end['Lat']],
                color=color, lw=lw, alpha=0.9, solid_capstyle='round')

energy_types = ['coal', 'hydro', 'nuclear', 'PV', 'wind']
colors       = ['dimgray', 'deepskyblue', 'red', 'orange', 'lawngreen']
buffer       = 4
max_adjust_steps = 1
adjusted_positions = []

def pie_zoom(total):
    
    return np.sqrt(total) / 800

for _, row in energy_df.iterrows():
    province_name = row['Province']
    coord = coord_df[coord_df['Province'] == province_name]
    if coord.empty:
        continue
    lng, lat = coord['Lon'].values[0], coord['Lat'].values[0]

    total = row[energy_types].sum()
    if total <= 0:
        continue

    sizes = [row[et] for et in energy_types]
    filtered = [(s, c) for s, c in zip(sizes, colors) if s > 0]
    sizes_f, colors_f = zip(*filtered) if filtered else ([], [])

    pie_fig, pie_ax = plt.subplots(figsize=(1, 1))
    pie_ax.pie(sizes_f, colors=colors_f, startangle=90)
    pie_ax.axis('equal')
    buf = BytesIO()
    pie_fig.savefig(buf, format='png', dpi=90, bbox_inches='tight', transparent=True)
    plt.close(pie_fig)
    buf.seek(0)
    img = plt.imread(buf)


    adjusted_lng, adjusted_lat = lng, lat
    step = 0.3
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for _ in range(max_adjust_steps):
        collision = any(abs(adjusted_lng - pos['lng']) < buffer and
                        abs(adjusted_lat - pos['lat']) < buffer for pos in adjusted_positions)
        if not collision:
            break
        for dx, dy in directions:
            temp_lng, temp_lat = adjusted_lng + dx*step, adjusted_lat + dy*step
            collision = any(abs(temp_lng - pos['lng']) < buffer and
                            abs(temp_lat - pos['lat']) < buffer for pos in adjusted_positions)
            if not collision:
                adjusted_lng, adjusted_lat = temp_lng, temp_lat
                break

    adjusted_positions.append({'lng': adjusted_lng, 'lat': adjusted_lat})
    zoom = pie_zoom(total)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, (adjusted_lng, adjusted_lat), frameon=False)
    ax.add_artist(ab)


south_china_sea_ax = fig.add_axes([0.695, 0.072, 0.2, 0.2])


south_china_sea_bounds = [105, 125, 3, 25] 


china.plot(ax=south_china_sea_ax, edgecolor='k', linewidth=0.3, facecolor='w')
south_china_sea_ax.set_xlim(south_china_sea_bounds[0], south_china_sea_bounds[1])
south_china_sea_ax.set_ylim(south_china_sea_bounds[2], south_china_sea_bounds[3])
south_china_sea_ax.set_facecolor('w')


rect = Rectangle((south_china_sea_bounds[0], south_china_sea_bounds[2]),  
                 south_china_sea_bounds[1] - south_china_sea_bounds[0],  
                 south_china_sea_bounds[3] - south_china_sea_bounds[2],  
                 linewidth=2, edgecolor='black', facecolor='none', zorder=10)
south_china_sea_ax.add_patch(rect)


south_china_sea_ax.set_xticks([])
south_china_sea_ax.set_yticks([])


for spine in south_china_sea_ax.spines.values():
    spine.set_visible(False)

from matplotlib.patches import Rectangle

energy_handles = [Rectangle((0, 0), 2.4, 1.6, facecolor=c)  
                  for c in colors]

ac_capacities = [10000, 5000, 1000] 
dc_capacities = [12000, 8000, 3000]  
ac1_capacities = [2000]  

def legend_line_style(cate, capacity):
    if cate == 'DC':
        lw_min, lw_max = 1, 5
        cap_min, cap_max = trans_df[trans_df['CATE'] == 'DC']['Cap'].min(), trans_df[trans_df['CATE'] == 'DC']['Cap'].max()
        if cap_max == cap_min:
            lw = (lw_min + lw_max) / 2
        else:
            normalized_cap = (capacity - cap_min) / (cap_max - cap_min)
            exp_factor = 2.5
            lw = lw_min + (lw_max - lw_min) * (normalized_cap ** exp_factor)
    else:
        lw_min, lw_max = 1, 5
        cap_min, cap_max = trans_df['Cap'].min(), trans_df['Cap'].max()
        if cap_max == cap_min:
            lw = (lw_min + lw_max) / 2
        else:
            lw = lw_min + (capacity - cap_min) / (cap_max - cap_min) * (lw_max - lw_min)
    
    return lw

def legend_line(cap, cate):
    base_colors = {
        'AC': 'm', 
        'DC': 'mediumblue',
    }
    color = base_colors.get(cate, 'gray')
    lw = legend_line_style(cate, cap)
    
    return plt.Line2D([0, 2], [0, 0], color=color, lw=lw, marker='', linestyle='-')

line_handles = ([legend_line(cap, 'AC') for cap in ac_capacities] +
                [legend_line(cap, 'DC') for cap in dc_capacities])
line_labels  = ([f'AC {int(cap)} MW' for cap in ac_capacities] +
                [f'DC {int(cap)} MW' for cap in dc_capacities])


all_handles = energy_handles + line_handles
all_labels = ['Thermal', 'Hydropower', 'Nuclear', 'Solar PV', 'Wind'] + line_labels


legend = ax.legend(all_handles, all_labels, loc='lower left', 
                   bbox_to_anchor=(0.006, -0.005), ncol=3, fontsize=16,
                   frameon=True, framealpha=0.9, edgecolor='gray')


ax.set_xlim(70, 137)
ax.set_ylim(15, 55)




ax.set_xlabel('Longitude', fontsize=16, fontfamily='Times New Roman', labelpad=10)
ax.set_ylabel('Latitude', fontsize=16, fontfamily='Times New Roman', labelpad=10)
ax.xaxis.set_label_coords(0.5, -0.03)  
ax.yaxis.set_label_coords(-0.03, 0.5)  

plt.tight_layout()
plt.show()