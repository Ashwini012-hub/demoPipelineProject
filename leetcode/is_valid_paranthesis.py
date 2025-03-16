def is_valid_parentheses(s):
    # Initialize a stack to keep track of opening parentheses
    stack = []

    # Dictionary to hold mappings of opening and closing parentheses
    mapping = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the string
    for char in s:
        # If the character is one of the closing brackets
        if char in mapping:
            # Pop the topmost element from the stack if it is non-empty
            # Otherwise, assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'

            # The mapping for the current closing bracket doesn't match the element on the top of the stack
            if mapping[char] != top_element:
                return False
        else:
            # If it was an opening bracket, push to the stack
            stack.append(char)

    # If the stack is empty, then we have a valid expression
    return not stack


# Examples to test the function
print(is_valid_parentheses("()"))  # Output: True
# print(is_valid_parentheses("()[]{}"))  # Output: True
# print(is_valid_parentheses("(]"))  # Output: False
# print(is_valid_parentheses("([)]"))  # Output: False
# print(is_valid_parentheses("{[]}"))  # Output: True