# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.


# 1. Brute Force Solution
def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    print(s)


string = ["h", "e", "l", "l", "o", "o"]


# reverse_string(string)


def reverse_string_mine(s):
    temporary_str = s[:]
    index = 0
    length = len(s)

    for index in range(length):
        s[index] = temporary_str[length - index - 1]
    print(s)


reverse_string_mine(string)


def reverse_array(array):
    left = 0
    right = len(array) - 1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    print(array)


reverse_array([1, 2, 3, 4])
