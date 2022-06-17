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
  print("You have been granted access to enter the building. After hopefully wishing the security guards good morning, you make your way up the stairs to your locker. As a seventh grader, you only have three classes before lunch, in rooms 424, 308, and 206")
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
  print("You have decided to spend your class time in your locker hallway. You are on your phone, eating a snack you brought when a teacher confronts you.")
  print("Teacher: \"Excuse me, you can't eat in the locker hallway. What classroom are you supposed to be in?\"")
  choice = int(input("Enter a room number, or enter 0 to say you have a free period. "))
  if choice == 424 or choice == 308 or choice == 206:
    print("Teacher: \"Why aren't you in the class right now? Do you need me to show you where it is?\"")
    print("The teacher shows you to your classroom. You tell the teacher you got lost, and they say it isn't a problem and direct you to your seat.")
    classmorning()
  if choice >= 202 and choice < 434 and choice != 424 and choice != 308 and choice != 206:
    print("Teacher: \"Why aren't you in the class right now? Are you lost? Let me show you where the room is.\"")
    print("The teacher leads you to the classroom. As you walk in, you are faced with a class full of laughing Juniors and a confused math teacher.")
    print("You: \"I..I think I'm in the wrong class.... Sorry, It's my first day here.")
    print("You sprint out of the classroom and spend the next few minutes finding the assigned class on your schedule.")
    print("You have finally found the classroom. You tell the teacher you got lost, and they say it isn't a problem and direct you to your seat.")
    classmorning()
  if choice == 0:
    print("You: \"I have a free period right now\"")
    print("Teacher: \"Oh, well in that case continue one with whatever you were doing. Just put the food away, please.\"")
    lunch()

def lunch():
  print("It is now lunch period. You follow a new friend to Little Luzzo's to get a $5 special. You bring your pizza to the turf to eat.")
  print("Once you have eaten, your friend invites you to play in a pickup basketball game.")
  choice = input("Enter P to play. R to reject the invite: ")
  if choice == "P":
    basketball()
  if choice == "R":
    print("You have rejected your friend's offer to play basketball. Once Activities period starts, you witness the kids get kicked off the court by some seniors who didn't make the Varsity Team.")
    print("At 11:50, you make your way towards the school building for your afternoon classes.")
    classafternoon()

def basketball():
  print("You have joined the basketball game! As a casual player you contribute to your team by playing good defense, passing the ball, and giving players that make shots high-fives. A player on the other team sets a screen on your teammate, and you switch onto defending middle school basketball team star Sneel Smathur")
  print("Sneel calls an isolation on you, calling you trash. Do you stay on defense or call for help defense?")
  choice = input("Enter O to stay in isolation against Sneel, D to call for help defense: ")
  if choice == "O":
    print("The other members of both teams clear out of the way for the iso. Sneel crosses to the left, then back to the right, then uses a hesitation move. As he drives towards the basket, you move to stay with him, but he unleashes a vicious crossover that has you falling to the ground. He steps back to the three point line and drains one in your face. He proceeds to step over your body while you are on the ground.")
    print("As you try to get up, with everyone in the courtyard getting hype over the crazy move, you notice your ankle isn't aligned with the rest of your leg. You let out a scream.")
    print("Hours later, you wake up in the emergency room of the nearby hospital.")
    print("Obviously, you cannot return to school today. When you return home, you look on Instagram and see that a video of Sneel crossing you up has gone viral on multiple basketball highlight pages. You contemplate leaving the school altogether, but decide it would be best to stick with it. Try again!")
    start()
  if choice == "D":
    print("Sneel: \"Look, the 7 is scared!\"")
    print("Some kids chuckle at what Sneel says, but the game carries on. Congratulations, you managed to avoid being embarrassed on your first day at Hunter. When activities starts, a group of seniors who didn't make the Varsity Basketball team come to kick you off the court. You relax for the rest of your lunch period and head to class at 11:50.")
    classafternoon()

def classafternoon():
  print("You have made your way to afternoon classes. You have a period of gym and then three academic classes.")
  print("When you arrive to gym, you realize that all of your classmates are wearing the grey and black Hunter PE uniform. Your teacher notices you are the odd one out and comes up to you.")
  print("Gym Teacher: \"Why don't you have your uniform?\"")
  print("You explain to the gym teacher that you didn't realize you needed a uniform, and will bring it next class.")
  print("Gym Teacher: \"No worries, kid. Just have it for next class and I'll give you some spare shorts for the period.\"")
  print("You put on the size Adult XL shorts the teacher gives you. A few kids in your class laugh but you end up enjoying the class. The rest of your classes for the day go smoothly, you take good notes and are only cold called on once.")
  print("Congratulations on surviving your first day at Hunter!! Go home, do your homework, and come back tomorrow!")

start()

# Note: The minimum amount of choices one can make is 4, the maximum without restarting is 7