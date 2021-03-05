import json
from AppKit import NSWorkspace
import time

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
    if new_window in testList:
        print("this works!")
        time.sleep(1)
    else:
        print ("why are you not working stupid?")
        time.sleep(1)
        check_window()



# kollar om det nya fönstret/hemsidan hör till en kategori
# om NEJ, skicka tillbaka till check_window (för det här programmet ska inte trackas, check_window får då gå för evigt)
# om JA, skicka till timer


def timer(new_window):
    start_time = time.time()
    while True:
        newer_window = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        elapsed_time = time.time() - start_time
        if new_window != newer_window:
            print("you spent", elapsed_time, "in trello, good job!")
            check_window()
        else:
            time.sleep(1)
    
    
#timear sekunder som användaren är i fönstret
#om användaren byter fönster, skicka till time_log


def time_log():
    pass
# spara tid spenderad och kategori i JSON
# skicka till check_window

def add_category(category, appOrSite): # user inputs the category the new app or site is going into, followed by the full name of the app/site.
    jsonInput = {"category": category, "appOrSite": appOrSite}
    with open("categories.json", "w") as f:
        json.dump(jsonInput, f)
#TODO: just nu skriver add_category över tidigare rader, det ska den inte göra.

#check_window()

f = open('categories.json',) 

# returns JSON object as  
# a dictionary 
data = json.load(f) 

# Iterating through the json list
#for i in data['categories']: 
 #   print(i) 

for i in range(0, 3):
    print(data['categories'][i]['appOrSite'])





# Closing file 
f.close() 

