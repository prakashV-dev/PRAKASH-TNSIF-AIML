#write a program to reverse an array

lst = list(map(int, input("Enter a values for array:").split()))

print("Original_array:", lst)

print("reversed_array: ",lst[::-1])

#Using Two pointers:

arr = list(map(int, input("Enter a values for array:").split()))

left = 0
right = len(arr)-1

for i in range(left,right):
    if left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

print(arr)
        
