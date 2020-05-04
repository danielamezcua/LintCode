class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        max_length = 0
        freq_chars = {}
        start_index = 0
        end_index = 0
        if k == 0:
            return 0
        for char in s:
            if char not in freq_chars:
                freq_chars[char] = 0
            if freq_chars[char] == 0:
                if k == 0:
                    #compare substring length to max length
                    if end_index - start_index > max_length:
                        max_length = end_index - start_index
                    #update starting index
                    while freq_chars[s[start_index]] != 1:
                        freq_chars[s[start_index]]-=1
                        start_index+=1
                    freq_chars[s[start_index]] -= 1
                    start_index += 1
                else:
                    k-=1
            freq_chars[char]+=1
            end_index+=1
        
        if end_index - start_index > max_length:
            max_length = end_index - start_index
        return max_length