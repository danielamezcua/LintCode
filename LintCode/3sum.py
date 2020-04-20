from collections import defaultdict
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        n = len(numbers)
        counter = defaultdict(int)
        for k in range(n):
            counter[numbers[k]] += 1
        triplets = []
        #fix i index
        i = 0
        while i < n - 2:
            #fix j index and find on the rest of the array
            j = i + 1
            while j < n-1:
                find = 0 - (numbers[i] + numbers[j])
                #check if we are looking for the same number as numbers[j]
                #it will only apply if there is more than one numbers[j] in the array
                if find == numbers[j]:
                    if find == numbers[i]:
                        if counter[find] > 2:
                            triplets.append([numbers[i],numbers[j],find])
                    elif counter[find] > 1:
                        triplets.append([numbers[i],numbers[j],find])
                #check if the number we look for is in the array. it has to be greater than numbers[j]
                elif counter[find] > 0 and find > numbers[j]:
                    triplets.append([numbers[i],numbers[j],find])
                
                #move j index until different number if found
                actual_j = numbers[j]
                j += 1
                while numbers[j] == actual_j and j < n - 1:
                    j += 1
            
            #now we move i until we find a different number than the actual numbers[i]
            actual_i = numbers[i]
            i+= 1
            while i < n - 2 and numbers[i] == actual_i:
                i+= 1
                
        return triplets