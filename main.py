import json
from AppKit import NSWorkspace
import time
import timer as t


testList = ["Trello", "Safari"]
def check_window(): 
    first_window = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    while True:
        new_window = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        if new_window != first_window:
            check_category(new_window)
        else:
            print("no change")
            time.sleep(1)
# om användaren byter fönster, skicka till check_category

def check_category(new_window):
    f = open('categories.json',) 
    # returns JSON object as a dictionary 

    data = json.load(f) 
    categoryList = [] #stores all categories so the timer knows how to store the data.

    for item in data["categories"]:
        categoryList.append(item["appOrSite"])
    print(categoryList)


    if new_window in categoryList: #Safari, Onenote, Trello
        t.timer(new_window, category) #TODO: skapa category, det ska vara kategorin som 
        time.sleep(1)
    else:
        print ("why are you not working stupid?")
        time.sleep(1)
        check_window()


def add_category(category, appOrSite): # user inputs the category the new app or site is going into, followed by the full name of the app/site.
    jsonInput = {"category": category, "appOrSite": appOrSite}
    with open("categories.json", "w") as f:
        json.dump(jsonInput, f)
#TODO: just nu skriver add_category över tidigare rader, det ska den inte göra.


"""
# pröva en grej
f = open('categories.json',) 

# returns JSON object as  
# a dictionary 
data = json.load(f) 

# Iterating through the json list
#for i in data['categories']: 
 #   print(i) 

for i in range(0, 3):
    print(data['categories'][i]['appOrSite'])

f.close() 
"""

check_window()
