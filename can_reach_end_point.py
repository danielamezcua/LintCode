from collections import deque
class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint(self, map):
        # Write your code here
        def get_move_points(point):
            #up,down,left,right
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            
            for direction in directions:
                if 0 <= (direction[0] + point[0]) < n  and 0 <= (direction[1] + point[1]) < m:
                    yield(direction[0] + point[0], direction[1] + point[1])
                    
        #rows
        n = len(map)
        #columns
        m = len(map[0])
        if map[0][0] == 9:
            return True
        dq = deque()
        dq.append((0,0))
        visited = set()
        visited.add((0,0)) 
        
        while dq:
            point = dq.popleft()
            for new_point in get_move_points(point):
                if new_point not in visited:
                    if map[new_point[0]][new_point[1]] == 9:
                        return True
                    elif map[new_point[0]][new_point[1]] == 1:
                        dq.append(new_point)
                    visited.add(new_point)
        return False
                        
            
            