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
                
        
a = Solution()
print(a.findMin([1, 2]))