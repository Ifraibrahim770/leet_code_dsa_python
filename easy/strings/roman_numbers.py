# Given a roman numeral, convert it to an integer.

# Example one
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example two
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.


def roman_to_int(s: str) -> int:
    mappings = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(s) - 1):
        if mappings[s[i]] < mappings[s[i + 1]]:
            ans = ans - mappings[s[i]]
        else:
            ans = ans + mappings[s[i]]

    ans = ans + mappings[s[len(s) - 1]]

    return ans


print(roman_to_int('LVIII'))
