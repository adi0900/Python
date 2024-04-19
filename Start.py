"""
This is a comment
written in
more than just one line
""" # """ Multiple line Comment
print("This is Comment")

if 1>2:
    print("This Statement is True")

else:
    print("This Statement is False")
    
    x = 5
    y = 10
    c = x+y
    print(c)

    x = 4         # int type
    x = "Sally"   # updated to a type of string
    print(x) 

    x = str(3)   # will be '3'
    y = int(3)   # will be 3 
    z = float(3) # will be 3.0

    x = 5 
    y = "John"
    print(type(x))
    print(type(y))

    x = "John"
    y = 'John'
    print(type(x))
    print(type(y))

name = "John"
message = f"Hello, {name}!"
print(name)
print(message)

import datetime
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

_mynam = "John"
print(_mynam)

# Variable

myVariable = "KICK"
print(myVariable)

x, y, z = "Orange" , "Mango" , "Cherry"
print(x,y,z)

x =y= z= "Orange"
print(x,y,z)

fruits = ["apple" , "banana" , "cherry"]
x , y, z = fruits
print(x,y,z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x+y+z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

l = "Awesome"

def myfunc():
    
    print("Python is " + l)

myfunc()
