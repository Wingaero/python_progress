from random import randint

number_of_loops = 0

start = input("Would you like to start? (y/n)")

while start == "y":

  number_of_rolls = input("How many dice are you rolling?")
  size_of_dice = input("What size are the dice being used?")
  print( "Using " + number_of_rolls + " " + size_of_dice + "-sided dice.")
  number_of_loops += 1

  number_of_rolls = int(number_of_rolls)
  size_of_dice = int(size_of_dice)
  i = 1
  rolls_list = []

  while i <= number_of_rolls:
    i += 1
    rolls_list.append(randint(1,size_of_dice))
    print(sum(rolls_list))

  cont = input("Would you like to continue? (y/n)")

  if cont == "n":
    start = "n"
  else: start = "y"

else: print("Rolling halted.")