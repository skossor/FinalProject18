import random

#create a list of choices the player and computer can choose from
weapons = ['drill', 'laser cutter', 'White Tardis']
rooms = ['Mrs. Gersteins Room', 'the MakerSpace', 'Sanservinos Room']
suspects = ['Amanda', 'Thomas', 'Raymond']


games = {"win" : (random.choice(weapons), random.choice(rooms), random.choice(suspects))}


name = input ("What is your name?")
print(f"Hey {name}. Let's play Magnet Clue. Let us explain....")
#explain rules here

#def checking():
  #if int(room_choice) != 1:
    #print("please only guess one number")
  #elif room_choice not in rooms:
    #print(f"please choose one of the three numbers available!")
  #else:
    #print(f"choose a differnet character")



game = True
while game == True:


  print (games["win"][1])

  room_choice = int(input("What room do you think the murder happened in? Your choices are 1. Mrs. Gersteins Room, 2. Makerspace, 3. Sanservinos Room ")) - 1


  if rooms[room_choice]  == games["win"][1]:
    print(f"The murder happened in {rooms[room_choice]}!")
  elif room_choice != 1:
    print(f"please only choose one number!")
  else:
   print(f"The murder did not happen in {rooms[room_choice]}!")




  print (games["win"][0])
  weapon_choice = int(input("What weapon do you think was used? Your choices are 1. Drill, 2. Laser Cutter, 3. White Tardis")) - 1


  if weapons[weapon_choice]  == games["win"][0]:
    print(f"The murderer did use the {weapons[weapon_choice]}!")
  else:
   print(f"The murderer did not use the {weapons[weapon_choice]}!")

  print (games["win"][2])

  suspect_choice = int(input("Who do you think did it? Your choices are 1. Amanda, 2. Thomas, 3. Raymond.")) - 1

  if suspects[suspect_choice]  == games["win"][2]:
    print(f"Good job! The murderer was {suspects[suspect_choice]}!")
  else:
   print(f"The murderer was not {suspects[suspect_choice]}!")

  if rooms[room_choice] == games["win"][1] and weapons[weapon_choice] == games["win"][0] and suspects[suspect_choice] == games["win"][2]:
    print ("Congrats you won!")
    game = False









