class Solution:
    """
    @param S: a string
    @return: return a list of strings
    """
    def letterCasePermutation(self, S):
        # write your code here
        
        def construct_string(prefix,suffix):
            if suffix == "":
                results.append(prefix)
            else:
                character = suffix[0]
                if character.isalpha():
                    construct_string(prefix + character.lower(), suffix[1:])
                    construct_string(prefix + character.upper(), suffix[1:])
                else:
                    construct_string(prefix+character,suffix[1:])
                
        results = []
        construct_string("", S)
        return results