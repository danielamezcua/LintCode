class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        
        stack_paren = []
        
        for char in s:
            if char == '{' or char == '[' or char == '(':
                stack_paren.append(char)
            elif char == '}':
                if stack_paren and stack_paren[-1] == '{':
                    stack_paren.pop()
                else:
                    return False
            elif char == ']':
                if stack_paren and stack_paren[-1] == '[':
                    stack_paren.pop()
                else:
                    return False
            elif char == ')':
                if stack_paren and stack_paren[-1] == '(':
                    stack_paren.pop()
                else:
                    return False
        if stack_paren:
            return False
        return True
