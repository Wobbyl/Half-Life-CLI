# Imports librarys / modules.
import time
import os
import sys

def tprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)

def intro():    # Code for start screen.
    print("Welcome to Half-Life CLI! What would you like to do? \n[E] Exit , [L] Load , [R] Run")
    action = input("-> ")
    if action == "E" or action == "e":   # Exits if user inputs "E".
        quit()
    elif action == "L" or action == "l":     # Starts the loader if user inputs "L".
        loader()
    elif action == "R" or action == "r":     # Starts from beginning if user inputs "R".
        chap1start()
    else:
        print("Invalid input")  # Restarts program is the input isn't "E", "L" or "R".
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal.
        intro()

def loader():   # Loader script.
    print("Please input your save code.")
    savecode = input("-> ")
    if savecode == "4341":
        os.system('cls' if os.name == 'nt' else 'clear')
        chap1start()
    elif savecode == "5353":
        os.system('cls' if os.name == 'nt' else 'clear')
        chap2start()
    else:
        print("Invalid input")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        loader()

# CHAPTER 1 - BLACK MESA INBOUND.

def chap1start():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("BLACK MESA INBOUND.\nYour save code is 4341.")
    time.sleep(1)
    dismiss = input("Continue? [y/N] ")
    if dismiss == "Y" or dismiss == "y":
        chap1()
    elif dismiss == "N" or dismiss == "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        intro()
    else:
        print("Invalid Input!")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        chap1start()

def chap1():
    os.system('cls' if os.name == 'nt' else 'clear')
    tprint("SUBJECT: GORDON FREEMAN, MALE, AGE 27.")
    time.sleep(0.4)
    tprint("\nEDUCATION: PH.D., MIT, Theoretical Physics.")
    time.sleep(0.4)
    tprint("\nPOSITION: Research Associate.")
    time.sleep(0.4)
    tprint("\n\nLate for work, you board the tram at the Black Mesa Research Facility to get to your office, the test labs in sector C. Passing by, you see Barney the security guard banging on a door. As you get closer to your destination, you see a mysterious man in a suit staring at you from a distance. Strange.")
    time.sleep(0.4)
    chap1options()


def chap1options():
    options = input("Anomolous Materials [A]")
    if options == "A" or options == "A":
        chap2start()
    else:
        chap1options()

# CHAPTER 2 - ANOMOLOUS MATERIALS.

def chap2start():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("ANOMALOUS MATERIALS.\nYour save code is 5353.")
    time.sleep(1)
    dismiss = input("Continue? [y/N] ")
    if dismiss == "Y" or dismiss == "y":
        chap2()
    elif dismiss == "N" or dismiss == "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        intro()
    else:
        print("Invalid Input!")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        chap2start()
    
    def chap2():
        tprint("super cool second chapter")


# Main Code
intro()