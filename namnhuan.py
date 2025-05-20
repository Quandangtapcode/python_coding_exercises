def namnhuan(num):
    if (num % 4 == 0 and num % 100 != 0) or ( num % 400 == 0):
        print(f"{num} là năm nhuận")
    else:
        print(f"{num} không phải là năm nhuận")    

while True:
    num = input("Input a year:")  
    if not num.isdigit():
       print("Vui lòng nhập số nguyên dương:")
       continue
    num = int(num)
    if num == 0:
       break     
    
    namnhuan(num)