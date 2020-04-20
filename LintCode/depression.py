class Solution:
    """
    @param m: the limit
    @param k: the sum of choose
    @param arr: the array
    @return: yes or no
    """
    def depress(self, m, k, arr):
        # Write your code here.
        # we sort the array, then we just check if the sum of the first k elements
        # is greater or equal to m
        def quicksort(start,end):
            if start < end:
                index_pivot = end
                index_lowest = start
                for i in range(end-start):
                    if arr[start + i] < arr[index_pivot]:
                        #swap
                        aux = arr[start + i]
                        arr[start + i] = arr[index_lowest]
                        arr[index_lowest] =  aux
                        index_lowest+=1
                #swap pivot
                aux = arr[index_lowest]
                arr[index_lowest] = arr[index_pivot]
                arr[index_pivot] = aux
                quicksort(start, index_lowest - 1)
                quicksort(index_lowest + 1, end)
        n = len(arr)
        quicksort(0,n-1)
        print(arr)
        sum = 0
        for i in range(k):
            sum+= arr[i]
        if sum < m:
            return "yes"
        else:
            return "no"