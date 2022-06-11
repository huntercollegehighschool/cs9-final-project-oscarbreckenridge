"""
Name(s): Oscar Breckenridge
Name of Project: A Day At Hunter: Choose Your Own Adventure
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

def start():
  print("Welcome to your first day at Hunter College High School! We all have very busy schedules, so you will have to navigate your way around and make your own decisions. Best of Luck!")
  choice = input("Enter B to enter the building, H to go back home: ")
  if choice == "B":
    enterbuilding()
  elif choice == "H":
    gohome()
  
def gohome():
  print("You went home, went to sleep, and woke up the next day. Try again!")
  start()


def enterbuilding():
  print("You have entered the building. You need to tap your student ID on the scanner, or fill out the google form to enter if your ID is not on you.")
  choice = input("Enter I to tap your ID, F to fill out the form: ")
  if choice == "I":
    tapid()
  if choice == "F":
    form()

def form():
  print("You have waited in line and it is now your turn at the laptop. A google form is open to fill out your ID number")
  choice = int(input("Enter your graduating class: "))
  if choice >= 2022:
    idnumber = int(input("Enter your number without the graduating class: "))
    if idnumber > 0:
      tapid()
    else:
      print("You have been deemed not a student of Hunter College High School. The security guards grab you by your arm and escort you out of the building. They throw you into Madison Avenue where you are run over by the M1 Bus. Battered and bruised, you return home for the day. Try again!")
      start()
  else:
    print("You have been deemed not a student of Hunter College High School. The security guards grab you by your arm and escort you out of the building. They throw you into Madison Avenue where you are run over by the M1 Bus. Battered and bruised, you return home for the day. Try again!")
    start()

def classmorning():
  print("You have arrived at your first morning of classes! Make sure to stay awake, take notes, and participate!")
  print("10:30 AM.")
  print("You have survived your first three classes.")
  lunch()

def skipclass():
  print("You have chosen to skip class. Do you want to spend your class periods at the library or in the locker hallway?")
  choice = input("Enter L to go to the library, W to go to the locker hallway: ")
  if choice == "L":
    library()
  if choice == "W":
    lockerhallway()

def tapid():
  print("You have been granted access to enter the building. After hopefully wishing the security guards good morning, you make your way up the stairs to your locker. As a seventh grader, you only have three classes before lunch.")
  choice = input("Enter C to go to class, S to skip class: ")
  if choice == "C":
    classmorning()
  if choice == "S":
    skipclass()

def library():
  print("You decide to go to the library during your class time. While this may not be the smartest decision, as you haven't actually learned anything in class yet that you could study, but you use this time wisely and finish up your homework for the coming night. You work in the back corner of the Quiet Study room, and aren't noticed.")
  print("10:30 AM.")
  lunch()

def lockerhallway():
    print("here's some random stuff")
    lunch()


def lunch():
  print("It is now lunch period. You follow a new friend to Little Luzzo's to get a $6 special. You bring your pizza to the turf to eat.")
  print("Once you have eaten, your friend invites you to play in a pickup basketball game.")
  choice = input("Enter P to play. R to reject the invite: ")
  if choice == "P":
    basketball()
  if choice == "R":
    print("You have rejected your friend's offer to play basketball. Once Activities period starts, you witness the kids get kicked off the court by some seniors who didn't make the Varsity Team.")
    print("At 11:50, you make your way towards the school building for your afternoon classes.")
    classafternoon()

def basketball():
  print("You have joined the basketball game! As a casual player you contribute to your team by playing good defense, passing the ball, and giving players that make shots high-fives. A player on the other team sets a screen on your teammate, and you switch onto defending middle school basketball team star Schmeel Schmathur")
  print("Schmeel calls an isolation on you, calling you trash. Do you stay on defense or call for help defense?")
  choice = input("Enter O to stay in isolation against Schmeel, D to call for help defense: ")
  if choice == "O":
    iso()
  if choice == "D":
    helpdefense()

start()
#variables used: B H I F C S L W P R O D