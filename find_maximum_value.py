import random

s = [random.randint(0,100) for x in range(20)]

print(s)

a = s.pop()

while s != []:
    b = s.pop()
    if b > a:
        a = b

    
print("The maximum value of the list is: ", a)        