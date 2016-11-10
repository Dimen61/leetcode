class Solution(object):
    def subsetsWithDup(self, nums):
        """
        Implement with dfs

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        subsets = []
        nums.sort()
        
        def dfs(index, subset):
            """
            :type index: int
            :type subset: List[int]
            :rtype void
            """
            subsets.append(subset)
            if index >= length: 
                return 
        
            for i in range(index, length):
                if i > index and nums[i] == nums[i-1]: continue
                dfs(i+1, subset + [nums[i]])
            
        dfs(0, [])
        return subsets


    def subsetsWithDup(self, nums):
        """
        Implement with iteration.

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []

        nums.sort()
        subsets = [[nums[0]]]
        pre_subsets = [[nums[0]]]

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                more_sets = []
                for j in range(len(pre_subsets)):
                    one_set = pre_subsets[j] + [nums[i]]
                    more_sets.append(one_set)
                    subsets.append(one_set)
                pre_subsets = more_sets
            else:
                pre_subsets = []
                for j in range(len(subsets)):
                    one_set = subsets[j] + [nums[i]]
                    pre_subsets.append(one_set)
                pre_subsets.append([nums[i]])
                subsets.extend(pre_subsets)

        subsets.append([])
        return subsets








a = Solution()
# for lst in a.subsetsWithDup([1, 2, 2]):
    # print(lst)

# for lst in a.subsetsWithDup([5,5,5,5,5]):
#     print(lst)

for lst in a.subsetsWithDup([4,4,4,1,4]):
    print(lst)
