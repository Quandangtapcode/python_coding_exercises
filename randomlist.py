import random


N = int(input("Enter the number of elements N: "))

a = [random.randint(0, 99) for _ in range(N)]
print("Initial list:", a)

a.sort()
print("list after sorting:", a)

a = list(dict.fromkeys(a))
print("List after removing duplicates:", a)