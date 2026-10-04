# right rotation by k position

arr = list(map(int, input("Enter a values for list:").split()))

k = int(input("Enter a value for rotation:"))

def reverse(left,right):
    while left<right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left+=1
        right-=1

reverse(0,len(arr)-1)
reverse(0,k-1)
reverse(k,len(arr)-1)

print(arr)
   
