# library
import pdb
import json
import datetime
import numpy as np
import matplotlib.pyplot as plt

# exclusion_list = ['c', 'i', 'ro', 'r']
exclusion_list = ['c', 'i']

# Grab data
with open('data.json') as f:
    data = json.load(f)

with open('outbreaks.json') as f:
    outbreaks = json.load(f)

ob_map = {}
ob_dict = {}
for index, outbreak in enumerate(outbreaks):
    ob_id = outbreak['id']
    ob_name = outbreak['name']
    ob_from = outbreak.get('from', None)
    ob_map[index] = ob_id
    ob_dict[ob_id] = ob_name

outbreak_days = {d['date']:d for d in data}
outbreak_days_sorted = [x['date'] for x in data]
outbreak_days_sorted.sort()

x_list = []
y_list = []
y_list_labels = [ob_dict[ob_map[i]] for i in range(0, len(ob_map))]



for outbreak_date in outbreak_days_sorted:
    x = outbreak_days[outbreak_date]['date']
    x_list.append(x)


for i in range(0, len(ob_map)):

    ob_id = ob_map[i]

    mini_y_list = []
    for outbreak_date in outbreak_days_sorted:
        clust_dict = {c['id']: c for c in outbreak_days[outbreak_date]['clusters'] if c['id'] not in exclusion_list}
        
        total = clust_dict.get(ob_id, {}).get('total', None)

        if total is None:
            if len(mini_y_list) == 0:
                total = clust_dict.get(ob_id, {}).get('new', 0)
            else:
                # print('')
                # print(mini_y_list)
                # print(mini_y_list, type(mini_y_list[-1]), outbreak_date)
                total = clust_dict.get(ob_id, {}).get('new', 0) + mini_y_list[-1]
        
        mini_y_list.append(total)
        # pdb.set_trace()

    y_list.append(mini_y_list)



# pdb.set_trace()

# Your x and y axis

# Basic stacked area chart.
plt.stackplot(x_list,y_list, labels=[y for y in y_list_labels if y not in exclusion_list])
# plt.legend(loc='upper left')
plt.show()
 