# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.


def strStr(haystack: str, needle: str) -> int:
    # If the needle string is empty, it is always found in the haystack at index 0
    if not needle:
        return 0
    # Get the lengths of the haystack and needle strings
    n, m = len(haystack), len(needle)
    # Iterate through all possible substrings of length m in the haystack
    for i in range(n - m + 1):
        # Extract the substring of length m starting at index i
        sub = haystack[i:i + m]
        # If the substring matches the needle string, return its starting index
        if sub == needle:
            return i
    # If no match was found, return -1
    return -1





