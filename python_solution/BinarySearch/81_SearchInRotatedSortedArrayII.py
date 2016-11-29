class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2

            # print('left: {0}; right: {1}; mid: {2}'.format(left, right, mid))

            if nums[mid] < nums[left]: # In rotated part
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                elif nums[mid] == target:
                    return True
                else:
                    right = mid - 1
            elif nums[mid] > nums[left]:
                if nums[mid] == target:
                    return True
                elif nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # nums[mid] == nums[left]
                if nums[mid] == target: return True
                left += 1

        # print('left: {0}; right: {1}; mid: {2}'.format(left, right, mid))

        return nums[left] == target


a = Solution()
#               0  1  2
# print(a.search([3, 1, 1], 3))
# print(a.search([5, 1, 3], 3))
#               0  1  2  3
# print(a.search([1, 1, 3, 1], 3))
print(a.search([3, 5, 1], 1))



