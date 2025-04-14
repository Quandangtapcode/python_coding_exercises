     
# Check in the string with numeric characters or capitalized characters
def check_string(a):
    has_digit = any(char.isdigit() for char in a)
    has_upper = any(char.isupper() for char in a)
    is_symmetry = a == a[::-1]
    word_count = len(a.split())
    char_count = {}
    for char in a:
        char_count[char] = char_count.get(char, 0) + 1 
    return has_digit, has_upper, is_symmetry, word_count, char_count 

#Enter any a string from the keyboard in size (0,99)
def input_and_check_string():
    while True:
        a = input("Enter a string: ")
        if 0 < len(a) < 100:
            digit_result, upper_result, is_symmetry_result, word_count, char_count = check_string(a)
            print("valid string:", a)
            print("There are numbers : " if digit_result else "not contains numeric characters")
            print("There are capital letters : " if upper_result else "not contains capitalized characters")
            print("Is palindrome string " if is_symmetry_result else "Isn't palindrome string")
            print(f"string a has {word_count}")
            print("Frequency of each character:")
            if char_count:
                for char, count in char_count.item():
                    print(f"Character '{char}' appeared '{count}' times ")
                else:
                    print("No character")    
            return a
        else:
            print("The string must have a character length from 1 to 99. Please enter again.")
        
#Check character in string 
def check_character(a):
    char = input("Enter any character:" )
    if len(char) == 1 :
        if char in a :
            print(f"Character '{char}' in a string")
        else:
            print(f"Character '{char}' not in a string")            
    else:
        print("Please enter only one character")
        
#Enter a b string, check len(b) vs len(a)
def check_substring(a):
    b = input("Enter any b string:")
    if len(b) > len(a):
        print(f"String '{b}' has a greater length than string '{a}'")
    else:
        print(f"String '{b}' hasn't greater length than string '{a}'")
        
    if b in a:
        print("String b is sub-string of the string a")
    else:
        print("String b isn't sub-string of the string a")        
   
   
   
 
               
input_string = input_and_check_string()        
check_character(input_string)
check_substring(input_string) 
    
    



            
        