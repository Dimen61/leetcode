# Use additional array
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        # Replace red
        for i in range(count[0]):
            nums[i] = 0
        # Replace while
        for i in range(count[0], count[1]+count[0]):
            nums[i] = 1
        # Replace blue
        for i in range(count[1]+count[0], len(nums)):
            nums[i] = 2
        
# Use two pointers            
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        index = 0
        
        while index <= right:
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                index += 1
                left += 1
            elif nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            else:
                index += 1
            
            