def reverse_string(s):
    reversed_s = ""
    for i in range(len(s)-1,-1,-1):
        reversed_s += s[i]
    return reversed_s    
     


while chuoi != "X" and chuoi != "x":
    chuoi = input("Enter a string: ")
    print("Reversed string:", reverse_string(chuoi))