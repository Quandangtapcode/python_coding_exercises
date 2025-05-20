def capitalize_words(s):
    words = s.split()  
    capitalize_words = []
    
    for word in words:
        capitalize_word = word[0].upper() + word[1:]   
        capitalize_words.append(capitalize_word)       
        
    result = " ".join(capitalize_words)                

while True:
    chuoi = input("Please enter text:")
    if chuoi == "exit":
        break
    if chuoi.isdigit():
        print("Please enter text: ")
        continue
    
    print("Capitalized text:", capitalize_words(chuoi))