import numpy as np 
from matplotlib import pyplot as plt 
import json

# kanske bäst att hårdkoda ändå? så att man får listor på allt och sedan plusar ihop det?



f = open('timeLog.json',) 
    # returns JSON object as a dictionary 

data = json.load(f) 

print(data["timeSaved"][1]) #ettan blir visst vilken rad det gäller, men den vägrar fortfarande hitta det specifika värdet, aka timeInMinutes



"""
for item in data["categories"]:
    categoryList.append(item["appOrSite"])
print(categoryList)


timeSpent = {"work": 20, "fun": 30, "work": 45, "waste": 15}

for item in timeSpent:
    if item == "work":
        print("success!")
#print(timeSpent.get("work"))

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