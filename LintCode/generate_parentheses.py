class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here

        def generate_parentheses_rec(n,opened,closed,s):
            if opened == n and closed == n:
                results.append(''.join(s))
            else:
                if opened == closed:
                    s.append('(')
                    generate_parentheses_rec(n, opened+1,closed, s)
                    s.pop()
                else:
                    #open new parentheses
                    if opened < n:
                        s.append('(')
                        generate_parentheses_rec(n, opened+1, closed,s)
                        s.pop()
                    #close parentheses
                    s.append(')')
                    generate_parentheses_rec(n, opened, closed+1,s)
                    s.pop()
                
                
        results = []
        generate_parentheses_rec(n,0,0,[])
        return results