class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # greedy solution
        char_counter = [0 for i in range(26)]
        
        for task in tasks:
            char_counter[ord(task)-65] += 1
        
        char_counter.sort()
        
        max_value = char_counter[25] - 1
        idle_spots = max_value*n
        
        for i in range(24, -1, -1):
            idle_spots -= min(char_counter[i], max_value)
        
        if idle_spots > 0:
            return idle_spots + len(tasks)
        else:
            return len(tasks)