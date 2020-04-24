class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        def yield_solution(queens):
            r = []
            for queen in queens:
                line = []
                for i in range(n):
                    if i == queen[1]:
                        line.append('Q')
                    else:
                        line.append('.')
                r.append(''.join(line))
            result.append(r)
            print(r)
        
        def can_put_queen(queens,i,j):
            for queen in queens:
                #check row
                if queen[0] == i:
                    return False
                #check column
                if queen[1] == j:
                    return False
                
                #check diagonal
                if abs(queen[0] - i) == abs(queen[1] - j):
                    return False
            return True
            
        def solve_n_queens_rec(queens,i):
            for j in range(n):
                #check if we can place a quene here given the position of the
                #other queens
                if can_put_queen(queens,i,j):
                    if i == n-1:
                        queens.append((i,j))
                        yield_solution(queens)
                        queens.pop()
                    else:
                        queens.append((i,j))
                        solve_n_queens_rec(queens, i+1)
                        queens.pop()
        if n == 0:
            return [[]]
        if n == 1:
            return [["Q"]]
        
        result = []
        solve_n_queens_rec([],0)
        return result