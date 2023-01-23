# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.

# Example
# Input: s = "leetcode"
# Output: 0

def first_unique_char(s):
    for i, char in enumerate(s):
        count = s.count(char)
        if count == 1:
            return i
    return -1


s = "aabb"
print(first_unique_char(s))