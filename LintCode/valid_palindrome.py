class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    """
        '-------aa' true
        '        a' true
        'anita,lavalatina¡'¡¡' true
        'a ------- ' true
        'a ¨¨*^Ç¨* a'true
        '¨Ç¨^**¨Ç¨_¨^!!!!' false
        '' true
    """
    def isPalindrome(self, s):
        # write your code here
        #we will use two indexes. one starts from the left and one from the right
        #the left index will look for the first letter, then the right index does the same
        #then we compare those letters. they have to be the same. 
        #we stop when one index has reached the other.
        #then we compare the number of characters each index found. they must be equal
        #it finishes in one of the two circumstances:
        
        n = len(s)
        left = 0
        right = n - 1
        chars_left = 0
        chars_right = 0
        if n == 0:
            return True
            
        while left < right and left < n and right >= 0:
            while left < n and not s[left].isalnum():
                left += 1
            if left >= n:
                break
            chars_left += 1
            
            while right >= 0 and not s[right].isalnum():
                right -= 1
            if right < 0:
                break
            
            chars_right += 1
            
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
        
        if chars_right == chars_left:
            return True
        else:
            return False