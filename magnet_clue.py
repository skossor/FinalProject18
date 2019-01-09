import random

#create a list of choices the player and computer can choose from
weapons = ['drill', 'laser cutter', 'White Tardis']
rooms = ['Mrs. Gersteins Room', 'MakerSpace', 'Sanservinos Room']
suspects = ['Amanda', 'Thomas', 'Mrs. Gerstein']


games = {"win" : [(weapons[2], rooms[1], suspects[1]) ]}

name = input ("What is your name?")
print(f"Hey {name}. Let's play Magnet Clue. Let us explain....")
#explain rules here
tries = 3
game = True
while game == True:

  room_choice = int(input("What room do you think the murder happened in? Your choices are 1. Mrs. Gersteins Room, 2. Makerspace, 3. Sanservinos Room "))

  if room_choice == 1:
    print("The murder did not happen in Mrs. Gersteins Room.")
    rooms = [0]
  elif room_choice == 2:
    print("The murder happened in the MakerSpace.")
    rooms = [1]
  elif room_choice == 3:
    print("The murder did not happen in Sanservinos Room.")
    rooms = [2]
  else:
    print("That is not an option!")

  weapon_choice = int(input("What weapon do you think was used? Your choices are 1. Drill, 2. Laser Cutter, 3. White Tardis"))

  if weapon_choice == 1:
    print("That weapon was not used")
    weapons = [0]

  elif weapon_choice == 2:
    print ("That weapon was not used")
    weapons = [1]

  elif weapon_choice == 3:
    print("The White Tardis was used to kill the victim.")
    weapons = [2]

  else:
    print("That is not an option!")


  suspect_choice = int(input("Who do you think did it? Your choices are 1. Amanda, 2. Thomas, 3. Mrs. Gerstein."))

  if suspect_choice == 1:
    print("Amanda was not the killer.")
    suspects = [0]

  elif suspect_choice == 2:
    print ("Thomas is the killer.")
    suspects = [1]


  elif suspect_choice == 3:
    print ("Mrs. Gerstein was not the killer.")
    suspects = [2]

  else:
    print("That is not an option!")








