class Solution(object):
    def singleNumber(self, nums):
        """
        Count for each bit through nums.

        :type nums: List[int]
        :rtype: int
        """
        bit_count = [0] * 32
        for i in range(32):
            for num in nums:
                bit_count[i] += (num >> i) & 1
            bit_count[i] = bit_count[i] % 3
        res = 0
        for i in range(32):
            res += bit_count[i] << i

        # Python int has no boundary, so 1 << 31 would
        # result  2147483648 other than -2147483648.
        return res - 2**32 if res >= 2**31 else res

    def singleNumber(self, nums):
        """
        More consice implement.

        :type nums: List[int]
        :rtype: int
        """
        ones = twos = threes = 0
        for i in range(len(nums)):
            threes &= ~(threes & nums[i])
            threes |= twos & nums[i]
            twos &= ~(twos & nums[i])
            twos |= ones & nums[i]
            ones ^= nums[i]
            ones &= ~threes
            
        return ones


            
a = Solution()
print(a.singleNumber([2, 2, 3, 2]))    
# print(a.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))        















