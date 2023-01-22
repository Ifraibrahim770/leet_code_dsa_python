# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

def is_anagram(s, t):
    if len(t) != len(s):
        return False
    s_count = {}
    t_count = {}
    # First start at the S string and iterate through it getting
    # counts of characters and storing them in dictionaries

    for char in s:
        if char in s_count:
            s_count[char] += 1
        else:
            s_count[char] = 1

    # Second, start at the T string and iterate through it getting
    # counts of characters and storing them in dictionaries
    for char in t:
        if char in t_count:
            t_count[char] += 1
        else:
            t_count[char] = 1

    return t_count == s_count


s = "rat"
t = "tar"
print(is_anagram(s, t))
