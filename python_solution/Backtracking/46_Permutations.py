class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def dfs_search(nums, path):
            """
            :type nums: List[int]
            :type path: List[int]
            :rtype: void
            """
            if not nums:
                result.append(path)
                return
        
            for i in range(len(nums)):
                dfs_search(nums[:i] + nums[i+1:], path+[nums[i]])
            
        dfs_search(nums, [])
        return result