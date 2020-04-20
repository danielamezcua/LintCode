from collections import deque
class Solution:
    """
    @param target: the destination
    @return: the minimum number of steps
    """
    def reachNumber(self, target):
        # Write your code here
        #BFS: time limit exceeded
        # target = 6
        # dq = deque()
        # if target == 0:
        #     return 0
        # n = 1
        # if target == 1 or target == -1:
        #     return 1
        # dq.append((-1,1))
        # dq.append((1,1))
        # while dq:
        #     left = dq.popleft()
        #     right = dq.popleft()
        #     if (left[0] - (left[1] + 1) == target) or (left[0] + (left[1] + 1) == target):
        #         return left[1] + 1
        #     if (right[0] - (right[1] + 1) == target) or (right[0] + (right[1] + 1) == target):
        #         return right[1] + 1
            
        #     dq.append((left[0] - (left[1] + 1), left[1] + 1))
        #     dq.append((left[0] + (left[1] + 1), left[1] + 1))
        #     dq.append((right[0] - (right[1] + 1), right[1] + 1))
        #     dq.append((right[0] + (right[1] + 1), right[1] + 1))
        
        #math approach
        target = abs(target)
        if target == 0:
            return 0
        steps = 1
        sum = 1
        while sum < target:
            steps+=1
            sum+=steps

        difference = target - sum
        if difference % 2 == 0:
            return steps
        else:
            return steps + 1 + (steps%2)
