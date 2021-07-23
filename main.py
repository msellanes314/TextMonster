## Starter Code
import time

def roomType():
  if room == 'empty':
    print('You are in an empty room.')
  elif room=='sword':
    print('This room has a sword.')
  elif room=='magic stones':
    print('This room has a magic stones.')
  elif room=='monster':
    print('You have confronted a monster. A sword is required to defeat the beast')
  elif room=='boss monster':
    print('You have confronted a BOSS monster. They can only be defeated with a sword AND magic stones.')
  elif room=="stairs down":
    print('You have entered a room with stairs down')
  elif room=="stairs up":
    print('You have entered a room with stairs up')
  elif room=="prize":
    print('You have entered a room with the PRIZE!')
    #gameState = 'won' doesnt work because this is a function
  else:
    print('Where are you?')
    
## Text Monster Game
## The goal of this game is to beat the monsters and claim the prize at the end of the dungeon.

# Map of the dungeon
# Feel free to adapt and design your own level. The whole map must be at least 3 floors and 15 rooms total, though.
floor0 = ['empty', 'sword', 'stairs up', 'monster', 'empty']
floor1 = ['magic stones', 'monster', 'stairs down', 'empty', 'stairs up']
floor2 = ['prize', 'boss monster', 'sword', 'sword', 'stairs down']

# Items in the player's possession
inventory = []

# Player's current position in the dungeon
# The player starts in the first room on floor 0
currentFloor = 0
currentRoom = 0

# Keep track of whether the game is in progress or over (so we know when to stop the game loop)
gameState = 'ongoing'
boss_monster_status="alive"

print("Welcome to Text Monster. \nThe goal of this game is to claim the prize at the end of the dungeon. \nBeware of monsters protecting their gems.")
time.sleep(3)
print("\nOh no! You have lost the map but remembered that every floor has the same number of rooms.")
time.sleep(3)
print("Goodluck! May the odds be ever in your favor. If you're lost, you can always ask for help!")

while gameState == 'ongoing':
  #Describe the room the player is in
  if currentFloor == 0:
    floor = floor0
  elif currentFloor == 1:
    floor = floor1
  else:
    floor = floor2

  room = floor[currentRoom]
  

  # Get command from the player
  choice = input('Command? ')
  # You need to handle describing the other cases..
  last_command=""

  # Respond to command
  if choice == 'help':
    if room=="stairs up":
      if currentRoom==4:
        print("possible commands are up and left")
      elif currentRoom==0:
        print("possible commands are up and right")
      else: 
        print("possible commands are up, left, or right")
    elif room=="stairs down":
      if currentRoom==4:
        print("possible commands are down and left")
      elif currentRoom==0:
        print("possible commands are down and right")
      else: 
        print("possible commands are down, left, or right")
    elif room=="empty":
      if currentRoom==4:
        print("possible command is left (or you'll hit a wall)")
      elif currentRoom==0:
        print("possible command is right(or you'll hit a wall)")
      else:
        print("possible commands are left or right")
    elif (room=="magic stones" or room=="sword"):
      if currentRoom==4:
        print("possible commands are grab or left (or you'll hit a wall)")
      elif currentRoom==0:
        print("possible commands are grab or right(or you'll hit a wall)")
      else:
        print("possible commands are grab, left, or right)")
    elif (room=="monster" or room=="boss monster") and last_command=="left":
      print("possible commands are fight or right")
    elif (room=="monster" or room=="boss monster") and last_command=="right":
      print("possible commands are fight or left")
    else:
      print("You are in another world. *Gasp*")
    
  elif choice == 'left':
    # Player wants to move left
    if currentRoom==0:
      print("Invalid move. There is no room to the left.")
    elif (room=="monster" or room=="boss monster") and last_command=="left":
      print("You must fight to access the room behind the beast!")
    else:
      last_command="left"
      currentRoom=currentRoom-1
      room=floor[currentRoom]
      roomType()


  elif choice == 'right':
    if currentRoom==4:
      print("invalid move. There is no room to the right.")
    elif room=="monster" and last_command=="right":
      print("you must fight monster to access the room behind the beast")

    else:
      last_command="right"
      currentRoom=currentRoom+1
      #currentRoom=currentRoom+1
      room=floor[currentRoom]
    #print(room)
    roomType()

    # Player wants to move right

  elif choice == 'up':
    
    if room!="stairs up":
      print("invalid move. There are no stairs up")
    else: #room =='stairs up'
      last_command="up"
      currentFloor=currentFloor+1

      if currentFloor == 0:
        floor = floor0
      elif currentFloor == 1:
        floor = floor1
      else:
        floor = floor2

      room=floor[currentRoom]
      roomType()
      #room=floor[currentRoom]
      
    # Player wants to go upstairs
    #roomType()

  elif choice == 'down':
    
    if room!="stairs down":
      print("invalid move. There are no stairs down")
    else:
      last_command="down"
      currentFloor=currentFloor-1

      if currentFloor == 0:
        floor = floor0
      elif currentFloor == 1:
        floor = floor1
      else:
        floor = floor2

      room=floor[currentRoom]
      roomType()
    # Player wants to go downstairs

  elif choice == 'grab':
    # Player wants to grab item from the room
    print("Grab was chosen")
    #print("now in:",room)

    if len(inventory)>=3:
      print("You can only hold three items at a time")

    if room =='sword':
      inventory.append('sword')
      print("A sword has been added to your inventory")
      floor[currentRoom]="empty"
      room=floor[currentRoom]

    elif room=='magic stones':
      inventory.append('magic stones')
      print("Magic stones have been added to your inventory")
      floor[currentRoom]="empty"
      room=floor[currentRoom]

    elif room=='prize':
      inventory.append('prize')
      break
    else:
      print("Invalid move. Please try again.")
   
  
  elif choice == 'fight':
    if room=="monster":
      if len(inventory)==0:
        print("You have no swords and died")
        gameState="Lost"
      else:
        if "sword" in inventory:
          last_command="fight"
          print("You have a sword and used it to beat the monster")
          time.sleep(2)
          print("Oh no your sword broke!")
          inventory.remove("sword")
          floor[currentRoom]="empty"
          room=floor[currentRoom]
        else:
          print("You do not have a sword and died trying to battle the monster without a weapon")
          gameState="Lost"


    elif room=="boss monster":
      if ("sword" and "magic stones") in inventory:
        print("You have a sword and magic stones and used it beat the BOSS monster! Congratulations")
        time.sleep(2)
        print("Oh no your sword broke and your stones dissolved!")
        inventory.remove("sword")
        inventory.remove("magic stones")
        boss_monster_status="dead"
        floor[currentRoom]="empty"
        room=floor[currentRoom]
      else:
        print("You do not have The necessary tools to beat the monster and have died trying.")
        gameState="Lost"

    else:
      print("Invalid move. There is nothing to fight")

  else:
    print('Command not recognized. Type "help" to see all commands.')

if boss_monster_status=="dead" and room=="prize":
  gameState="won"
#print(room)

if gameState == 'won':
  time.sleep(3)
  print("Congratulations. You beat the boss monster and claimed the prize!")
  print('You won the game! :)')
else:
  print('You lost the game. :( Maybe next time.')
  gameState="Lost"



