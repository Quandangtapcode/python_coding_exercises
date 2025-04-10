a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

# total of list
total = 0
for x in range(0,10):
    total += a[x]
print("total = ", total)    

# count positive number and total of positive number
count = 0
total_of_positive_number = 0 
for x in range(0,10):
    if a[x] >=0:
        count += 1
        total_of_positive_number += a[x]
        
print("count of positive number in list is: ", count)
print("total of all positive number in list = ", total_of_positive_number)


# calculate the average of list and calculate the average of positive number

print("calculate the average of list =", sum(a)/len(a) )
print("calculate the average of positive number = ",total_of_positive_number/count )


# 