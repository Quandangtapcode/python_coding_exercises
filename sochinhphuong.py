def is_perfect_square(n):
    if n < 0:
        return False
    x = 0
    while x*x <=n:
        if x*x == n:
            return True
        x += 1
    return False

while True:
    n = input("Input a number: ")
    if n == "0":
        break
    if not n.isdigit():
        print("Invalid input. Please enter a number.")
        continue
    n = int(n)
    if is_perfect_square(n):
        print(f"{n} is ferfect square")
    else:
        print(f"{n} is not perfect square")        
  
     



