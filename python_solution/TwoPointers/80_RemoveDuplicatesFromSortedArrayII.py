class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        count = 0
        for right in range(len(nums)):
            if right == 0:
                count += 1
                nums[left] = nums[right]
                left += 1
            elif nums[right] == nums[right-1]:
                if count == 2: continue
                count += 1
                nums[left] = nums[right]
                left += 1
            else:
                count = 1
                nums[left] = nums[right]
                left += 1
                
        return left
        
a = Solution()
lst = [1, 1, 1, 2, 2, 3]
a.removeDuplicates(lst)
print(lst)