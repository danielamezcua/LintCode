class Solution:
    """
    @param op: the type of information
    @param name: the name of user
    @param w: the money need to save or take
    @return: output the remaining money of the user.if the operation is illegal,output -1
    """
    def getAns(self, op, name, w):
        # Write your code here
        n = len(op)
        if n == 0:
            return []
        result = []
        accounts = {}
        for i in range(n):
            operation = op[i]
            nam = name[i]
            amount = w[i]
            
            #retrieve
            if operation == 1:
                if nam in accounts:
                    if amount > accounts[nam]:
                        result.append(-1)
                    else:
                        left = accounts[nam] - amount
                        result.append(left)
                        accounts[nam] = left
                else:
                    accounts[nam] = 0
                    result.append(-1)
            #deposit
            else:
                if nam not in accounts:
                    accounts[nam] = 0
                accounts[nam]+=amount
                result.append(accounts[nam])
        return result
                
                