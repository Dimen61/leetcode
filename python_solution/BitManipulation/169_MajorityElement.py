class Solution(object):
    def majorityElement(self, nums):
        """
        Concise solution.

        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)//2]

    def majorityElement(self, nums):
        """
        Subtle iteration.
        Moore Voting Algorithm.

        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if major == nums[i]:
                count += 1
            elif major != nums[i] and count > 0:
                count -= 1
            elif major != nums[i] and count == 0:
                major = nums[i]
                count = 1
        return major

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = 0
        mask = 1
        for i in range(32):
            bit_count = 0
            for num in nums:
                if num & mask > 0: 
                    bit_count += 1
            if bit_count > len(nums) // 2:
                major |= mask
            mask <<= 1
        return major if major < 2**31 else major - 2**32

a = Solution()
# print(a.majorityElement([1,2,2,2]))
# print(a.majorityElement([-2147483648]))























