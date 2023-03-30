#you can create modules

#FIRST FILE
#name: calc.py
def add(x, y):
    return (x+y)
 
def subtract(x, y):
    return (x-y)

#second file
import calc
 
print(calc.add(10, 2))

#must be in same folder
