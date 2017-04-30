# Maintain the range [1, missed) which missed means the
# number we could not get from what we enumerate now from
# nums.
# when we get num from nums:
#   (1) If num <= missed, missed could be extended to
#       missed + num
#   (2) If num > missed which means that missed that
#       number could not be combined by current nums,
#       we add missed number to nums to extend the missed
#       greedily.
#
# The implement of program is pretty tricky.
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        missed = 1
        i = 0
        patch_time = 0
        while missed <= n:
            if i < len(nums) and nums[i] <= missed:
                missed += nums[i]
                i += 1
            else:
                missed += missed
                patch_time += 1
                
        return patch_time
            