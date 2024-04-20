# Create a variable named carname and assign the value Volvo to it.
charname = "Volvo"
print("charname")
# Create a variable named l and assign the value 50 to it.
l = 50
print(l)
# Display the sum of 5 + 10, using two variables: x and y.
x=5
y=10
print(x+y)
# Create a variable called z, assign x + y to it, and display the result.
z=x+y
print(z)
# Insert the correct syntax to assign values to multiple variables in one line:
games = ["RD2" , "HSR" , "CR"]
d,f,g = games
print(d , f , g)
# Insert the correct syntax to assign the same value to all three variables in one code line.
j=k=l="Lemon"
print(j , k , l)
# Insert the correct keyword to make the variable x belong to the global scope.
p = "awsome"
def fun():
    global p
    p = "Fantastic"
fun()
print("Pyhton is" , p)  