class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        dp_array = [0 for i in range(m+1)]

        n = len(A)
        for i in range(n):
            aux_dp_array = [0]
            for j in range(1, m+1):
                #check if we can put this item in the bag
                if A[i] <= j:
                    aux_dp_array.append(max(dp_array[j], A[i] +  dp_array[j-A[i]]))
                else:
                    aux_dp_array.append(dp_array[j])
            dp_array = aux_dp_array
        return dp_array[m]