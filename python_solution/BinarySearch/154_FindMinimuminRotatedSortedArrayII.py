class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = left + (right-left) // 2
            if nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
            else:  # nums[mid] == nums[left]            
                left += 1
        return nums[left]


a = Solution()
# print(a.findMin([2, 4, 5, 6, 7, 2, 2, 2, 2]))
# print(a.findMin([1, 1]))

print(a.findMin([10, 10, 10, 1, 10]))
# print(a.findMin([3, 1, 1]))
# print(a.findMin([3, 3, 1]))
# assert a.findMin([3, 3, 1]) == 1
# assert a.findMin([3, 1, 3, 3]) == 1
# assert a.findMin([1, 3, 1, 1]) == 1
# assert (a.findMin([1, 3, 1, 1])) == 1