def reverse_string(s):
    reversed_s = ""
    for i in range(len(s)-1,-1,-1):
        reversed_s += s[i]
    return reversed_s    
     


while chuoi != "X" and chuoi != "x":
    chuoi = input("Nhập 1 chuỗi: ")
    print("Chuỗi đảo ngược:", reverse_string(chuoi))