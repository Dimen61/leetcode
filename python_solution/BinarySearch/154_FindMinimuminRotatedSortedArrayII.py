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
        # mid = (left + right) // 2
        while left < right:
            mid = (left + right) // 2

            print('left: {0}; right: {1}; mid: {2}'.format(left, right, mid))

            if nums[mid] == nums[0]:
                if nums[-1] < nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[0]:
                left = mid + 1
            elif nums[mid] >= nums[mid-1]:
                right = mid -1
            else:
                left = mid
                break
        return min(nums[left], nums[0])

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