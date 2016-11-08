class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(nums):
            """
            :type nums: List[int]
            :rtype: void
            """
            if not nums: return
        
            result.append(nums)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i] + nums[i+1:])
        
        nums.sort()
        dfs(nums)
        result.append([])
        return result

a = Solution()
for lst in a.subsetsWithDup([1, 2, 2]):
    print(lst)