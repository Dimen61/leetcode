class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        ans = 10**5
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_3 = nums[i] + nums[left] + nums[right]
                if abs(sum_3-target) < abs(ans-target):
                    ans = sum_3
                if  sum_3 > target:
                    right -= 1
                elif sum_3 < target:
                    left += 1
                elif sum_3 == target:
                    return target
        
        return ans