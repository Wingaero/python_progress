from random import randint
import numpy

number_of_rolls = 4
i = 1
rolls_list = []

while i <= number_of_rolls:
  i += 1
  rolls_list.append(randint(1,4))
  print(numpy.sum(rolls_list))

