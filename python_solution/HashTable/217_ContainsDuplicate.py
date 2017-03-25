class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        appear_num = dict()
        for num in nums:
            if num in appear_num:
                return True
            appear_num[num] = True
        return False
        

