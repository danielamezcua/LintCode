class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        def check_diagonal(start_i, start_j):
            element = matrix[start_i][start_j]
            i = start_i + 1
            j = start_j + 1
            while i<n_rows and j<n_cols:
                if matrix[i][j] != element:
                    return False
                i+=1
                j+=1
            return True
            
        # Write your code here
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        for i in range(n_rows):
            if not check_diagonal(i,0):
                return False
        
        for i in range(1,n_cols):
            if not check_diagonal(0,i):
                return False
                
        return True
