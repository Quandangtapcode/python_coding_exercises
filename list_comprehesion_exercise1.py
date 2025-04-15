def is_digit(s):
    try:
        int(s)
        return True
    except:
        return False 
        
values = []        
while True:
    s = input("Enter values(Enter 'done' to exit):")
    if s.lower() == 'done':
        break
    if s != 'done':
        values.append(s)
                
        
val = [int(x) for x in values if is_digit(x)]     

   
        
        
print("\nListed list:", val)