from collections import defaultdict
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        n = len(s)
        if n == 0:
            return 0
        letters = defaultdict(lambda: -1)
        max_length = -1
        start_position = 0
        for i in range(n):
            if letters[ord(s[i])] != -1 and letters[ord(s[i])] >= start_position:
                #we found a repited character in the substring
                if (i - start_position + 1) > max_length:
                    max_length = i - start_position
                start_position = letters[ord(s[i])] + 1
            letters[ord(s[i])] = i

        if (i - start_position + 1) > max_length:
            return (i-start_position + 1)
        else:
            return max_length