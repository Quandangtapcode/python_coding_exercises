# Viết chương trình tính tổng các số từ 1 đến 100

sum = 0
n = int(input("Please enter a number: "))
while n < 0:
    n = int(input("Please enter a number: "))
for i in range(1,n+1):
   sum += i
    
print("Sum = ", sum)


