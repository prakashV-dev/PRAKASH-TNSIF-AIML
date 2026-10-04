# check whether two arrays are equal

arr1 = [1, 2, 2, 3, 4]
arr2 = [4, 2, 3, 2, 1]

if len(arr1) != len(arr2):
    print("Arrays are not equal")
else:
    freq1 = {}
    freq2 = {}

    for num in arr1:
        freq1[num] = freq1.get(num, 0) + 1

    for num in arr2:
        freq2[num] = freq2.get(num, 0) + 1

    if freq1 == freq2:
        print("Arrays contain the same elements with the same frequency")
    else:
        print("Arrays are not equal")
