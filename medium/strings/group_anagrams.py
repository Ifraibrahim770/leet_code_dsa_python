# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Algorithm
# 1. Loop through the list of strings
# 2. For each string, sort the characters
# 3. For anagrams, the sorted result will be the same
# 4. Store the original strings in a hash map, the key is the sorted string
# 5. Iterate through the hashmap and store the values into the result string.


def group_anagrams(strs):
    anagram_map = {}
    final_result = []
    for str in strs:
        result_list = []
        sorted_string = "".join(sorted(list(str)))
        if sorted_string in anagram_map:
            anagram_map[sorted_string].append(str)
        else:
            result_list.append(str)
            anagram_map[sorted_string] = result_list
        final_result.append(result_list)

    for key, value in anagram_map.items():
        final_result.append(value)
    return final_result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))
