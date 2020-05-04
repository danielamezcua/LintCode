from collections import defaultdict, deque
class Solution:
    """
    @param cards: 
    @return: the minimal times to discard all cards
    """
    def getAns(self, cards):
        freq_cards = {}