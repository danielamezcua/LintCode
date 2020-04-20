#Lint code Problem 22: Flatten List
#Non recursive solution ;)
#Daniel Amezcua Sánchez A01234223

class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        n = len(nestedList)
        info_list = [{'actual_index':0,'length':n}]
        flatten_list = []
        i = info_list[0]['actual_index']
        actual_list = nestedList
        actual_level = 0
        while actual_level != 0 or i < n:
        	if i < n:
        		if type(actual_list[i]) == int:
        			flatten_list.append(actual_list[i])
        			i = i + 1
        			info_list[actual_level]['actual_index'] = i
        		else:
        			#go one level deeper
        			#create info for new level and restart index at 0
        			n = len(actual_list[i])
        			info_list[actual_level]['actual_index'] = i + 1
        			actual_level = actual_level + 1
        			info_list.append({'actual_index':0,'length':n})
        			actual_list = actual_list[i]
        			i = 0
        	else:
        		#go back one level
        		actual_level = actual_level - 1
        		j = 0
        		actual_list = nestedList
        		while j < actual_level:
        			actual_list = actual_list[info_list[j]['actual_index']-1]
        			j = j + 1
        		n = info_list[actual_level]['length']
        		i = info_list[actual_level]['actual_index']
        return flatten_list








            