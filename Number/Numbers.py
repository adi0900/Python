#numeric types
"int float Complex"

x = 1
print(type(x))
y = 2.5
print(type(y))
z=1j
print(type(z))

z1 = -3255522
print(type(z1))
z2 = 12E4
print(z2 , type(z2))      # e4 -> indicates 4 Zeros

x2 = 3+5j
print(x2, type(x2))

a = float(x) 
print(a)

b = int(y)
print(b)

c = complex(x)
print(c)

import random
print(random.randrange(1,10))