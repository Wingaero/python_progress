from datetime import datetime
from random import randint
from tkinter import Y

now = datetime.now()

current_time = now.strftime(" %m/%d/%Y, %H:%M:%S")

file = open('outfit_arrays.txt', 'r')

ifsummer = True if (5 > int(now.strftime('%m')) and int(now.strftime('%m')) < 10) else False

isactive = True

while isactive:
    
    with open('outfit_arrays.txt') as file:
        data = file.readline()
        i = 0
        while i < len(data):
            if ifsummer:
                season = 'summer'
            else: season = 'winter' or 'summer'
        file.close()
        
        else: isactive = False

    print("Outfit created for" + current_time)
