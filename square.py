def square (n):
   perimeter = 4 * n
   acreage = n * n
   return perimeter, acreage

n = float(input("Enter side of square (Enter 0 if you want to exit): "))

while n != 0:
    perimeter, acreage = square(n)
    print(f"Perimeter of square: {perimeter}")
    print(f"Acreage of square: {acreage}")
    n = float(input("Enter side of square (Enter 0 if you want to exit): "))
    
print("Program has exited.")    