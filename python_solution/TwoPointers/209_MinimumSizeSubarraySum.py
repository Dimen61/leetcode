# The main idea is to main the proper window:
# Consider that every window which ends position is
# from 0 to len(nums)-1 and consider the start position
# of each window. We notice that start positions are ascending
# series.
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        left = right = 0
        total = 0
        min_len = 10 ** 8
        
        for right in range(len(nums)):
            total += nums[right]
            
            while total >= s:
                min_len = min(min_len, right-left+1)
                total -= nums[left]
                left += 1
                
        return 0 if min_len == 10 ** 8 else min_len
        
        