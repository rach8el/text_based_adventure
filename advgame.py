
import math
def welcome_player():
    playerinput = input("Welcome to Noodlequest. Would you like to begin?\n (y/n) ")
    if playerinput == "y": 
      print()
    elif playerinput == "n": 
     exit()


def scene_one():
   player_name = input("You are getting a call from Lord Farquaad!")
   player_input = input("Do you accept?")
   if player_input == "yes":
      print("You must venture into the Italian Chinese food restaurant to acquire infinite Chinese food. I am starving and my 5 meals a day just won’t do any longer. I will lend you a backpack chockablock with items pivotal to your journey, which are a Grappling Hook, a Flashlight, a Freddy Fazbear Watch, an SOS Reciever, and a bag of Cheezits. If you fail to complete within 48 hours, I will put you in the oven with the gingerbread man. Do you acquiesce?")
   elif player_input == "no":
      print("Answer regardless. \n You must venture into the Italian Chinese food restaurant to acquire infinite Chinese food. I am starving and my 5 meals a day just won’t do any longer. I will lend you a backpack chockablock with items pivotal to your journey, which are a Grappling Hook, a Flashlight, a Freddy Fazbear Watch, an SOS Reciever, and a bag of Cheezits. If you fail to complete within 48 hours, I will put you in the oven with the gingerbread man. Do you acquiesce?")
   play_input = input("Press enter to venture inside.")
   print("Speak to the worker")

def scene_two():
   player_input = input("\n Scene 2: The Restaurant Enterance")
   player_input = input("You get dropped off by Lord Farquaad at the mysterious Italian Chinese restaurant.")
   player_input = input("A worker stands at the enterance as you walk in, looking expectantly at you.")
   player_input = input("Ey, welcome to the Italian Chinese food restaurant. Ya must enter a room to complete a challenge for the infinite Chinese food or whatever. You get a bag of donkey hair.")
   player_input = input("Do you continue?")
   if player_input == "yes":
      print("You enter one of the rooms and find a Chuck e Cheese token to unlock the door in the back.")
   elif player_input == "no":
      print("Go inside regardless. \n You enter one of the rooms and find a Chuck e Cheese token to unlock the door in the back.")
   player_input = input("You have the option to look around or..")
   player_input = input("Eat some Cheez-Its!")
   player_input = input("Do you wish to look around or eat the Cheez Its?")
   if player_input == "Look around":
      print("You look around for a while and end up finding a door in the back of the room.")
   elif player_input == "Eat the Cheez-Its":
      print("GAME OVER")
      exit()


welcome_player()

scene_one()

scene_two()