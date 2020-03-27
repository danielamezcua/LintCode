class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack_input = []
        self.stack_output = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack_input.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if not self.stack_output:
            while self.stack_input:
                self.stack_output.append(self.stack_input.pop())
        return self.stack_output.pop()
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if not self.stack_output:
            while self.stack_input:
                self.stack_output.append(self.stack_input.pop())
        return self.stack_output[-1]