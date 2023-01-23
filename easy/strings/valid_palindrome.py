# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
# all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

import re


def is_palindrome(s):
    pattern = re.compile(r'[^a-zA-Z0-9\s]')
    cleaned_string = pattern.sub('', s).replace(" ", "")  # remain with only characters
    left = 0  # left pointer
    right = len(cleaned_string) - 1  # right pointer
    while left < right:  # loop through the string reversing the elements
        if cleaned_string[left].casefold() != cleaned_string[right].casefold():
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("A man, a plan, a canal: Panama"))
