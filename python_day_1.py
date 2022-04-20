fruits = ["apple", "banana", "cherry"]
more_fruits = []
x = 0
z = x + 1
while True:
    for i in range(len(fruits)):
      if x % 2 == 0:
        x += 1
        print(fruits[i].lower())
      else:
        x += 1
        print(fruits[i].upper())
    
      if i == len(fruits) - 1:
        i = 0