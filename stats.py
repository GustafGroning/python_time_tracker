import numpy as np 
from matplotlib import pyplot as plt 
import json


f = open('timeLog.json',) 
data = json.load(f) 

for i in data['timeSaved']:
    print(i['timeInMinutes']) #TODO: nu printar den alla värden i ordning! Nu ska den göra det enligt kategori och plusa, AKA ta allt "work" och lägg ihop.




"""
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#plt.show()
"""

"""
cirkeldiagram med tid spenderat i olika kategorier
"""