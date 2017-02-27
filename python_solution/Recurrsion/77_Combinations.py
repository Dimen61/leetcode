# DFS
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(index, seq):
            if len(seq) == k:
                res.append(seq)
                return
            
            if index > n: return
        
            dfs(index+1, seq+[index])
            dfs(index+1, seq)
            
        dfs(1, [])
        return res
        