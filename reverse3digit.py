#LintCode. Problem 37: Reverse 3-digit integer
class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        return ((number%10)*100) + ((number%100)//10)*10 + (number//100)
