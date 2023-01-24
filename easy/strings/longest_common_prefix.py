# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longest_common_prefix(strs) -> str:
    min_length = len(strs[1])
    for string in strs:
        min_length = min(min_length, len(string))

    for i in range(min_length):
        for string in strs:
            if string[i] != strs[0][i]:
                return strs[0][:i]

    return strs[0]


print(longest_common_prefix(["dog", "doger", "dodge"]))


# Sorting method
def longest_common_prefix(strs) -> str:
    strs.sort()
    first_string = strs[0]
    last_string = strs[-1]
    prefix = ""

    for i, char in enumerate(first_string):
        if char != last_string[i]:
            return prefix
        prefix = f'{prefix}{char}'

    return prefix


print(longest_common_prefix(["dog", "doger", "dodge"]))
