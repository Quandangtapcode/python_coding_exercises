def reverse_string(s):
    return s == s[::-1]

def main():
    while True:
        a = input("Enter a string (Enter 0 to exit): ").strip()
        if a == "0":
            print("The program ends")
            break
          
        if len(a) <= 0 or len(a) >= 50:
            print("Invalid string length. Please enter again.")
            continue 

        if reverse_string(a):
            print("Symmetry string.")
        else:
            print("Asymmetric chain.")

if __name__ == "__main__":
    main()
