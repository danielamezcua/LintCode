class Solution:
    """
    @param maze: the maze 
    @return: Can they reunion?
    """
    """[".S**."
        "...*.",
        ".*...",
        ".*.T.",
        "..*.*"]
    """
    def findHer(self, maze):
        # write your code here
        def get_neighbours(position):
            #up, down, left, right
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for direction in directions:
                ni = position[0] + direction[0]
                nj = position[1] + direction[1]
                if (0 <= ni < len(maze)) and (0 <= nj < len(maze[0])):
                    yield ni,nj
        bfs = []
        visited = set()
        found = False
        # find either T or S
        for i in range(len(maze)):
            if found:
                break
            for j in range(len(maze[0])):
                if maze[i][j] == 'T' or maze[i][j] == 'S':
                    bfs.append((i,j))
                    visited.add((i,j))
                    found = True
                    break
        
        # do BFS from all zeros
        while bfs:
            #get the neighbours of this position
            position = bfs.pop()
            for ni,nj in get_neighbours(position):
                if (ni,nj) not in visited:
                    if maze[ni][nj] == 'T' or maze[ni][nj] == 'S':
                        return True
                    if maze[ni][nj] == '.':
                        bfs.append((ni,nj))
                    visited.add((ni,nj))
        return False