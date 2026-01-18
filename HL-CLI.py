#My first room in the adventure game

#procedures

def start():
  choice = None
  while choice not in ["a","b","c"]:
    print("You are a 27 year old MIT graduate called Dr. Gordon Freeman, and you are late to work. How do you get there?")
    print("a) - Ride the tram")
    print("b) - Drive your car")
    choice = input ("Your choice? ->")
    if choice == "a":
      print("You made it to work, you see a security guard (Barney) banging on a locked door, how strange.")
      #put appropriate actions here
    elif choice == "b":
      print("You can't get to work by driving, it's strictly forbidden as it's a security issue! Ride the tram")
      #put appropriate actions here
    else:
      print("That is not a valid choice")
      
def desk():
  choice = None
  while choice not in ["a","b","c"]:
    print("On your way to your location, you see nuclear missiles ready for transport to launch sites. Why are they there?, you think to yourself.")
    print("a) - Continue to loaction")
    choice = input ("Your choice? ->")
    if choice == "a":
      print("You arrive at work! You work in Anomalous Materials Laboratory, which is part of The Black Mesa Reseach Facility. Some scientests tell you to put on your HEV suit, in preparation for an experement.")
      #put appropriate actions here
    else:
      print("That is not a valid choice")


#main code
start()
desk()
