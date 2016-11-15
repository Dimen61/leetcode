class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        elif not nums: return 0
        elif nums[0] < nums[-1]: return nums[0]
        
        left, right = 1, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[0]:
                left = mid + 1
            elif nums[mid] > nums[mid-1]:
                right = mid -1
            else:
                return nums[mid]

    def findMin(self, nums):
        """
        More concise implementation.

        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
            
        
a = Solution()
print(a.findMin([1, 2]))