class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.min_values = [] #this as well will be a stack
        self.data = []
        self.number_of_elements = 0

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        if self.is_empty() or number <= self.min_values[-1]:
            self.min_values.append(number)

        self.data.append(number)
        self.number_of_elements += 1

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if not self.is_empty():
            element = self.data.pop()
            if element == self.min_values[-1]:
                self.min_values.pop()
            self.number_of_elements -= 1
            return element

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        if not self.is_empty():
            return self.min_values[-1]
    
    def is_empty(self):
        if self.number_of_elements == 0:
            return True
        else:
            return False