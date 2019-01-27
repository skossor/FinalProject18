import random 

#create a list of choices the player and computer can choose from 
weapons = ['drill', 'laser cutter', 'White Tardis', 'wrench', 'soldering iron', 'computer']
rooms = ['Mrs. Gersteins Room', 'the MakerSpace', 'Sanservinos Room', 'the Auditorium', 'the Main Office', 'Dr. Guptas Room']
suspects = ['Amanda', 'Thomas', 'Raymond', 'Tara', 'Christian', 'Charles']

#the computer generates the winning choices
games = {"win" : (random.choice(weapons), random.choice(rooms), random.choice(suspects))}

#ask the user their name
name = input ("What is your name Detective? ") 
#print the rules of the game
print(f"Hey Detective {name}. Let us explain... \n There has been a murder on campus! You need to find out what happened and bring the killer to justice! \n You need to go through a series of options to eventually discover where the murder took place, what weapon was used, and who did it! After each of your guesses, you will be able to rule out some of the options until you finally find out what exactly happened. You will get small hints from the lab to help you guide your search. \n If you guess the wrong suspect 3 times, the Murderer will hunt you down and find you and you will be forced to fight him, win or lose. Don't let it get to that. \n Good luck solving the murder... we are all counting on you! ") 


#the list of incorrect guesses the user inputs 
guessed_room = []
guessed_weapon = []
guessed_suspect = []

#the number of guesses per category 
number_room = 0
number_weapon = 0
number_suspect = 0

#the list of descriptions for the different rooms
description_room = ['a smaller room with a suspicious looking motorcycle helmet', 'a dangerous room filled with sharp equiment that is sure to bring a slow and painful death', 'a room that seems to have taken a trip to the wild west with what seems to be a shredded pop quiz in the garbage can', 'a larger room filled with rows of chairs and what looks to be a projector that never works', 'a room that has three additional rooms with a swipping machine', 'a chemical-smelling room with a suspicious sketelton figured staring out of a connecting lab']
#describing the winning room depending on the computer's random choice as a hint
description = []
if games["win"][1] == rooms[0]:
  description = description_room[0]
elif games["win"][1] == rooms[1]:
  description = description_room[1]
elif games["win"][1] == rooms[2]:
  description = description_room[2]
elif games["win"][1] == rooms[3]:
  description = description_room[3]
elif games["win"][1] == rooms[4]:
  description = description_room[4]
elif games["win"][1] == rooms[5]:
  description = description_room[5]

#the list of descriptions for the different suspects
description_suspect = ['seemed to have black hair and carrying a waterbottle', 'seemed to be particularly tall with light brown hair', 'seemed to be typing very fast on a computer (perhaps coding or hacking??)', 'seemed to have dark brown hair with a Westfield jakcet', 'seemed to be have dirty blonde hair and always suspiciously smiled at everyone the suspect saw', 'seemed to have headphones in as the witness called out and the suspect did not flinch']
#describing the winning suspect depending on the computer's random choice as a hint
description_s = []
if games["win"][2] == suspects[0]:
  description_s = description_suspect[0]
elif games["win"][2] == suspects[1]:
  description_s = description_suspect[1]
elif games["win"][2] == suspects[2]:
  description_s = description_suspect[2]
elif games["win"][2] == suspects[3]:
  description_s = description_suspect[3]
elif games["win"][2] == suspects[4]:
  description_s = description_suspect[4]
elif games["win"][2] == suspects[5]:
  description_s = description_suspect[5]

#the list of descriptions for the different weapons
description_weapon = ['had several holes within their head', 'had deep burn marks across their torso', 'had large blunt force trama', 'had percise blunt force trama', 'had percise, small and deep burn marks on the neck area', 'had severe blunt force trama by a very large object']
#describing the winning weapon depending on the computer's random choice as a hint
description_w = []
if games["win"][0] == weapons[0]:
  description_w = description_weapon[0]
elif games["win"][0] == weapons[1]:
  description_w = description_weapon[1]
elif games["win"][0] == weapons[2]:
  description_w = description_weapon[2]
elif games["win"][0] == weapons[3]:
  description_w = description_weapon[3]
elif games["win"][0] == weapons[4]:
  description_w = description_weapon[4]
elif games["win"][0] == weapons[5]:
  description_w = description_weapon[5]


#create a loop for the game to continue to run through
game = True 
while game == True:

  while True:
    #ask the user which room they would like to be in
    room_choice = input("""\nWhat room do you think the murder happened in? Your choices are \n 1. Mrs. Gersteins Room \n 2. Makerspace \n 3. Sanservinos Room \n 4. the Auditorium \n 5. the Main Office \n 6. Dr. Guptas Room \n  
 _____________________________________________
|.'',                                     ,''.|
|.'.'',                                 ,''.'.|
|.'.'.'',                             ,''.'.'.|
|.'.'.'.'',                         ,''.'.'.'.|
|.'.'.'.'.|                         |.'.'.'.'.|
|.'.'.'.'.|===;                 ;===|.'.'.'.'.|
|.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
|.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
|,',',',',|---|',|'|???????|'|,'|---|,',',',',|
|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
|.'.'.'.'.|---|','   /%%%\   ','|---|.'.'.'.'.|
|.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|
|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
|.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
|.'.','         /%%%%%%%%%%%%%\         ','.'.|
|.','          /%%%%%%%%%%%%%%%\          ','.|
|;____________/%%%%%%%%%%%%%%%%%\____________;|""")
    #response if the user does not choose the appropriate response 
    if room_choice == '1' or room_choice == '2' or room_choice =='3'or room_choice == '4' or room_choice == '5' or room_choice == '6':
      break
    else:
      print("Please choose one of the chooses above!!")
  #associate the user input with the list item
  room_choice = int(room_choice) -1 
  #response if the user guesses the correct room
  if rooms[room_choice]  == games["win"][1]:
    print(f"\nThe murder happened in {rooms[room_choice]}!")
  #response if the user already guessed the room
  elif rooms[room_choice] in guessed_room:
    print("\nYou already guessed that and it was wrong") 
  #response with a hint if the user guesses incorrectly 
  else:
   print(f"\nThe murder did not happen in {rooms[room_choice]}!You get information back from the labs that has you recalulating your previous thoughts. You find out that the room that the murder happened in had this description: {description}")
   #the number of guesses the user has increases
   number_room += 1
   #adds the incorrect guess to the list of incorrect guesses
   guessed_room.append((rooms[room_choice]))
   print (f"Number of Guesses for Room: {number_room}")
  #ask if the user wants to know the incorrect guesses
  see_room = input("Do you want to see what you have picked incorrectly so far?: y/n")
  #response if the user answers yes or no
  if see_room == 'y':
    print (f" Rooms: {guessed_room} \n Weapons: {guessed_weapon} \n Suspects {guessed_suspect}")
  else:
    print ("Ok good luck!")

   
   
  


  

  while True:
    #ask the user which weapon they think was used
     weapon_choice = input("""\nWhat weapon do you think was used? Your choices are \n 1. Drill \n 2. Laser Cutter \n 3. White Tardis \n 4. Wrench \n 5. Soldering Iron \n 6. Computer \n  
  ,  /\  .  
 //`-||-'\\ 
(| -=||=- |)
 \\,-||-.// 
  `  ||  '  
     ||     
     ||     
     ||     
     ||     
     ||     
     ()
     """)
    #response if the user does not choose the appropriate response      
    if weapon_choice == '1' or weapon_choice == '2' or weapon_choice =='3' or weapon_choice == '4' or weapon_choice == '5' or weapon_choice == '6':
      break
    else:
      print("Error")
  #associate the user input with the list item
  weapon_choice = int(weapon_choice) -1 
  #response if the user guesses the correct weapon
  if weapons[weapon_choice]  == games["win"][0]:
    print(f"\nThe murderer did use the {weapons[weapon_choice]}!") 
  #response if the user already guessed the weapon
  elif weapons[weapon_choice] in guessed_weapon:
    print("You already guessed that and it was wrong")
  #response with a hint if the user guesses incorrectly 
  else:
   print(f"\nThe murderer did not use the {weapons[weapon_choice]}! The lab that anaylzed the body calls you with important imformation that can help you figure out the weapon that was used. The lab says the victim: {description_w}!")
   #the number of guesses the user has increases 
   number_weapon += 1
   print (f"Number of Guesses for Weapon: {number_weapon}")
   #adds the incorrect guess to the list of incorrect guesses
   guessed_weapon.append((weapons[weapon_choice]))
  #ask if the user wants to know the incorrect guesses
  see_weapon= input("do you want to see what you have picked incorrectly so far?: y/n")
  #response if the user answers yes or no
  if see_weapon == 'y':
    print (f" Rooms: {guessed_room} \n Weapons: {guessed_weapon} \n Suspects {guessed_suspect}")
  else:
    print ("Ok good luck!")

 

  
  while True: 
    #ask the user which suspect they think committed the murder
    suspect_choice = input("""\nWho do you think did it? Your choices are \n 1. Amanda \n 2. Thomas \n 3. Raymond \n 4. Tara \n 5. Christian \n 6. Charles \n


 ....,       ,....
.' ,,, '.   .' ,,, '.
 .`   `.     .`   `.
: ..... :   : ..... :
:`~'-'-`:   :`-'-'~`:
 `.~-`.'     `.~`'.'
   ```   ___   ```
       ( . . )

        .._..
      .'     '.   
     `.~~~~~~~.`
       `-...-`
       """)

    #response if the user does not choose the appropriate response   
    if suspect_choice == '1' or suspect_choice == '2' or suspect_choice =='3' or suspect_choice == '4' or suspect_choice == '5' or suspect_choice == '6':
      break
    else:
      print("Error")

  #associate the user input with the list item 
  suspect_choice = int(suspect_choice) -1 
  #response if the user guesses the correct suspect
  if suspects[suspect_choice]  == games["win"][2]:
    print(f"\nGood job! The murderer was {suspects[suspect_choice]}!") 
  #response if the user already guessed the suspect
  elif suspects[suspect_choice] in guessed_suspect:
    print("\nYou already guessed that and it was wrong")
  #response with a hint if the user guesses incorrectly 
  else:
   print(f"\nThe murderer was not {suspects[suspect_choice]}. However, a new witness has stepped forward and saw a glimpse of the murderer. The witness said the murderer: {description_s}")
   #the number of guesses the user has increases 
   number_suspect +=1
   print (f"Number of Guesses for Suspect: {number_suspect}")
    #adds the incorrect guess to the list of incorrect guesses
   guessed_suspect.append((suspects[suspect_choice]))
  #ask if the user wants to know the incorrect guesses
  see_suspect= input("do you want to see what you have picked incorrectly so far?: y/n")
  #response if the user answers yes or no
  if see_suspect == 'y':
    print (f" Rooms: {guessed_room} \n Weapons: {guessed_weapon} \n Suspects {guessed_suspect}")
  else:
    print ("Ok good luck!")



  # if the incorrect number of suspect guesses is equal to 3, this runs
  if number_suspect == 3:
    print ("You have run out of chances. You better be ready to meet your match.")
    # make a class called humans with a name, health, attack skills, and defense skills
    class Human: 
      species = "Human"
      def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

      # give humans the ability to heal and fight, and create conditions for both
      def heal(self):
        self.hp += 5
      def fight(self, opponent): 
        opponent.hp -= self.atk
        print(f"You attack the {opponent.name}.")
        dmg = self.atk - opponent.defense
        

    #create two humans, the detective, which is the player, and the murderer
    Detective = Human("Detective", 50, 20, 10)
    Murderer = Human("Murderer", 60, 5, 20)
    
    #have the humans perform actions
    Detective.fight(Murderer)
    

    Murderer.hp -= Detective.atk

    print(f"Murderer has {Murderer.hp} health points left! Keep going!")

    #give the player the option to attack the murderer again
    attack_again = input("Do you want to hit him again or stop fighting?: y/n")
    # if they say yes, have the murderer and the detective fight and have the detective win and reveal what happened
    # have humans perform actions and change the health accordingly
    if attack_again == 'y':
      Murderer.fight(Detective)
      Detective.atk -= Murderer.atk
      print(f" The murderer attacked you! Your health is now {Detective.hp}. Don't let him get you.")
      Murderer.hp -= Detective.atk
      print(f"Murderer has {Murderer.hp} health points left! Keep going!")
      Murderer.hp -= Detective.atk
      print(f"Murderer has {Murderer.hp} health points left! You got him! Congrats! You apprehended the murderer and got justice")
      print (f"""You solved the case! The murder happened in {games["win"][1]}, the weapon used was {games["win"][0]}, and the murderer was {games["win"][2]}. """)
      game = False

    # if they say no, have the murderer attack the detective (actions for class) and end game with case unsolved
    else:
      Murderer.fight(Detective)
      print(f" The murderer kept attacking you! You are dead! The case will remain unsolved.")
      game = False
     

  else:
    print ("Good luck")


  # if they guess all of the choices correctly before they chose the suspect wrong three times, congratulate them and end the game
  if rooms[room_choice] == games["win"][1] and weapons[weapon_choice] == games["win"][0] and suspects[suspect_choice] == games["win"][2]:
    print (f"""You solved the case! The murder happened in {games["win"][1]}, the weapon used was {games["win"][0]}, and the murderer was {games["win"][2]}. """)
    game = False 

