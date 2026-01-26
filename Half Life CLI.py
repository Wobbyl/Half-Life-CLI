# Imports librarys / modules.
import time
import os

def intro():    # Code for start screen.
    print("Welcome to Half-Life CLI! What would you like to do? \n[E] Exit , [L] Load , [R] Run")
    action = input("-> ")
    if action == "E":   # Exits if user inputs "E".
        quit()
    elif action == "L":     # Starts the loader if user inputs "L".
        loader()
    elif action == "R":     # Starts from beginning if user inputs "R".
        chap1()
    else:
        print("Invalid input")  # Restarts program is the input isn't "E", "L" or "R".
        os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal.
        time.sleep(1)
        intro()

def loader():   # Loader script.
    print("Please input your save code.")
    savecode = input("-> ")
    if savecode == "4341":
        os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal.
        chap1()

def chap1():
    print("Black Mesa Inbound. Your save code is 4341.")

# Main Code
intro()