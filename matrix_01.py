from collections import deque
class Solution:
    """
    @param matrix: a 0-1 matrix
    @return: return a matrix
    """
    def updateMatrix(self, matrix):
        # write your code here
        def get_neighbours(position):
            #up, down, left, right
            directions = [(-1,0),(1,0),(-1,0),(1,0)]
            for direction in directions:
                ni = position[0] + direction[0]
                nj = postition[1] + direction[1]
                if (0 <= ni <= len(matrix)) and (0 <= nj <= len(matrix[0])) and matrix[ni][nj] != 0:
                    yield ni,nj
        queue = deque()
        visited = set()
        # get positions of all zeros
        for i in range(matrix):
            for j in range(matrix[i]):
                if matrix[i][j] == 0:
                    #enqueue the position and the distance to the nearest 0
                    queue.append((i,j, 0))
                else:
                    matrix[i][j] = float('inf')
        # do BFS from all zeros
        while queue:
            #get the neighbours of this position
            position = queue.popleft()
            for ni,nj in get_neighbours(position):
                #from the nature of BFS, we know that when the cell is visited,
                #it's caller is the closest possible path to a 0.
                if (ni,nj) not in visited:
                    matrix[i][j] = position[2] + 1
                    queue.append((ni,nj, position[2] + 1))
                    visited.add((ni,nj))
        return matrix