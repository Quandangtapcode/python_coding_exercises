def is_digit(s):
    try:
        int(s)
        return True
    except:
        return False 
        
values = []    

while True:
    s = input("Enter values(Enter 'done' to exit:): ")
    
    if s.lower() == 'done':
        break
    if is_digit(s):
        values.append(int(s))
    else:
        print("Invalid number, pls try again.")    
        
        
print("\nListed list:", values)


    
    
    
              
        
        
     