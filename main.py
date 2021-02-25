
from AppKit import NSWorkspace
import time
#active_app_name = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
#print (active_app_name)



#from distutils.sysconfig import get_python_lib
#print(get_python_lib())

def check_window(): 
    active_window = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    while True:
        new_window = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        if new_window != active_window:
            check_category(new_window)
        else:
            print("no change")
            time.sleep(2)
# om användaren byter fönster, skicka till check_category


def check_category(new_window):
    if new_window == "Trello":
        print ("you're in trello, good job!")
        time.sleep(2)
        check_window()
    else:
        print ("why are you not working stupid?")
        time.sleep(2)
        check_window()

# kollar om det nya fönstret/hemsidan hör till en kategori
# om NEJ, skicka tillbaka till check_window (för det här programmet ska inte trackas, check_window får då gå för evigt)
# om JA, skicka till timer


def timer():
    pass
#timear sekunder som användaren är i fönstret
#om användaren byter fönster, skicka till time_log


def time_log():
    pass
# spara tid spenderad och kategori i JSON
# skicka till check_window

check_window()