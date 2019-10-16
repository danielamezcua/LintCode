#Problem no 17. LintCode: Subsets
#Given a set of distinct integers, return all possible subsets.

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        length = len(nums)
        nums.sort()
        s = self.subsets_recursive(nums,length)
        s.append([])
        return s

    def subsets_recursive(self,nums,length):
    	if length == 0:
    		return []
    	#base case: when the list is of length 1
    	#return all lists of length 1
    	else if length == 1:
    		return [nums]
    	else:	
    	#recursive case: all the subsets will be all the possible subsets
    	#from the list without the first element, plus the first element and without it
    		lists = [[nums[0]]]
    		first_element = [nums[0]]
    		sublists = self.subsets_recursive(nums[1:],length-1)
    		for sublist in sublists:
    			lists.append(first_element + sublist)
    		lists = lists + sublists
    		return lists


