def get_user_input():
    collection_list = []
    collection_set = set()
    collection_dict = {}
    
    count = int(input("How many items you want to enter? "))
    index = 1
    
    while count > 0:
        for _ in range(count):
            item = input(f"The {index} item is: ")
            collection_list.append(item)
            collection_set.add(item)
            collection_dict[index] = item
            index += 1
        
        print("\nCurrent Collection:")
        print("List:", collection_list)
        print("Tuple:", tuple(collection_list))
        print("Set:", collection_set)
        print("Dictionary:", collection_dict)
        
        count = int(input("How many more items do you want to enter? (Enter 0 to exit"))
    
    print("The program ends")


get_user_input()