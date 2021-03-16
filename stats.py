import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import json
import array
from datetime import date


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
        

    work = sum(workList)
    fun = sum(funList)
    waste = sum(wasteList)
    # sums time spent in each category, sends to pie_chart for plotting.

    pie_chart(work, fun, waste)
    bar_chart(work, fun, waste)


def pie_chart( work,fun, waste): #the pie shows % time spent in each category

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'work', 'fun', 'waste'
    sizes = [work, fun, waste]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes,  labels=labels, autopct='%1.1f%%',
             startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Time spent in different categories')
    plt.show()

    bar_chart(work, fun, waste)

def bar_chart(work, fun, waste): #bar shows amount of time spent, in minutes


    minutesWorked = [work, fun, waste]
    bars = ('work', 'fun', 'waste')
    x_pos = np.arange(len(bars))

    plt.bar(x_pos, minutesWorked, color = ("red", "blue", "green"))

    plt.title('Time spent in minutes')
    plt.xlabel('')
    plt.ylabel('values')

    plt.xticks(x_pos, bars)

    plt.show()

    
today = date.today()
print(today)

