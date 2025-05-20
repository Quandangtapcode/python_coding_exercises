# Viết 1 hàm có tham số là chuỗi, trả về tổng tất cả các số trong chuỗi đấy
n = input("Please enter a text: ")

def summary(n):
    total = 0
    for i in n:
        if i.isdigit():
            total += int(i)
    return total        

y = summary(n)    
print("Sum of number:", y)    
       
    