class Solution:
    """
    @param a: the array a
    @return: return the index of median
    """
    def getAns(self, a):
        # write your code here 
        
        def mergeSort(array):
            n = len(array)
            if n > 1:
                middle = n//2
                left = array[:middle]
                right = array[middle:]
                mergeSort(left)
                mergeSort(right)
                
                i = 0
                j = 0
                k = 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        array[k] = left[i]
                        i+=1
                    else:
                        array[k] = right[j]
                        j+=1
                    k+=1
                
                while i < len(left):
                    array[k] = left[i]
                    k+=1
                    i+=1
                
                while j < len(right):
                    array[k] = right[j]
                    j+=1
                    k+=1
        
        #obtain a sorted array
        b = [el for el in a]
        mergeSort(b)
        
        #obtain median index and then find it on the original array
        n = len(a)
        print(b)
        if n%2 == 0:
            median_index = (n//2) - 1
        else:
            median_index = n//2
        i = 0
        while a[i] != b[median_index]:
            i+=1
        return i