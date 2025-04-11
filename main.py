''' Read in first equation, ax + by = c '''
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

''' Read in second equation, dx + ey = f '''
d = int(input("d = "))
e = int(input("e = "))
f = int(input("f = "))

found = 0

for x in range(-10,11):
    for y in range(-10,11):
        if a*x + b*y == c and d*x + e*y == f:
            print(f'x = {x} , y = {y}')
            found = 1
            break
    if found == 1:
        break

if found == 0:
     print("There is no solution")