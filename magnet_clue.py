import random

#create a list of choices the player and computer can choose from
weapons = ['drill', 'laser cutter', 'White Tardis']
rooms = ['Mrs. Gersteins Room', 'the MakerSpace', 'Sanservinos Room']
suspects = ['Amanda', 'Thomas', 'Raymond']


games = {"win" : (random.choice(weapons), random.choice(rooms), random.choice(suspects))}


name = input ("What is your name?")
print(f"Hey {name}. Let's play Magnet Clue. Let us explain....")
#explain rules here

guessed_room = []
guessed_weapon = []
guessed_suspect = []

game = True
while game == True:


  print (games["win"][1])



  while True:
    room_choice = input("What room do you think the murder happened in? Your choices are 1. Mrs. Gersteins Room, 2. Makerspace, 3. Sanservinos Room ")
    if room_choice == '1' or room_choice == '2' or room_choice =='3':
      break
    else:
      print("Error")

  room_choice = int(room_choice) -1
  if rooms[room_choice]  == games["win"][1]:
    print(f"The murder happened in {rooms[room_choice]}!")
  elif rooms[room_choice] in guessed_room:
    print("You already guessed that and it was wrong")
  else:
   print(f"The murder did not happen in {rooms[room_choice]}!")
   guessed_room.append((rooms[room_choice]))
  see_room = input("do you want to see what rooms you have picked incorrectly so far?: y/n")
  if see_room == 'y':
    print (guessed_room)
  else:
    print ("Ok good luck!")






  print (games["win"][0])

  while True:
    weapon_choice = input("What weapon do you think was used? Your choices are 1. Drill, 2. Laser Cutter, 3. White Tardis")
    if weapon_choice == '1' or weapon_choice == '2' or weapon_choice =='3':
      break
    else:
      print("Error")

  weapon_choice = int(weapon_choice) -1
  if weapons[weapon_choice]  == games["win"][0]:
    print(f"The murderer did use the {weapons[weapon_choice]}!")
  elif weapons[weapon_choice] in guessed_weapon:
    print("You already guessed that and it was wrong")
  else:
   print(f"The murderer did not use the {weapons[weapon_choice]}!")
   guessed_weapon.append((weapons[weapon_choice]))
  see_weapon= input("do you want to see what weapons you have picked incorrectly so far?: y/n")
  if see_weapon == 'y':
    print (guessed_weapon)
  else:
    print ("Ok good luck!")

  print (games["win"][2])


  while True:

    suspect_choice = input("Who do you think did it? Your choices are 1. Amanda, 2. Thomas, 3. Raymond.")
    if suspect_choice == '1' or suspect_choice == '2' or suspect_choice =='3' :
      break
    else:
      print("Error")


  suspect_choice = int(suspect_choice) -1
  if suspects[suspect_choice]  == games["win"][2]:
    print(f"Good job! The murderer was {suspects[suspect_choice]}!")
  elif suspects[suspect_choice] in guessed_suspect:
    print("You already guessed that and it was wrong")
  else:
   print(f"The murderer was not {suspects[suspect_choice]}!")
   guessed_suspect.append((suspects[suspect_choice]))
  see_suspect= input("do you want to see what suspects you have picked incorrectly so far?: y/n")
  if see_suspect == 'y':
    print (guessed_suspect)
  else:
    print ("Ok good luck!")

  if rooms[room_choice] == games["win"][1] and weapons[weapon_choice] == games["win"][0] and suspects[suspect_choice] == games["win"][2]:
    print ("Congrats you won!")
    game = False

