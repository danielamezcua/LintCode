class Solution:
    """
    @param arr: the arr
    @return:  the number of train carriages in this transfer station with the largest number of train carriages
    """
    def trainCompartmentProblem(self, arr):
        # Write your code here.
        n = len(arr)
        stack = []
        size_stack = 0
        max_size_stack = 0
        i = 1
        for carriage in arr:
            if i == carriage:
                i+=1
            elif i < carriage:
                while i < carriage:
                    stack.append(i)
                    i+=1
                    size_stack += 1
                if size_stack > max_size_stack:
                    max_size_stack = size_stack
                i+=1
            elif carriage == stack[-1]:
                stack.pop()
                size_stack -= 1
            else:
                return -1
        return max_size_stack