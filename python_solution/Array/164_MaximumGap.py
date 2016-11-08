class Solution(object):
    def maximumGap(self, nums):
        """
        Radix sort
        
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        
        max_num = max(nums)
        exp = 1
        while max_num // exp > 0:
            bucket = [[] for i in range(10)]
            for num in nums:
                bucket[(num // exp) % 10].append(num)
            nums = []
            for items in bucket:
                nums.extend(items)
            exp *= 10
        
        max_gap = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > max_gap:
                max_gap = nums[i] - nums[i-1]
        return max_gap if max_gap != 1 else 0
        

a = Solution()
print(a.maximumGap([100, 3, 2, 1]))
        