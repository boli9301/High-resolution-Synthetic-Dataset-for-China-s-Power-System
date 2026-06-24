# The code is for generating Fig.7, including different regions and provinces.
# The Fig.7 in the paper is adjusted for aesthetics and readability

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 24

colors = ['k', 'deepskyblue', 'r', 'darkorange', 'limegreen']

energy_types = ['Thermal', 'Hydropower', 'Nuclear', 'Solar', 'Wind']
provinces    = ['Jiangsu', 'Zhejiang', 'Fujian', 'Shanghai', 'Anhui']
years        = ['2011', '2019', '2024']
def convert_to_gw(data_dict):
    for province in data_dict:
        for key in ['source', 'actual']:
            data_dict[province][key] = [x/1000 for x in data_dict[province][key]]
    return data_dict
data_2011 = {
    'Jiangsu' : {'source': [57077, 1103, 2120, 49, 1195],   'actual': [64800, 1140, 2120, 396, 1580]},
    'Zhejiang': {'source': [37386, 7830, 4406, 0, 197],     'actual': [46260, 9710, 4330, 8, 320]},
    'Fujian'  : {'source': [22111, 8447, 0, 0, 531],        'actual': [25100, 11250, 0, 0, 820]},
    'Shanghai': {'source': [18915, 0, 0, 7, 279],           'actual': [19430, 0, 0, 14, 210]},
    'Anhui'   : {'source': [27079, 1358, 0, 2, 250],        'actual': [29590, 2000, 0, 4, 200]}
}
data_2011 = convert_to_gw(data_2011)
data_2019 = {
    'Jiangsu' : {'source': [91801, 2603, 4371, 12554, 9600], 'actual': [100500, 2650, 4372, 14860, 10410]},
    'Zhejiang': {'source': [54854, 9600, 9608, 9226, 1510],  'actual': [62120, 11700, 9086, 13390, 1600]},
    'Fujian'  : {'source': [30741, 10008, 8712, 1347, 3067],  'actual': [31720, 13210, 8712, 1690, 3760]},
    'Shanghai': {'source': [21789, 0, 0, 459, 747],         'actual': [24750, 0, 0, 1090, 810]},
    'Anhui'   : {'source': [51079, 2585, 0, 8384, 2700],    'actual': [55210, 3450, 0, 12540, 2740]}
}
data_2019 = convert_to_gw(data_2019)
data_2024 = {
    'Jiangsu' : {'source': [100993, 2603, 6608, 14696, 22230], 'actual': [109520, 2751, 6610, 61647, 23210]},
    'Zhejiang': {'source': [62737, 13103, 9608, 11741, 5579],  'actual': [71650, 14980, 9170, 47275, 7241]},
    'Fujian'  : {'source': [35143, 13808, 11012, 2005, 7833],  'actual': [38546, 17200, 12220, 12583, 8540]},
    'Shanghai': {'source': [24643, 0, 0, 689, 998],          'actual': [25575, 0, 0, 4114, 1067]},
    'Anhui'   : {'source': [57258, 5600, 0, 14072, 6831],   'actual': [63130, 6498, 0, 43113, 9077]}
}
data_2024 = convert_to_gw(data_2024)
fig, ax = plt.subplots(figsize=(16, 8))

bar_width = 0.15
group_width = bar_width * 6
n_provinces = len(provinces)
n_years = len(years)

index = np.arange(n_provinces * n_years)

actual_legend_added = False

for i, province in enumerate(provinces):
    for j, year in enumerate(years):
        data = globals()[f'data_{year}']
        pos = i * n_years + j
        
        for k, energy_type in enumerate(energy_types):
          
            x_pos = pos + k * bar_width - (bar_width * 2)
            
           
            source_value = data[province]['source'][k]
            actual_value = data[province]['actual'][k]
            
           
            ax.bar(x_pos, source_value, bar_width,
                   color=colors[k], alpha=0.7, label=energy_type if (i == 0 and j == 0) else "")
            
           
            if not actual_legend_added:
                ax.plot(x_pos, actual_value, 'o', 
                       markersize=8, color='darkred', markeredgecolor='white', markeredgewidth=1,
                       label='Actual Capacity')
                actual_legend_added = True
            else:
                ax.plot(x_pos, actual_value, 'o', 
                       markersize=8, color='darkred', markeredgecolor='white', markeredgewidth=1)

ax.set_ylabel('Capacity (GW)', fontsize=24, fontname='Times New Roman')

handles, labels = ax.get_legend_handles_labels()

unique_handles = []
unique_labels = []
seen_labels = set()

for handle, label in zip(handles, labels):
    if label not in seen_labels:
        seen_labels.add(label)
        unique_handles.append(handle)
        unique_labels.append(label)

ax.legend(unique_handles, unique_labels, title='Energy Type (East)', 
          title_fontproperties={'family': 'Times New Roman', 'size': 24},
          prop={'family': 'Times New Roman'})

plt.tight_layout()
plt.show()





import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 24

colors = ['k', 'deepskyblue', 'r', 'darkorange', 'limegreen']

energy_types = ['Thermal', 'Hydropower', 'Nuclear', 'Solar', 'Wind']

provinces    = ['Sichuan', 'Chongqing', 'Hunan', 'Hubei', 'Henan', 'Jiangxi']
years        = ['2011', '2019', '2024']
def convert_to_gw(data_dict):
    for province in data_dict:
        for key in ['source', 'actual']:
            data_dict[province][key] = [x/1000 for x in data_dict[province][key]]
    return data_dict
data_2011 = {
    'Sichuan'   : {'source': [9460, 35372, 0, 0, 62],    'actual': [14440, 33420, 0, 0, 20]},
    'Chongqing' : {'source': [4884, 5885, 0, 0, 49],     'actual': [6940, 5980, 0, 0, 50]},
    'Hunan'     : {'source': [14565, 11045, 0, 0, 36],   'actual': [17650, 13370, 0, 0, 106]},
    'Hubei'     : {'source': [16161, 37921, 0, 1, 115],  'actual': [19180, 33860, 0, 3, 100]},
    'Henan'     : {'source': [41910, 4022, 0, 0, 177],   'actual': [49190, 3950, 0, 0, 110]},
    'Jiangxi'   : {'source': [12250, 3057, 0, 0, 134],   'actual': [13820, 4110, 0, 7, 130]}
}
data_2011 = convert_to_gw(data_2011)
data_2019 = {
    'Sichuan'   : {'source': [12171, 84933, 0, 1748, 2940], 'actual': [15700, 78460, 0, 1880, 3250]},
    'Chongqing' : {'source': [14251, 6467, 0, 473, 601],    'actual': [15480, 7720, 0, 650, 640]},
    'Hunan'     : {'source': [19069, 12879, 0, 2504, 4476],  'actual': [22800, 16120, 0, 3440, 4270]},
    'Hubei'     : {'source': [28905, 38561, 0, 5793, 3742], 'actual': [31570, 36790, 0, 6210, 4050]},
    'Henan'     : {'source': [65343, 4027, 0, 5661, 5015],   'actual': [70500, 4080, 0, 10540, 7940]},
    'Jiangxi'   : {'source': [19449, 8741, 0, 4586, 2773],   'actual': [22050, 6610, 0, 6300, 2860]}
}
data_2019 = convert_to_gw(data_2019)
data_2024 = {
    'Sichuan'   : {'source': [14609, 114558, 0, 7511, 7107],  'actual': [21470, 97700, 0, 10823, 8930]},
    'Chongqing' : {'source': [16045, 9172, 0, 973, 1299],     'actual': [17493, 8886, 0, 3098, 2600]},
    'Hunan'     : {'source': [25612, 16199, 0, 5921, 10038],  'actual': [28953, 16370, 0, 18734, 10457]},
    'Hubei'     : {'source': [37821, 39421, 0, 22201, 8501], 'actual': [40775, 38120, 0, 35100, 9594]},
    'Henan'     : {'source': [71698, 7227, 0, 6430, 20283],   'actual': [74210, 5981, 0, 43491, 23340]},
    'Jiangxi'   : {'source': [28904, 8874, 0, 15455, 5766],   'actual': [31610, 7609, 0, 25639, 6684]}
}
data_2024 = convert_to_gw(data_2024)

fig, ax = plt.subplots(figsize=(16, 8))

bar_width = 0.15
group_width = bar_width * 6
n_provinces = len(provinces)
n_years = len(years)


index = np.arange(n_provinces * n_years)


actual_legend_added = False

for i, province in enumerate(provinces):
    for j, year in enumerate(years):
        data = globals()[f'data_{year}']
        pos = i * n_years + j
        
        for k, energy_type in enumerate(energy_types):
         
            x_pos = pos + k * bar_width - (bar_width * 2)
            
        
            source_value = data[province]['source'][k]
            actual_value = data[province]['actual'][k]
            
          
            ax.bar(x_pos, source_value, bar_width,
                   color=colors[k], alpha=0.7, label=energy_type if (i == 0 and j == 0) else "")
            
            if not actual_legend_added:
                ax.plot(x_pos, actual_value, 'o', 
                       markersize=8, color='darkred', markeredgecolor='white', markeredgewidth=1,
                       label='Actual Capacity')
                actual_legend_added = True
            else:
                ax.plot(x_pos, actual_value, 'o', 
                       markersize=8, color='darkred', markeredgecolor='white', markeredgewidth=1)

ax.set_ylabel('Capacity (GW)', fontsize=24, fontname='Times New Roman')
handles, labels = ax.get_legend_handles_labels()
unique_handles = []
unique_labels = []
seen_labels = set()

for handle, label in zip(handles, labels):
    if label not in seen_labels:
        seen_labels.add(label)
        unique_handles.append(handle)
        unique_labels.append(label)

ax.legend(unique_handles, unique_labels, title='Energy Type (Mid)', 
          title_fontproperties={'family': 'Times New Roman', 'size': 24},
          prop={'family': 'Times New Roman'})

plt.tight_layout()
plt.show()




import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 24

colors = ['k', 'deepskyblue', 'r', 'darkorange', 'limegreen']

energy_types = ['Thermal', 'Hydropower', 'Nuclear', 'Solar', 'Wind']

provinces    = ['Inner_Mongolia', 'Beijing', 'Tianjin', 'Hebei', 'Shanxi', 'Shandong']
years        = ['2011', '2019', '2024']
def convert_to_gw(data_dict):
    for province in data_dict:
        for key in ['source', 'actual']:
            data_dict[province][key] = [x/1000 for x in data_dict[province][key]]
    return data_dict
data_2011 = {
    'Inner_Mongolia': {'source': [55480, 1432, 0, 40, 12666],  'actual': [59550, 850, 0, 87, 14570]},
    'Beijing'       : {'source': [3843, 1010, 0, 0, 136],      'actual': [5140, 1050, 0, 0, 150]},
    'Tianjin'       : {'source': [9507, 0, 0, 0, 238],         'actual': [10830, 0, 0, 0, 130]},
    'Hebei'         : {'source': [32429, 1649, 0, 0, 4132],    'actual': [38100, 1790, 0, 147, 4470]},
    'Shanxi'        : {'source': [39625, 2519, 0, 0, 843],     'actual': [46510, 2430, 0, 27, 900]},
    'Shandong'      : {'source': [46568, 1006, 0, 54, 2001],   'actual': [64480, 1069, 0, 37, 2460]}
}
data_2011 = convert_to_gw(data_2011)
data_2019 = {
    'Inner_Mongolia': {'source': [87109, 3177, 0, 10972, 28909], 'actual': [87210, 2390, 0, 10510, 29200]},
    'Beijing'       : {'source': [10289, 1010, 0, 260, 186],     'actual': [11350, 990, 0, 510, 190]},
    'Tianjin'       : {'source': [15649, 0, 0, 1545, 612],       'actual': [16390, 10, 0, 1430, 600]},
    'Hebei'         : {'source': [47253, 1699, 0, 15480, 16130], 'actual': [50210, 1820, 0, 14740, 16390]},
    'Shanxi'        : {'source': [61796, 2940, 0, 9123, 13381],  'actual': [66870, 2230, 0, 10880, 12510]},
    'Shandong'      : {'source': [91434, 1006, 2500, 17002, 13706], 'actual': [107130, 1080, 2500, 16190, 13540]}
}
data_2019 = convert_to_gw(data_2019)
data_2024 = {
    'Inner_Mongolia': {'source': [118095, 3432, 0, 36598, 78355], 'actual': [121070, 2620, 0, 48109, 85990]},
    'Beijing'       : {'source': [10498, 1010, 0, 260, 236],      'actual': [11520, 1017, 0, 1303, 236.5]},
    'Tianjin'       : {'source': [17222, 0, 0, 4904, 1566],       'actual': [18990, 10, 0, 7241, 2072]},
    'Hebei'         : {'source': [41312, 8899, 0, 25823, 28131],  'actual': [56471, 6334, 0, 72024, 38090]},
    'Shanxi'        : {'source': [77282, 2940, 0, 24243, 24481],  'actual': [81980, 3054, 0, 34768, 26160]},
    'Shandong'      : {'source': [107863, 4006, 2711, 26149, 24946], 'actual': [121220, 4272, 4180, 76134, 26690]}
}
data_2024 = convert_to_gw(data_2024)
fig, ax = plt.subplots(figsize=(16, 8))

bar_width = 0.15
group_width = bar_width * 6
n_provinces = len(provinces)
n_years = len(years)

index = np.arange(n_provinces * n_years)
actual_legend_added = False

for i, province in enumerate(provinces):
    for j, year in enumerate(years):
        data = globals()[f'data_{year}']
        pos = i * n_years + j
        
        for k, energy_type in enumerate(energy_types):
            
            x_pos = pos + k * bar_width - (bar_width * 2)
            
            
            source_value = data[province]['source'][k]
            actual_value = data[province]['actual'][k]
            
            ax.bar(x_pos, source_value, bar_width,
                   color=colors[k], alpha=0.7, label=energy_type if (i == 0 and j == 0) else "")
            
            if not actual_legend_added:
                ax.plot(x_pos, actual_value, 'o', 
                       markersize=8, color='darkred', markeredgecolor='white', markeredgewidth=1,
                       label='Actual Capacity')
                actual_legend_added = True
            else:
                ax.plot(x_pos, actual_value, 'o', 
                       markersize=8, color='darkred', markeredgecolor='white', markeredgewidth=1)

ax.set_ylabel('Capacity (GW)', fontsize=24, fontname='Times New Roman')
handles, labels = ax.get_legend_handles_labels()

unique_handles = []
unique_labels = []
seen_labels = set()

for handle, label in zip(handles, labels):
    if label not in seen_labels:
        seen_labels.add(label)
        unique_handles.append(handle)
        unique_labels.append(label)

ax.legend(unique_handles, unique_labels, title='Energy Type (North)', 
          title_fontproperties={'family': 'Times New Roman', 'size': 24},
          prop={'family': 'Times New Roman'})

plt.tight_layout()
plt.show()




import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 24

colors = ['k', 'deepskyblue', 'r', 'darkorange', 'limegreen']

energy_types = ['Thermal', 'Hydropower', 'Nuclear', 'Solar', 'Wind']

provinces = [ 'Jilin', 'Liaoning', 'Heilongjiang']
years = ['2011', '2019', '2024']

def convert_to_gw(data_dict):
    for province in data_dict:
        for key in ['source', 'actual']:
            data_dict[province][key] = [x/1000 for x in data_dict[province][key]]
    return data_dict

data_2011 = {
    'Jilin': {'source': [12631, 7055, 0, 0, 2859], 'actual': [15870, 4330, 0, 0, 2850]},
    'Liaoning': {'source': [23297, 2618, 0, 0, 3227], 'actual': [28510, 1470, 0, 0, 4020]},
    'Heilongjiang': {'source': [13905, 1060, 0, 0, 2512], 'actual': [17370, 960, 0, 0, 2550]}
}
data_2011 = convert_to_gw(data_2011)
data_2019 = {
    'Jilin': {'source': [16580, 7210, 0, 2803, 4882], 'actual': [18450, 4450, 0, 2740, 5570]},
    'Liaoning': {'source': [30211, 4227, 4476, 1851, 7639], 'actual': [34460, 3020, 4476, 3430, 8320]},
    'Heilongjiang': {'source': [18670, 1173, 0, 2522, 5877], 'actual': [22530, 1080, 0, 2740, 6110]}
}
data_2019 = convert_to_gw(data_2019)
data_2024 = {
    'Jilin': {'source': [17292, 10090, 0, 4259, 12151], 'actual': [18903, 6991, 0, 5830, 14550]},
    'Liaoning': {'source': [34618, 6027, 6714, 4498, 12996], 'actual': [39610, 4244, 6680, 12139, 15860]},
    'Heilongjiang': {'source': [22034, 2373, 0, 5108, 10790], 'actual': [25770, 2650, 0, 7171, 13861]}
}
data_2024 = convert_to_gw(data_2024)
fig, ax = plt.subplots(figsize=(16, 8))

bar_width = 0.15
group_width = bar_width * 6
n_provinces = len(provinces)
n_years = len(years)

index = np.arange(n_provinces * n_years)

actual_legend_added = False

for i, province in enumerate(provinces):
    for j, year in enumerate(years):
        data = globals()[f'data_{year}']
        pos = i * n_years + j
        
        for k, energy_type in enumerate(energy_types):
           
            x_pos = pos + k * bar_width - (bar_width * 2)
            
           
            source_value = data[province]['source'][k]
            actual_value = data[province]['actual'][k]
            
    
            ax.bar(x_pos, source_value, bar_width,
                   color=colors[k], alpha=0.7, label=energy_type if (i == 0 and j == 0) else "")
            
            if not actual_legend_added:
                ax.plot(x_pos, actual_value, 'o', 
                       markersize=8, color='darkred', markeredgecolor='white', markeredgewidth=1,
                       label='Actual Capacity')
                actual_legend_added = True
            else:
                ax.plot(x_pos, actual_value, 'o', 
                       markersize=8, color='darkred', markeredgecolor='white', markeredgewidth=1)

ax.set_ylabel('Capacity (GW)')
handles, labels = ax.get_legend_handles_labels()

unique_handles = []
unique_labels = []
seen_labels = set()

for handle, label in zip(handles, labels):
    if label not in seen_labels:
        seen_labels.add(label)
        unique_handles.append(handle)
        unique_labels.append(label)

ax.legend(unique_handles, unique_labels, title='Energy Type (Northeast)')

plt.tight_layout()
plt.show()




import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 24

colors = ['k', 'deepskyblue', 'r', 'darkorange', 'limegreen']

energy_types = ['Thermal', 'Hydropower', 'Nuclear', 'Solar', 'Wind']

provinces = ['Guangdong', 'Guangxi', 'Yunnan', 'Guizhou', 'Hainan']
years = ['2011', '2019', '2024']
def convert_to_gw(data_dict):
    for province in data_dict:
        for key in ['source', 'actual']:
            data_dict[province][key] = [x/1000 for x in data_dict[province][key]]
    return data_dict
# 2011
data_2011 = {
    'Guangdong': {'source': [54346, 10939, 6120, 0, 1044],  'actual': [56350, 13020, 6120, 8, 740]},
    'Guangxi'  : {'source': [9995, 17778, 0, 0, 50],        'actual': [11770, 15260, 0, 0, 250]},
    'Yunnan'   : {'source': [9124, 23467, 0, 0, 754],       'actual': [11360, 28420, 0, 20, 670]},
    'Guizhou'  : {'source': [17740, 20848, 0, 0, 248],      'actual': [20300, 18660, 0, 0, 40]},
    'Hainan'   : {'source': [2406, 483, 0, 0, 248],         'actual': [3150, 810, 0, 25, 250]}
}
data_2011 = convert_to_gw(data_2011)
# 2019
data_2019 = {
    'Guangdong': {'source': [81933, 13714, 16136, 3156, 4043], 'actual': [86280, 15760, 16136, 6100, 4410]},
    'Guangxi'  : {'source': [20468, 20200, 2712, 1702, 1991],  'actual': [22940, 16810, 2172, 1350, 2870]},
    'Yunnan'   : {'source': [11236, 73012, 0, 3675, 8339],    'actual': [15090, 68730, 0, 3750, 8630]},
    'Guizhou'  : {'source': [32420, 24502, 0, 4465, 4046],    'actual': [34100, 22230, 0, 5100, 4570]},
    'Hainan'   : {'source': [3830, 1083, 1300, 984, 248],     'actual': [4650, 1540, 1300, 1400, 290]}
}
data_2019 = convert_to_gw(data_2019)
data_2024 = {
    'Guangdong': {'source': [109574, 18626, 16136, 16569, 15326], 'actual': [127400, 19050, 16140, 41155, 18080]},
    'Guangxi'  : {'source': [29256, 21800, 4532, 13866, 12217],  'actual': [31850, 19040, 4530, 20523, 18080]},
    'Yunnan'   : {'source': [11382, 83212, 0, 34054, 16582],    'actual': [14560, 83600, 0, 37230, 18810]},
    'Guizhou'  : {'source': [36015, 24645, 0, 19507, 6686],    'actual': [39990, 22980, 0, 19856, 8600]},
    'Hainan'   : {'source': [7797, 1083, 1300, 2801, 868],     'actual': [10010, 1740, 1300, 7408, 360]}
}
data_2024 = convert_to_gw(data_2024)

fig, ax = plt.subplots(figsize=(16, 8))
bar_width = 0.15
group_width = bar_width * 6
n_provinces = len(provinces)
n_years = len(years)

index = np.arange(n_provinces * n_years)

actual_legend_added = False

for i, province in enumerate(provinces):
    for j, year in enumerate(years):
        data = globals()[f'data_{year}']
        pos = i * n_years + j
        
        for k, energy_type in enumerate(energy_types):

            x_pos = pos + k * bar_width - (bar_width * 2)
 
            source_value = data[province]['source'][k]
            actual_value = data[province]['actual'][k]

            ax.bar(x_pos, source_value, bar_width,
                   color=colors[k], alpha=0.7, label=energy_type if (i == 0 and j == 0) else "")
            
            if not actual_legend_added:
                ax.plot(x_pos, actual_value, 'o', 
                       markersize=8, color='darkred', markeredgecolor='white', markeredgewidth=1,
                       label='Actual Capacity')
                actual_legend_added = True
            else:
                ax.plot(x_pos, actual_value, 'o', 
                       markersize=8, color='darkred', markeredgecolor='white', markeredgewidth=1)

ax.set_ylabel('Capacity (GW)', fontsize=24, fontname='Times New Roman')

handles, labels = ax.get_legend_handles_labels()

unique_handles = []
unique_labels = []
seen_labels = set()

for handle, label in zip(handles, labels):
    if label not in seen_labels:
        seen_labels.add(label)
        unique_handles.append(handle)
        unique_labels.append(label)

ax.legend(unique_handles, unique_labels, title='Energy Type (South)', 
          title_fontproperties={'family': 'Times New Roman', 'size': 24},
          prop={'family': 'Times New Roman'})

plt.tight_layout()
plt.show()





import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 24

colors = ['k', 'deepskyblue', 'r', 'darkorange', 'limegreen']
energy_types = ['Thermal', 'Hydropower', 'Nuclear', 'Solar', 'Wind']

provinces    = ['Xinjiang', 'Gansu', 'Qinghai', 'Shanxi', 'Ningxia', 'Xizang']
years        = ['2011', '2019', '2024']
def convert_to_gw(data_dict):
    for province in data_dict:
        for key in ['source', 'actual']:
            data_dict[province][key] = [x/1000 for x in data_dict[province][key]]
    return data_dict
# 2011
data_2011 = {
    'Xinjiang' : {'source': [10334, 2899, 0, 145, 1099],  'actual': [16230, 3270, 0, 5, 1880]},
    'Gansu'    : {'source': [14170, 5809, 0, 138, 4894],  'actual': [15240, 6550, 0, 111, 5550]},
    'Qinghai'  : {'source': [1140, 11856, 0, 355, 50],    'actual': [2300, 10960, 0, 938, 20]},
    'Shanxi'   : {'source': [39625, 2519, 0, 0, 843],     'actual': [46510, 2430, 0, 27, 900]},
    'Ningxia'  : {'source': [16154, 392, 0, 280, 1218],   'actual': [16400, 430, 0, 491, 1170]},
    'Xizang'   : {'source': [180, 488, 0, 40, 0],         'actual': [370, 540, 0, 66, 0]}
}
data_2011 = convert_to_gw(data_2011)
# 2019
data_2019 = {
    'Xinjiang' : {'source': [58779, 7132, 0, 14205, 19107], 'actual': [58130, 7730, 0, 10720, 19560]},
    'Gansu'    : {'source': [19700, 7590, 0, 9011, 12387],  'actual': [21040, 9430, 0, 9240, 12970]},
    'Qinghai'  : {'source': [3260, 12221, 0, 15810, 4465],  'actual': [3930, 11920, 0, 11220, 4620]},
    'Shanxi'   : {'source': [61796, 2940, 0, 9123, 13381],  'actual': [66870, 2230, 0, 10880, 12510]},
    'Ningxia'  : {'source': [29770, 392, 0, 9490, 10124],   'actual': [32190, 430, 0, 9180, 11160]},
    'Xizang'   : {'source': [180, 1547, 0, 1132, 50],       'actual': [420, 1700, 0, 1100, 10]}
}
data_2019 = convert_to_gw(data_2019)
# 2024
data_2024 = {
    'Xinjiang' : {'source': [73006, 10598, 0, 58364, 39091], 'actual': [77080, 11531, 0, 56748, 47080]},
    'Gansu'    : {'source': [23757, 7594, 0, 25551, 28771],  'actual': [25111, 10518, 0, 31388, 32150]},
    'Qinghai'  : {'source': [3424, 15654, 0, 32936, 8728],   'actual': [4125, 16400, 0, 36420, 12683]},
    'Shanxi'   : {'source': [77282, 2940, 0, 24243, 24481],  'actual': [81980, 3054, 0, 34768, 26160]},
    'Ningxia'  : {'source': [31865, 392, 0, 23242, 14428],   'actual': [33300, 427, 0, 26240, 15805]},
    'Xizang'   : {'source': [180, 3810, 0, 3177, 522],       'actual': [428, 3134, 0, 4039, 180]}
}
data_2024 = convert_to_gw(data_2024)
fig, ax = plt.subplots(figsize=(16, 8))

bar_width = 0.15
group_width = bar_width * 6
n_provinces = len(provinces)
n_years = len(years)

index = np.arange(n_provinces * n_years)

actual_legend_added = False

for i, province in enumerate(provinces):
    for j, year in enumerate(years):
        data = globals()[f'data_{year}']
        pos = i * n_years + j
        
        for k, energy_type in enumerate(energy_types):
  
            x_pos = pos + k * bar_width - (bar_width * 2)
          
            source_value = data[province]['source'][k]
            actual_value = data[province]['actual'][k]
            
    
            ax.bar(x_pos, source_value, bar_width,
                   color=colors[k], alpha=0.7, label=energy_type if (i == 0 and j == 0) else "")
            
            if not actual_legend_added:
                ax.plot(x_pos, actual_value, 'o', 
                       markersize=8, color='darkred', markeredgecolor='white', markeredgewidth=1,
                       label='Actual Capacity')
                actual_legend_added = True
            else:
                ax.plot(x_pos, actual_value, 'o', 
                       markersize=8, color='darkred', markeredgecolor='white', markeredgewidth=1)
ax.set_ylabel('Capacity (GW)', fontsize=24, fontname='Times New Roman')

handles, labels = ax.get_legend_handles_labels()
unique_handles = []
unique_labels = []
seen_labels = set()

for handle, label in zip(handles, labels):
    if label not in seen_labels:
        seen_labels.add(label)
        unique_handles.append(handle)
        unique_labels.append(label)

ax.legend(unique_handles, unique_labels, title='Energy Type (West)', 
          title_fontproperties={'family': 'Times New Roman', 'size': 24},
          prop={'family': 'Times New Roman'})
plt.tight_layout()
plt.show()