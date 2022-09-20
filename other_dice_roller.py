import random

is_active = True
while is_active:
    num_of_rolls = int(input('How many dice are you rolling?: '))
    num_of_sides = int(input('How many sides are on your dice?: '))
    dice_rolls = [random.choice(range(1, num_of_sides+1)) for rolls in range(num_of_rolls)]
    print(dice_rolls, 'You rolled', sum(rolls for rolls in dice_rolls))

    is_restart = input('Would you like to roll more dice? (y/n): ')
    if is_restart == 'n': is_active = False #notmycode