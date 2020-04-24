class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        def dfs_rec(num,target,r,i):
            if i < n:
                #two options: use the current number or don't use it
                #option 1: use it
                if num[i] == target:
                    r.append(num[i])
                    result.append(r.copy())
                    r.pop()
                    while i < n and num[i] == target:
                        i+=1
                elif num[i] < target:
                    r.append(num[i])
                    dfs_rec(num,target - num[i],r,i+1)
                    r.pop()
                    i+=1
                else:
                    return
                
                #option 2: don't use it
                while i < n and num[i] == num[i-1]:
                    i+=1
                dfs_rec(num,target, r,i)
                
        num.sort()
        result = []
        n = len(num)
        dfs_rec(num,target, [], 0)
        return result