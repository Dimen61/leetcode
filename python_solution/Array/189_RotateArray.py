class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        new_nums = nums[-k:] + nums[0:len(nums)-k]
        for i in range(len(nums)):
            nums[i] = new_nums[i]
            
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        old_nums = nums[:]
        for i in range(len(old_nums)):
            nums[(i+k) % len(old_nums)] = old_nums[i]
        
    def reverse_num(self, nums, left, right):
        """
        Reverse the nums from index i to j.
        
        :type nums: List[int]
        :type left: int
        :type right: int
        """
        i, j = left, right
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse_num(nums, 0, len(nums)-k-1)
        self.reverse_num(nums, len(nums)-k, len(nums)-1)
        self.reverse_num(nums, 0, len(nums)-1)
        
        