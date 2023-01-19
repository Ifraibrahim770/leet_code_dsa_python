def is_valid(s):
    # Create an empty stack
    stack = []
    # Create a mapping of close bracket to open bracket
    mapping = {')': '(', '}': '{', ']': '['}
    # Iterate through each character in the string
    for char in s:
        # If the character is a close bracket
        if char in mapping:
            # Get the top element of the stack, or a placeholder value if the stack is empty
            top_element = stack.pop() if stack else '#'
            # If the top element of the stack does not match the open bracket for the close bracket
            if mapping[char] != top_element:
                # Return False, as the string is not valid
                return False
        # If the character is an open bracket
        else:
            # Push it onto the stack
            stack.append(char)
    # Return True if the stack is empty, False otherwise
    return not stack


def is_valid_mine(s):
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in mapping:
            if stack:
                top_element = stack.pop()
            else:
                top_element = "#"
            if top_element != mapping[char]:
                return False
        else:
            stack.append(char)

    return not stack


string = "(()((())))"
print(is_valid_mine(string))
