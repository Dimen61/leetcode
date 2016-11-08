class Solution(object):
    def permuteUnique(self, nums):
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
                if i > 0 and nums[i] == nums[i-1]: continue
                dfs_search(nums[:i]+nums[i+1:], path+[nums[i]])
            
        nums.sort()
        dfs_search(nums, [])
        return result