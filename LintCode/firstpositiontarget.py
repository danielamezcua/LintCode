#Program no. 14

def binarySearch(self,nums,target):
	size = len(a)
	return binarySearch2(nums,target,size)

def binarySearch2(nums,target,size):
	if size == 0:
		return -1

	index = int(size/2)
	if nums[index] == target:
		return index
	else:
		#look in the left side
		if nums[index] > target:
			binarySearch2(nums[0:index-1])
		#look in the right side
		else:
			binarySearch2(nums[index+1:size-1])