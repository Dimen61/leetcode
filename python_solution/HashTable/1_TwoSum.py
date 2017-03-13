class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = dict()
        for index, num in enumerate(nums):
            if (target-num) in map:
                return [map[target-num], index]
            else:
                map[num] = index
                
        