def tong_so_le(n):
    sum = 0 
    while n > 0:
        i = n % 10       # lấy chữ số cuối cùng
        if i % 2 != 0:   # kiểm tra xem số lẻ
            sum += i
        n //= 10         # bỏ chữ số cuối cùng
    return sum
        
y = tong_so_le(1235)
print(y)