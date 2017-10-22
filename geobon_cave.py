#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################################
##
## THE GEO BON CAVE
## by Christian Langer
## 2017
##########################################################


import time

def cover():
 print(""""
 
    ---------------------------------------------------------
    ---------------------------------------------------------

       

▄▄▄█████▓ ██░ ██ ▓█████      ▄████ ▓█████  ▒█████      ▄▄▄▄    ▒█████   ███▄    █     ▄████▄   ▄▄▄    ██▒   █▓▓█████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀     ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒   ▓█████▄ ▒██▒  ██▒ ██ ▀█   █    ▒██▀ ▀█  ▒████▄ ▓██░   █▒▓█   ▀ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██░▄▄▄░▒███   ▒██░  ██▒   ▒██▒ ▄██▒██░  ██▒▓██  ▀█ ██▒   ▒▓█    ▄ ▒██  ▀█▄▓██  █▒░▒███   
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ░▓█  ██▓▒▓█  ▄ ▒██   ██░   ▒██░█▀  ▒██   ██░▓██▒  ▐▌██▒   ▒▓▓▄ ▄██▒░██▄▄▄▄██▒██ █░░▒▓█  ▄ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒▓███▀▒░▒████▒░ ████▓▒░   ░▓█  ▀█▓░ ████▓▒░▒██░   ▓██░   ▒ ▓███▀ ░ ▓█   ▓██▒▒▀█░  ░▒████▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░    ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░    ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▐░  ░░ ▒░ ░
    ░     ▒ ░▒░ ░ ░ ░  ░     ░   ░  ░ ░  ░  ░ ▒ ▒░    ▒░▒   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░     ░  ▒     ▒   ▒▒ ░░ ░░   ░ ░  ░
  ░       ░  ░░ ░   ░      ░ ░   ░    ░   ░ ░ ░ ▒      ░    ░ ░ ░ ░ ▒     ░   ░ ░    ░          ░   ▒     ░░     ░   
          ░  ░  ░   ░  ░         ░    ░  ░    ░ ░      ░          ░ ░           ░    ░ ░            ░  ░   ░     ░  ░
                                                            ░                        ░                    ░          

      
                    The GEO BON cave
                    
    ---------------------------------------------------------
    ---------------------------------------------------------
    
""")

 time.sleep(3)

def introduction():
 print("\n"
       "You are staying in front of the iDiv entrance and want to go to the GEO BON cave.\n"
       "You have the key for the main entrance but not for the cave unfortunately.\n"
       "You enter the iDiv floor...the game starts here.\n")
 time.sleep(0.5)

def map():
 print ("The iDiv floor:")
 print("""
 
         __  __
        |      |
        |Floor |
        |      |
        |      |
        |      | ______
        |      ||      |
        |      || GIS  |
        |         LAB  |
        |      ||      |
        |      ||      |
        |      ||______|
 _______|      |
|The CAVE      |
|_______|      |
        |      |
        |      |
        |      |
        |      |
 _______|      |
| Sec          |
|_______|______|   
        
        
 """)
  

def the_end():
  print("""


███╗   ███╗██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗     ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗     ███████╗████████╗███████╗
████╗ ████║██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██╔════╝╚══██╔══╝██╔════╝
██╔████╔██║██║███████╗███████╗██║██║   ██║██╔██╗ ██║    ██║     ██║   ██║██╔████╔██║██████╔╝██║     █████╗     ██║   █████╗  
██║╚██╔╝██║██║╚════██║╚════██║██║██║   ██║██║╚██╗██║    ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝     ██║   ██╔══╝  
██║ ╚═╝ ██║██║███████║███████║██║╚██████╔╝██║ ╚████║    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ███████╗███████╗   ██║   ███████╗
╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚══════╝
                                                                                                                             

                                                       

  """)


def game_over():
    print("""


  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   



  """)

# 6th loop

def loop6():
 action = input('Do you want to run out or try to deactivate the fire alarm?').lower()
 
 if action == 'deactivate':
  print("\n"
        "Damn, you notice that the fire is coming from the GIS lab.\n"
        "The people who were there before, left already the building.\n"
        "Bad choice to deactivate it...It seems to be no escape out of the building anymore.\n"
        "FUCK!")
  game_over()
  time.sleep(1)
 
 elif action == 'run out':
  print("\n"
        "With all respect to your coolnes, you run out of the building.\n"
        "You meet the other people from the GIS lab at the staircase.\n"
        "From the street, you can see fire coming out of the cave now.\n"
        "You are safe..VERY GOOD!\n")

  the_end()
  time.sleep(1)
 
 else:
  print("\n"
        "The sound gets louder.\n"
        "You need to come to a decision fast. Run out or deactivate?\n")
  time.sleep(2)
  loop6()

# 5th loop

def loop5():
 action = input('Do you want to stay in the room or do you wanna search the rat?').lower()
 
 if action == 'search the rat':
  print("\n"
        "You creep under the table, and grab the rat...suddenly you notice that the sound might be the firealarm.\n"
        "That was the strange sound!\n"
        "You keep cool again.\n")
  time.sleep(0.5)
  loop6()
  
 elif action == 'stay':
  print("\nThe rat looks at you with it´s big eyes and the strange sound gets louder.\n")
  time.sleep(0.5)
  loop5()
 
 else:
  print("\nGood idea, but does not take you further.\n")
  time.sleep(0.5)
  loop5()

# 4th loop

def loop4():
 action = input('Do you want to follow the rat or do you want to do nothing?').lower()
 
 if action == 'do nothing':
  print("\n"
        "Pussy...yo are staying in the room and want to wait for the secretary?\n"
        "Come on, the GEO BON cave was open the whole time, you need no key anymore!\n")
  time.sleep(0.5)
  loop4()
 
 elif action == 'follow the rat':
  print("\n"
        "You are following the rat into the GEO BON cave.\n"
        "Indeed the room was open the whole time.\n"
        "You enter the cave, but now you hear a another strange sound.\n"
        "The rat hides somewhere\n")
  loop5()
 else:
  print("\nHey bro, you can´t do that.\n")
  loop4()

# 3rd loop

def loop3():
 print("\nYou are reaching the end of the floor.\n"
       "The light in the room is still on, but nobody seems to be here.\n"
       "But you hear some weird sounds, what´s that?")
 time.sleep(2)
 
 action = input('What do you want to do? (Check the sounds or wait)?').lower()
 
 if action == 'wait':
  print("\nNot bad idea - but it seems not successfull.\n"
        "Nobody is coming so far...\n")
  time.sleep(0.5)
  loop3()
  
 elif action.lower() == 'check the sounds':
  print("\n"
        "DAMN, THAT WAS A RAT!!!\n"
        "The rat is running out of the room towards the GEO BON cave.\n"
        "You can see how the rat enters the cave. But the door was closed before, right?\n")
  time.sleep(0.5)
  
  loop4()
 
 else:
  print("\nEy boss...you can´t do that.\n")
  loop3()

# 2nd loop

def loop2():
 action = input('Where are you going now? (north, east, south oder west)?').lower()
 
 if action == 'east':
  print("\nYou ask the people in the GIS lab, but they have no key for the GEO BON cave.\n"
        "They give you the hint to ask the secretary who you can find at the end of the floor.")
  loop2()
 
 elif action == 'south':
  loop3()
 
 else:
  print("\nYou can´t go in this direction.\n")
  loop2()


# 1st loop

def loop1():
 action = input('Where do want to go? North, east, south or west? ')
 action = action.lower()

 if action  == 'south':
  print("\nYou are in the middle of the floor.\n"
        "In the east there is the GIS lab.\n"
        "Some people still work there, maybe they have the key for the GEO BON cave?\n"
        "In the south you can see some other rooms.\n")
  loop2()
 
 else:
  print("\nYou can´t go in this direction\n")
  loop1()


def main():
 cover()
 introduction()
 map()

 # start 1st loop to begin
 loop1()


main()
