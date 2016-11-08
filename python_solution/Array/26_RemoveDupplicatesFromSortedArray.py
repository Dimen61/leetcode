class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = -1
        j = 0
        while j < len(nums):
            if i == -1 or nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        del nums[i+1:]
        return len(nums)