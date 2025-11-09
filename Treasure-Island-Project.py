print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go? Type 'left' or 'right'")
choice1 = input().lower()
if choice1 == "left":
    print("You have crossed a path, which leads you to a beautiful lake surrounded by golden glowing trees with beautiful canopies.\n"
          "You quickly notice that there is an island in the middle of the lake.\n"
          "At the middle of the island you spot huge house with shining lights gleaming through the windows.\n"
          "You also see that there is a boat to get to the island, however it is very slow.\n"
          "Type 'wait' to wait for the boat to get across to the island\n"
          "Or type 'swim' to swim across to get to the island quickly.")
    choice2 = input().lower()
    if choice2 == "swim":
        print("You slowly get into the water and start swimming towards the island.\n"
              "Halfway through, a pack of hungry piranhas spot you and attack you viciously.")
        print(" GAME OVER!")
    if choice2 == "wait":
        print("Slowly but surely, the boat takes you safely to the island.\n"
              "You go ahead and step into the house.\n"
              "You see that there are 3 doors. One red, one yellow and one blue.\n"
              "Which colored door will you choose? Type 'red', 'yellow' or 'blue'.")
        choice3 = input().lower()
        if choice3 == "red":
            print("You have stepped into a room with a chimera!\n"
                  "The beast quickly spots you and kills you with its fiery breath.")
            print(" GAME OVER!")
        elif choice3 == "blue":
            print("You have entered into a humid room, almost like a swamp. When you look around, you spot a group of goblins.\n"
                  "They quickly surround you and ask you to hand over all of your money, however you don't have any on you.\n"
                  "The goblins become angry and decide to decapitate you.")
            print(" GAME OVER!")
        elif choice3 == "yellow":
            print("You have entered a room filled with flying fairies.\n"
                  "They are friendly and guide you to a chest filled with gold and jewels.")
            print(" CONGRATULATIONS! YOU WIN!")
        else:
            print("Since you did not choose a door, a magic trap was activated and the floor opens up beneath you, dropping you into a pit of spikes.")
            print(" GAME OVER!")
if choice1 == "right":
    print("You crossed the road and arrived at a dark cave.\n"
          "As you enter the cave, you are greeted by a hungry troll who gobbles you up in one bite.")
    print(" GAME OVER!")
else:
    print(" You have not chosen a path. A magical force has struck you and you are now a statue.")
    print(" GAME OVER!")