class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_map = dict()
        for num in nums:
            nums_map[num] = True
        miss_num = 1
        while miss_num in nums_map:
            miss_num += 1
        return miss_num
        
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        for i in range(nums_len):
            while nums[i] != i+1 and 0 < nums[i] <= nums_len and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(nums_len):
            if nums[i] != i+1:
                return i+1
        return nums_len+1
