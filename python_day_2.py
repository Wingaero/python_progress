from random import randint
is_active = True
import numpy as np
 
while is_active:

    # number_of_rolls = input("How many dice are you rolling?")
    # size_of_dice = input("What size are the dice being used?")
    weapon = input("What weapon are you using? ")
    # print("Using " + number_of_rolls + " " + size_of_dice + "-sided dice.")

    # number_of_rolls = int(number_of_rolls)
    # size_of_dice = int(size_of_dice)
    # number_of_dice = int(number_of_dice)
    weapon_list = ["mace", 1, 5, "hand-crossbow", 1, 4, "longsword", 1, 6]
    weapon_exist = weapon in weapon_list
    weapon_dice = weapon_list[1] in weapon_list
    weapon_dice_num = weapon_list[2] in weapon_list
    print (weapon_dice)
    i = 1
    rolls_list = []

    # while i <= number_of_rolls:
    #      i += 1
    #      rolls_list.append(randint(1, size_of_dice))
    #      print(sum(rolls_list))

    # is_restart = input('Would you like to roll more dice? (y/n): ')
    # if is_restart == 'n':
    #     is_active = False

    