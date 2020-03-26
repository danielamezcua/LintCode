"""
In python, you can use list as stack
stack = [1,2,3,4]
Get top element: stack[-1]  -> 4
Pop element: stack.pop()   -> 4
Push element: stack.append(5)
check the size of stack: len(stack)
"""


class Solution:
    """
    @param: stk: an integer stack
    @return: void
    """
    def stackSorting(self, stk):
        # write your code here
        sorted_stack = []
        while stk:
            el = stk.pop()
            if not sorted_stack:
                sorted_stack.append(el)
            else:
                #check if the element should be deeper on the stack
                if sorted_stack[-1] < el:
                    #unstack elements until we found were it belongs (top_element >= element)
                    removed_elements = 0
                    while sorted_stack and sorted_stack[-1] < el:
                        stk.append(sorted_stack.pop())
                        removed_elements += +1
                    sorted_stack.append(el)
                    while removed_elements > 0:
                        sorted_stack.append(stk.pop())
                        removed_elements-=1
                else:
                    sorted_stack.append(el)
        while sorted_stack:
            stk.append(sorted_stack.pop())
