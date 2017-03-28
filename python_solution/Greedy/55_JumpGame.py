class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = max(nums[i], dp[i-1]-1)
            if dp[i] == 0: # Stop
                break
        return i == (len(nums)-1)
        