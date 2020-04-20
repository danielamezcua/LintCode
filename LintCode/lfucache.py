#LintCode problem number 24: LFU Cache
from collections import OrderedDict
class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.max_frequency = 100 #will help to resize array
        self.frequencies_array = [OrderedDict() for i in range(self.max_frequency)] #tells me which numbers have been used 0, 1,2 times...
        self.frequencies_dict = {} #tells me how many times a specific number has been used
        self.keys_available = capacity
        self.cache = {}

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # check if space on cache
        if self.keys_available > 0:
            #if already on the cache, remove it from the frequencies_array
            if key in self.cache:
                position_in_frequencies_array = self.frequencies_dict[key]
                self.frequencies_array[position_in_frequencies_array].pop(key)
                self.keys_available = self.keys_available + 1

        else:
            #look for the least looked key and remove it from cache
            i = 0
            while not self.frequencies_array[i]:
                i = i + 1
            evicted_key = self.frequencies_array[i].popitem(last=False)[0]
            self.cache.pop(evicted_key)

            #remove it as well from the data structure that registers usage
            self.frequencies_dict.pop(evicted_key)

        #update value and set frequency to zero
        self.cache[key] = value
        self.frequencies_array[0][key] = ""
        self.frequencies_dict[key] = 0
        self.keys_available = self.keys_available - 1

        print(self.frequencies_array)
        print(self.frequencies_dict)
        print(self.cache)

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key in self.cache:
            #update frequency usage
            self.frequencies_dict[key] += 1

            if self.frequencies_dict[key] >= self.max_frequency:#resize array
               self.resize_array()

            self.frequencies_array[self.frequencies_dict[key]-1].pop(key)
            self.frequencies_array[self.frequencies_dict[key]][key] = ""
        else:
            return -1
        return self.cache[key] if key in self.cache else -1

    """
    Doubles size of array of frequencies. We do this because we don't know 
    how many times a key will be obtained. Thus we don't know the size of 
    the array of frequencies.
    """
    def resize_array(self):
        new_array = [set() for i in range(self.max_frequency*2)]
        for i in range(self.max_frequency):
            new_array[i] = self.frequencies_array[i]
        self.frequencies_array = new_array
        self.max_frequency *=2