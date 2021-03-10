import numpy as np 
from matplotlib import pyplot as plt 
import json


f = open('timeLog.json',) 
data = json.load(f) 

def get_stats():
    workList = []
    funList = []
    wasteList = []

    for i in data['timeSaved']:
        if (i)['category'] == "work": # i blir alltså raden som den printar ifrån, timeInMinutes väljer vilket värde som ska printas.
            workList.append(i['timeInMinutes'])
        

        if (i)['category'] == "fun":
            funList.append(i['timeInMinutes'])
        

        if (i)['category'] == "waste":
            wasteList.append(i['timeInMinutes'])
        

    print("you have worked for ", sum(workList))
    print("you had fun for ", sum(funList))
    print("you wasted ", sum(wasteList))
    pie_chart(workList, funList, wasteList)



def pie_chart(workList,funList,wasteList):
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'work', 'fun', 'waste'
    sizes = [workList, funList, wasteList]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'fun')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


get_stats()

"""
cirkeldiagram med tid spenderat i olika kategorier
"""