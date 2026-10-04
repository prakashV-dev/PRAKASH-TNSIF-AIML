# Remove duplicate elements

arr = list(map(int,input("Enter a values for array").split()))

arr1 = []

for val in arr:
    if val not in arr1:
        arr1.append(val)
   
print(arr1)
    
    
