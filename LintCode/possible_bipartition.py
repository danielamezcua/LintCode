from collections import defaultdict, deque
class Solution:
    """
    @param N:  sum of the set
    @param dislikes: dislikes peoples
    @return:  if it is possible to split everyone into two groups in this way
    """
    def possibleBipartition(self, N, dislikes):
        if not dislikes:
            return True
        if N <= 1:
            return False
        
        dislikes_graph = defaultdict(set)
        
        for dislike in dislikes:
            dislikes_graph[dislike[0]].add(dislike[1])
            dislikes_graph[dislike[1]].add(dislike[0])
        groups = {}
        q = deque()
        for i in range(1,N+1):
            if i not in groups:
                groups[i] = 1
                q.append(i)
                while q:
                    current = q.popleft()
                    for nb in dislikes_graph[current]:
                        if nb not in groups:
                            groups[nb] = groups[current] * -1
                            q.append(nb)
                        elif groups[nb] == groups[current]:
                            return False
        return True