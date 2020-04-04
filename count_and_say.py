class Solution:
    """
    @param n: the nth
    @return: the nth sequence
    """
    def countAndSay(self, n):
        # write your code here
        if n == 1:
            return "1"
        
        result = "1"
        
        while n > 1:
            previous_char = None
            char_count = 0
            tmp_result = ""
            for char in result:
                if not previous_char:
                    previous_char = char
                    char_count += 1
                elif previous_char == char:
                    char_count += 1
                else:
                    #append to the new result
                    tmp_result += (str(char_count) + previous_char)
                    char_count = 1
                previous_char = char
            tmp_result += (str(char_count) + previous_char)
            result = tmp_result
            n-=1
        return result

        