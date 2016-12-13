class Solution(object):
    def singleNumber(self, nums):
        """
        Use the properties of XOR.
        And use a key observation: the two distinct nums would has different bit at some position
        after XOR operation.
        After use XOR for all numbers, we get the target nums XOR each other and
        find out the bit they don't have the same. Then classify all nums by that
        bit. Finally XOR two parts.
        
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_res = 0
        for num in nums:
            xor_res ^= num

        # Get the rightest 1 number
        xor_res &= -xor_res 
        
        part1 = part2 = 0
        for num in nums:
            if num & xor_res > 0:
                part1 ^= num
            else:
                part2 ^= num
            
        return [part1, part2]