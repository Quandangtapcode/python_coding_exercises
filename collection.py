def get_user_input():
    collection_list = []
    collection_set = set()
    collection_dict = {}
    
    count = int(input("Bạn muốn nhập bao nhiêu mục? "))
    index = 1
    
    while count > 0:
        for _ in range(count):
            item = input(f"Mục thứ {index} là: ")
            collection_list.append(item)
            collection_set.add(item)
            collection_dict[index] = item
            index += 1
        
        print("\nBộ sưu tập hiện tại:")
        print("List:", collection_list)
        print("Tuple:", tuple(collection_list))
        print("Set:", collection_set)
        print("Dictionary:", collection_dict)
        
        count = int(input("Bạn muốn nhập thêm bao nhiêu mục? (Nhập 0 để dừng): "))
    
    print("Chương trình kết thúc!")


get_user_input()