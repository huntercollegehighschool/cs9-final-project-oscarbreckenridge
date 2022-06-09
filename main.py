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
  choice = input("Enter B to enter the building, H to go back home")
  if choice == B:
    enterbuilding()
  elif choice == H:
    gohome()
  
def gohome():
  print("You went home, went to sleep, and woke up the next day. Try again!")
  start()

def enterbuilding():
  print("You have entered the building. You need to tap your student ID on the scanner, or fill out the google form to enter if your ID is not on you.")
  choice = input("Enter I to tap your ID, F to fill out the form.")
  if choice == I:
    tapid()
  if choice == F:
    form()

def tapid():
  print("You have now entered the building. After (\hopefully)\ wishing the security guards good morning, you make your way up the stairs to your locker. As a seventh grader, you only have three classes before lunch.")