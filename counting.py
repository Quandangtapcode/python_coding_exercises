def is_integer(s):
    try:
        int(s)
        return True 
    except:
        return False 


def is_float(s):
    try:
        float(s)
        return not is_integer(s) 
    except:
        return False             
    
values = []

print("Enter values(Enter 'done' to exit):")             


while True:
    a = input("Enter values: ")
    if a.lower() == 'done':
        break
    elif is_integer(a):
        values.append(int(a))
    elif is_float(a):
        values.append(float(a)) 
    else:
        values.append(a)
        
        
type_count = {
    "int": 0,
    "float": 0,
    "str": 0
}           

for item in values:
    if isinstance(item, int):
        type_count["int"] += 1
    elif isinstance(item, float):
        type_count["float"] += 1
    elif isinstance(item, str):
        type_count["str"] += 1
        
print("\nListed list:", values)
print("Counting results by data type:", type_count)                       