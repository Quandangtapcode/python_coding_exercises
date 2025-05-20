num1 = int(input("Enter first number: "))
num2 = int(input("Enter second numner: "))
num3 = int(input("Enter third number: "))
# Xác định số lớn nhất
if num1 >= num2 and num1 >= num3:
    largest_number = num1
elif num2 >= num1 and num2 >= num3:
    largest_number = num2
else:
    largest_number = num3

print("Largest number is:", largest_number)