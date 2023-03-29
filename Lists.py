mylist = ["apple", "banana", "cherry"]

print("My List: " + mylist) #print list
print(len(mylist))#print length of list
print(mylist[1])#first item
print(mylist[-1])#first last item (counting backwards)
mylist.append("orange")#adds item to list
print("Updated List: " + mylist)
mylist.insert(1, "pineapple")#inserts item at specific position
mylist.remove("banana")#removes item from list

mytuple = ("kiwi", "orange")
mylist.extend(mytuple)#adds tuple to list
print("Added Tuple to List: " + mylist)#prints updated version