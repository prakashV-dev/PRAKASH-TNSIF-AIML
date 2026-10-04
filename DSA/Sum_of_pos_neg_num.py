# sum of positive and negative numbers

lst = list(map(int, input("Enter a values for list:").split()))

print("array:",lst)

neg_num = 0
pos_num = 0

for val in lst:
    if val < 0:
        neg_num += val
    else:
        pos_num += val

print("Negative_numbers:", neg_num)
print("positive numbers:", pos_num)
