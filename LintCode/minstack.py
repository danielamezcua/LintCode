class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.items = []
        self.current_position = -1

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.items+= [number]
        self.current_position+=1

    """
    @return: An integer
    """
    def pop(self):
        if not self.empty():
            item = self.items[self.current_position]
            self.current_position-= 1
            if self.empty():
                self.items = []
            else:
                self.items = self.items[:self.current_position+1]
            return item
        else:
            return None
        
    def empty(self):
        if self.current_position == -1:
            return True
        else:
            return False
            
    """
    @return: An integer
    """
    def min(self):
        # write your code here
        first = True
        for i in self.items:
            if first:
                min = i
                first = False
            elif i < min:
                min = i
        return min