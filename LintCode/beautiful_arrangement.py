class Solution:
    """
    @param N: The number of integers
    @return: The number of beautiful arrangements you can construct
    """
    def countArrangement(self, N):
        # Write your code here
        '''
        def count_arrangement_rec(arr, i, unused):
            if unused == []:
                return 1
            else:
                results = 0
                for j in range(N-(i-1)):
                    if i%unused[j] == 0 or unused[j]%i == 0:
                        results += count_arrangement_rec(arr+[unused[j]], i + 1, unused[:j] + unused[j+1:])
                return results
                
        arr = [i for i in range(1,N+1)]
        return count_arrangement_rec([], 1, arr)
        '''
        def swap(arr, i, j):
            aux = arr[i]
            arr[i] = arr[j]
            arr[j] = aux

        def dps_count_ways(numbers, depth):
            print("yo")
            if depth == N:
                print(numbers)
                return 1
            else:
                results = 0
                for i in range(depth, N):
                    swap(numbers,i,depth)
                    if numbers[depth]%(depth+1) == 0 or (depth+1)%numbers[depth] == 0:
                        results += dps_count_ways(numbers, depth+1)
                    #return array to normal
                    swap(numbers,i,depth)
                return results
        arr = [i for i in range(1,N+1)]
        return dps_count_ways(arr, 0)