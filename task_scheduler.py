from collections import deque
class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        queue = deque()
        queue_aux = deque()
        
        for task in tasks:
            queue.append(task)
            
        n_intervals = 0
        while queue:
            task = queue.popleft()
            #check if there are still tasks to do
            if queue:
                #check if the adjacent task is the same task
                if queue[0] == task:
                    i = n
                    last_task = task
                    while i > 0:
                        if not queue:
                            n_intervals+= 1 + i
                            i = 0
                        elif queue[0] != last_task:
                            last_task = queue.popleft()
                            n_intervals+=1
                            i-= 1
                        else:
                            queue_aux.append(queue.popleft())
                    
                    queue = queue.extend(queue_aux)
                    queue_aux = deque()
                else:
                    n_intervals += 1
            else:
                #there are no more elements
                n_intervals+=1
        return n_intervals