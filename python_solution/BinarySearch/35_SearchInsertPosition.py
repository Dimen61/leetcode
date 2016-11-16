class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)
        while left < right:
            if nums[left] > target:
                return left
            
            mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
        