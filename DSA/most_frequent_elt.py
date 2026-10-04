#find the Most frequent element

arr = list(map(int,input("Enter a values:").split()))

print(arr)

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

most_freq_num = 0

highest = 0

for num in frequency:
    if frequency[num] > highest:
        most_freq_num = num
        highest = frequency[num]

print("frequency_of_the_num:", highest)
print("most_frequent_num:", most_freq_num)
    






