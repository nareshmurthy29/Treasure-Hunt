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
print("Your mission is to find the treasure.\n")

print("Let's play and find the Treasure!\n")

# Starting from the main road
start = input("Want to go left or right from the main road? ").upper()
if start == "LEFT":
    print('Woww! You have reached a river\n')

    # Swim or wait for the boat - River
    while True:
        river = input("Do you want to swim or wait for the boat? Choose S for Swim and W to wait for the boat.\n").upper()
        if river == "W":
            print('Ohh! The boat was cursed. You are dead.\nGame Over!')
            exit()
        elif river == "S":
            print('Congrats! You  reached an Island.\n')
            break
        else:
            print('Wrong input, please enter either "S" or "W".')

    # Now choose weather in the cave
    weather = input("What weather would you choose for a cave?\nH for Hot\nD for Damp\nW for windy\n").upper()
    if weather == "H":
        print('Ohh no! You melted')
        exit()
    elif weather == "D":
        print('Congrats! You reached the end the end of the treasure hunt. Now choose 1 treasure box out of 3\n')
    else:
        print('Shit, You blew away to main road')
        exit()

    #Choose 1 out of 3 treasures.
    treasure = int(input("Choose your treasure box out of 3:\n1. Coated with Diamonds\n2. Coated with platinum\n3. Coated with mud\nChoose 1,2 or 3 \n"))
    if treasure == 1:
        print("Congrats!! You found the treasure")
    elif treasure == 2:
        print("Oh! You found trash")
    else:
        print('Nooooo, there are snakes in this treasure.\nYou are dead')

else:
    print("Oh no! There's a pot hole\nGame Over!")




