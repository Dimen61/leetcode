class Solution(object):
    def findPeakElement(self, nums):
        """
        Iteration
        Time complexity: O(n)

        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        elif len(nums) == 1: return 0
        
        length = len(nums) 
        for i in range(length):
            if i == 0 and nums[i] > nums[i+1]:
                return i
            elif i == length-1 and nums[i] > nums[i-1]:
                return i
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i

    def findPeakElement(self, nums):
        """
        Binary search:
            sequence indexes: left, left+1, ..., mid-1, mid, mid+1, ...., right-1, right
            If mid is target, then bingo. If not, nums[mid+1] or nums[mid-1] > nums[mid].
            Suppose nums[mid+1] > nums[mid], then the target must be in [mid+1, right] range,
            because if [mid+1, right] increases sequencely, then nums[right] is the target,
            since nums[right] > nums[right-1] and nums[right] > -infinte.
            Suppose nums[mid-1] > nums[mid], things go on like above, etc.

        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid

        return left




a = Solution()
print(a.findPeakElement([1, 2, 3, 1]))
        
        