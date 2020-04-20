class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        def get_locations(location):
            #left, right, up, down
            directions = [(0,-1), (0,1), (1,0), (-1,0)]
            for direction in directions:
                new_i = location[0] + direction[0]
                new_j = location[1] + direction[1]
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                    yield new_i, new_j
            
        def find_word(location, depth, visited):
            if depth == len(word):
                return True
            
            for new_i,new_j in get_locations(location):
                if board[new_i][new_j] == word[depth] and (new_i,new_j) not in visited:
                    new_visited = visited.copy()
                    new_visited.add((new_i,new_j))
                    if find_word((new_i,new_j), depth+1, new_visited):
                        return True
            return False
            
        if word == "":
            return True
        if not board:
            return False
        
        n_rows = len(board)
        n_cols = len(board[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i,j))
                    if find_word((i,j), 1, visited):
                        return True
        return False