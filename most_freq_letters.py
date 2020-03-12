#1654. Most Frequently Appearing Letters
class Solution:
    """
    @param str: the str
    @return: the sum that the letter appears the most
    """
    def mostFrequentlyAppearingLetters(self, str):
        # Write your code here.
        #init dictionary and max frequency
        frequency = {}
        max_frequency = 0
        #Iterate over string
        for c in str:
            #check if in dictionary
            if c in frequency:
            #if yes, add 1 to the value and compare it to max value
                frequency[c] += 1
            #if not, add entry and set value to 1
            else:
                frequency[c] = 1
            if frequency[c] > max_frequency:
                max_frequency = frequency[c]
        return max_frequency
