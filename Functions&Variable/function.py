'''
k = "awesome"

def myfunc():
    k = "Fantastic"
    print("Python is " + k)

myfunc()

print("Python is " + k)

'''
# Global Variable

x = "awsome"

def func():
    global x 
    x = "fantastic"

func() 
print("Python is " + x)