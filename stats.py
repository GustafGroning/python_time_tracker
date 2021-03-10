import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import json
import array

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

    work = sum(workList)
    print(work)
    fun = sum(funList)
    print(fun)
    waste = sum(wasteList)
    print(type(waste))
    print(type(work))
    print(type(fun))
    pie_chart(work, fun, waste)



def pie_chart( work,fun, waste):

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'work', 'fun', 'waste'
    sizes = [work, fun, waste]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes,  labels=labels, autopct='%1.1f%%',
             startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()




get_stats()

