# Given a string columnTitle that represents the column title as appears in an Excel sheet,
# return its corresponding column number.

# Example

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
def title_to_number(columnTitle):
    column_number = 0
    ans = 0
    for i, c in enumerate(columnTitle[::-1]):
        column_number += (ord(c) - ord('A') + 1) * (26 ** i)

    return column_number


title_to_number('ABA')
