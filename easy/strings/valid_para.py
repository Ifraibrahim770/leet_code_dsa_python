#

# Amount of Insertions it would take to make a string input of brackets valid
def valid_para(s):
    stack = []
    count = 0

    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                count = + 1
            else:
                stack.pop()

    return count + len(stack)


print(valid_para('(()))'))# should print one
