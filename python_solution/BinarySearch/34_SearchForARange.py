class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Find the starting position
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else: # nums[mid] == target
                right = mid
        start_pos = left
        if nums[start_pos] != target:
            return [-1, -1]
        
        # Find the ending position
        left, right = start_pos, len(nums)-1
        while left < right:
            mid = left + (right-left+1) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else: # nums[mid] == target
                left = mid
        end_pos = left
        return [start_pos, end_pos]
                
a = Solution()
print(a.searchRange([1], 1))