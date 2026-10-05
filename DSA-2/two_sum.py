def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        seen[nums[i]] = i
    return []

numbers = [2, 7, 11, 15]
target_val = 9
print(two_sum(numbers, target_val))
