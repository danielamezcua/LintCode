class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """
    def multiSort(self, array):
        # Write your code here
        self.merge_sort(array)
        return array
    
    def compare(self,left,right):
        if left[1] > right[1]:
            return 1
        elif left[1] < right[1]:
            return -1
        else:
            if left[0] < right[0]:
                return 1
            else:
                return -1
                
    def merge_sort(self,array):
        n = len(array)
        if n > 1:
            middle = n//2
            left = array[:middle]
            right = array[middle:]
            
            self.merge_sort(left)
            self.merge_sort(right)
            
            i = 0 #left
            j = 0 #right
            k = 0 #array
            #merge the two sorted arrays
            while i < len(left) and j < len(right):
                res = self.compare(left[i], right[j])
                #right is more than left
                if res < 0:
                    array[k] = right[j]
                    j += 1
                #left is more than right
                else:
                    array[k] = left[i]
                    i+= 1
                k += 1

            #check if there are still elements to add
            while i < len(left):
                array[k] = left[i]
                k+=1
                i+=1
            
            while j < len(right):
                array[k] = right[j]
                k+=1
                j+=1