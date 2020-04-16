class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        
        def plus_one_rec(digits, carry):
            print(digits)
            if not digits:
                return [1] if carry == 1 else []
            
            new_digit = digits[-1] + carry
            if new_digit == 10:
                return plus_one_rec(digits[:-1], 1) + [0]
            else:
                return plus_one_rec(digits[:-1], 0) + [new_digit]
            
        return plus_one_rec(digits,1)