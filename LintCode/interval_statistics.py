class Solution:
    """
    @param arr: the 01 array
    @param k: the limit 
    @return: the sum of the interval
    """
    #[0,0,1,0,1,1,0]
    def intervalStatistics(self, arr, k):
        # Write your code here.
        
        start = 0
        end = 0
        number_of_intervals = 0
        number_of_ones = 0
        last_zero_index = -1
        n = len(arr)
        #find position of first zero
        while start < n and arr[start] != 0:
            start+=1
        
        #we check if a zero was found
        if start < n:
            number_of_intervals = 1
            last_zero_index = start
        
        end = start + 1
        while end < n:
            if arr[end] == 1:
                number_of_ones += 1
            elif arr[end] == 0:
                last_zero_index = end
                number_of_intervals += 1
            
            if number_of_ones == k:
                #now we need to find the next one to know between which indexes the subintervals apply
                end += 1
                while end < n and arr[end] != 1:
                    number_of_intervals+=1
                    last_zero_index = end
                    end+=1

                x = (last_zero_index - start+1) - k
                number_of_intervals += ((x*(x-1))//2)

                #reset the indexes and the ones counter
                if start != last_zero_index:
                    start = last_zero_index
                else:
                    #find next start
                    start += 1
                    while start < n and arr[start] != 0:
                        start += 1
                    if start < n:
                        number_of_intervals += 1
                        last_zero_index = start
                end = start
                number_of_ones = 0
            input()
            end +=1
        if last_zero_index != start:
            x = (last_zero_index - start+1) - number_of_ones
            number_of_intervals += ((x*(x-1))//2)
        return number_of_intervals