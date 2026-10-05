def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        if (right - left + 1) > max_len:
            max_len = right - left + 1
    return max_len

text = "abcabcbb"
print(length_of_longest_substring(text))
