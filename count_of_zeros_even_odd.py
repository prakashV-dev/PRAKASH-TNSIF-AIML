# count the number of zeros, odd, even

lst = list(map(int, input("Enter a values for array:").split()))

print("array:", lst)

count_zero = 0
count_even = 0
count_odd = 0
 
for i in lst:
    if i==0:
        count_zero += 1
    elif i%2==0:
        count_even += 1
    else:
        count_odd += 1

print("count_of_zero:", count_zero)
print("count_of_even:", count_even)
print("count_of_odd:", count_odd)
        
