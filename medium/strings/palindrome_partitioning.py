# Given a string s, partition s such that every
# substring
#  of the partition is a
# palindrome
# . Return all possible palindrome partitioning of s.
#
#
#
# Example 1:
#
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
#
# Input: s = "a"
# Output: [["a"]]


def partition(s):
    # If the input string is empty, return a list with an empty list as its only element
    if not s:
        return [[]]

    # Initialize an empty list to store the partitions
    res = []

    # For each possible prefix of the input string
    for i in range(1, len(s) + 1):
        prefix = s[:i]
        # If the prefix is a palindrome
        if prefix == prefix[::-1]:
            # Recursively partition the suffix of the input string
            suffixes = partition(s[i:])
            # For each partition of the suffix, add the current prefix to the beginning
            for suffix in suffixes:
                res.append([prefix] + suffix)

    # Return the list of partitions
    return res


print(partition("aab"))
