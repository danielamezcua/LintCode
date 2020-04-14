class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """
    def similarRGB(self, color):
        # Write your code here
        def to_hex(decimal):
            return map[decimal//16] + map[decimal % 16]
        map = {
                0 :'0',
                1 : '1',
                2 : '2',
                3 : '3',
                4 : '4',
                5 : '5',
                6 : '6',
                7 : '7',
                8 : '8',
                9 : '9',
                10: 'A',
                11: 'B',
                12: 'C',
                13: 'D',
                14: 'E',
                15: 'F'
            }
        color = color[1:]
        r = color[1:3]
        g = color[3:5]
        b = color[5:7]
        
        new_r = to_hex(17*round(int(r,16)/17))
        new_g = to_hex(17*round(int(g,16)/17))
        new_b = to_hex(17*round(int(b,16)/17))
        
        return '#' +new_r+new_g+new_b