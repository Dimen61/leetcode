class Solution(object):
    def search(self, nums, target):
        """
        We could split the nums into two part according to the min num in the nums.
        Part 1 which are all bigger than the min num is on the left of the nums.
        Part 2 which are all smaller than or equivalent to the min num in the nums.
        Split nums into two parts by using binary search to find min num.
        Finally, use binary search to find the target in the part 1 or in the part 2.
        
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Find min num index
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] < nums[right]:
                break
            mid = left + (right-left) // 2
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid
            
        min_num_index = left
        
        # Find the target in the left part
        left, right = 0, min_num_index-1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return left
            
        # Find the target in the right part
        left, right = min_num_index, len(nums)-1 
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return left
        else:
            return -1
            
            
            