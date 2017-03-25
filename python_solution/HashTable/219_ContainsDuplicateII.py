class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_index_hash = dict()
        for index, num in enumerate(nums):
            if num not in num_index_hash:
                num_index_hash[num] = index
            else:
                if index - num_index_hash[num] <= k:
                    return True
                else:
                    num_index_hash[num] = index
        
        return False
        