#LintCode problem number 24: LFU Cache

class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.heap = Heap(capacity)

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        self.heap.set(key,value)

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        return self.heap.get(key)
        
"""NOTE: this heap is specific for this problem. It lacks of a function to resizze the heap when
it is full. the elements of the heap are pairs of numbers of the form (key, frequency)"""
class Heap:

    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.heap = [(0,0) for i in range(capacity)]
        self.keys_indexes = {}
        self.cache = {}

    def has_left_child(self,index):
        return True if index*2+1 < self.size else False

    def has_right_child(self,index):
        return True if index*2+2 < self.size else False

    def has_parent(self,index):
        return True if (index-1)//2 >= 0 else False

    def left_child(self,index):
        return self.heap[index*2+1]

    def right_child(self,index):
        return self.heap[index*2+2]

    def parent(self,index):
        return self.heap[(index-1)//2]

    def swap(self, index1,index2):
        #update indexes
        self.keys_indexes[self.heap[index1][0]] = index2
        self.keys_indexes[self.heap[index2][0]] = index1

        aux = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = aux

    def heapify_down(self,index=0):
        while self.has_left_child(index):
            smallest_child_index = index*2+1
            if self.has_right_child(index) and self.right_child(index)[1] < self.left_child(index)[1]:
                smallest_child_index = index*2+2
            if self.heap[index][1] < self.heap[smallest_child_index][1]:
                break
            else:
                self.swap(index,smallest_child_index)
            index = smallest_child_index

    def heapify_up(self,index=0):
        index = self.size-1
        while self.has_parent(index) and self.parent(index)[1] > self.heap[index][1]:
            self.swap(index,(index-1)//2)
            index = (index-1)//2

    def insert(self,element,value):
        key = element[0]
        if key in self.keys_indexes:
            index_repeated_value = self.keys_indexes[key]
            self.heap[index_repeated_value][1] = 0
            self.cache[key] = value
            self.heapify_up(index_repeated_value)
            
        elif self.size < self.capacity:
            self.heap[self.size] = element
            self.keys_indexes[element[0]] = self.size
            self.cache[element[0]] = value
            self.size = self.size + 1
            self.heapify_up()

    def peek(self):
        if self.size > 0:
            return self.heap[0]
        else:
            return None

    def pop(self):
        if self.size > 0:
            item = self.heap[0]
            self.swap(0, self.size-1)
            self.size = self.size - 1
            self.heapify_down()
            return item
        else:
            return None

    def is_full(self):
        return True if self.capacity == self.size else False

    def set(self,key,value):
        if self.is_full():
            #replace first value of the heap
            peeked = self.peek()
            self.heap[0] = (key,0)
            self.keys_indexes.pop(peeked[0])
            self.keys_indexes[key] = 0
            self.cache[key] = value
            print(self.heap)
        else:
            self.insert((key,0),value)
            print(self.heap)

    def get(self,key):
        if key in self.keys_indexes:
            index_in_heap = self.keys_indexes[key]
            element = (key, self.heap[index_in_heap][1] + 1)
            self.heap[index_in_heap] = element #update frequency value
            self.heapify_down(index_in_heap)
            print(self.heap)
            return self.cache[key]
        else:
            print(self.heap)
            return -1

