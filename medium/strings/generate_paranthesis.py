# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

# Algorithm

# 1. Perform Backtracking algorithm with the following pre-conditions
# - No right parenthesis should start, so insert right parentheses if left > 0
# - The number of parenthesis should be equal i.e left == right
def generate_parentheses(n):
    def backtracking(s, left, right):
        if len(s) == n * 2:
            result.append(s)
            return
        if left < n:
            backtracking(s + '(', left + 1, right)
        if right < left:
            backtracking(s + ')', left, right + 1)

    result = []
    backtracking("", 0, 0)
    return result


print(generate_parentheses(3))
