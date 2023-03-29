#String declared
a = "Hello"

#String over multiple Lines
multilinestring = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#new string
findstring = "Everything is code!"
print(findstring[1]) #prints out word or letter or number on that certain position

#loop program for digits in string
for x in "banana":
    print("banana: " + x)

#findout length of a string
print(len(findstring))

#searches for word in string
if "code" in findstring:
    print("Yes, there is code in the variable findstring")


#get certain positions !index starts at 0!
print(findstring[2:5]) #prints characters from position 2 to 5 

print(findstring[:10])#prints all characters until certain position
print(findstring[1:])#prints out string starting from certain position
print(findstring.upper())#prints string in capital letters
print(findstring.lower())#prints string in lower letters
print(findstring.strip())#removes any spaces
print(findstring.split(","))# splits string)

String1 = "string 1"
String2 = "string 2"
String3 = String1 + String2
print(String3)
