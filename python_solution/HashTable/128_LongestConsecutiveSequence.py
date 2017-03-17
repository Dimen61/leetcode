class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        nums_used = dict()
        nums_appear = dict()
        
        for num in nums:
            nums_appear[num] = True
            
        for num in nums:
            if num in nums_used: continue
            nums_used[num] = True
            low = num - 1
            high = num + 1
            
            while low in nums_appear:
                nums_used[low] = True
                low -= 1
            while high in nums_appear:
                nums_used[high] = True
                high += 1
                
            if high-low-1 > max_length:
                max_length = high-low-1
                    
        return max_length