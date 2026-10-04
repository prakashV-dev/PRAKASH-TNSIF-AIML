#Find the missing number

arr = list(map(int, input("Enter a values for list:").split()))

last_value = arr[len(arr)-1]

for i in range(1,last_value+1):
    if i not in arr:
        print("Missing Number:",i)

    
            
    




        


