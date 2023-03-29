#Declaring the variable
x = "awesome"
print ("Python is " + x)
#creating a function
def myfunc():
  #declaring x as a global variable
  #can be used everywhere
  global x
  #declaring another x
  x = "fantastic"

#calling function (using it)
#using this function changes the variable
#see via output, run the program
myfunc()
#using the variable
print("Python is " + x)