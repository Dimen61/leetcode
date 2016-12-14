class Solution(object):
    def subsets(self, nums):
        """
        Use binary to implement.
        
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_lst = []
        
        for x in range(1 << len(nums)):
            subset = []
            pow_2 = 1
            for i in range(len(nums)):
                if x & pow_2 > 0:
                    subset.append(nums[i])
                pow_2 <<= 1
            res_lst.append(subset)
            
        return res_lst
        
    def subsets(self, nums):
        """
        DFS
        
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_lst = []
        
        def dfs(index, subset):
            if index >= len(nums):
                res_lst.append(subset)
                return
            
            dfs(index+1, subset)
            dfs(index+1, subset+[nums[index]])
        
        dfs(0, [])
        return res_lst
        

a = Solution()
print(a.subsets([1, 2, 3]))