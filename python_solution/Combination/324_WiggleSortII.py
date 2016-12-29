class Solution(object):
    def wiggleSort(self, nums):
        """
        Basic idea with sorting.
        After sorting, insert bigger numbers into smaller numbers.

        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        # Slice of list could be  assignmented.
        nums[::2], nums[1::2] = nums[:(len(nums)+1)//2][::-1], nums[(len(nums)+1)//2:][::-1]


class Solution2(object):
    def wiggleSort(self, nums):
        """
        Improvement with three-way-partition and find-kth-largest.

        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def find_kth_largest(nums, k):
            import heapq
            return heapq.nsmallest(k, nums)[-1]

        def three_way_partition(nums, mid_val):
            '''
            Rearrange nums, so nums could be separated into 3 parts.
            1 part < 2 part < 3 part.
            And all numbers in 2 part are all equal to mid_val.
            '''
            i, j, k = 0, 0, len(nums)-1
            while j <= k:
                if nums[j] < mid_val:
                    nums[i], nums[j] = nums[j], nums[i] # Swop is necessary.
                    i += 1
                    j += 1
                elif nums[j] > mid_val:
                    nums[j], nums[k] = nums[k], nums[j] 
                    k -= 1
                else:
                    j += 1


        mid_val = find_kth_largest(nums, (len(nums)+1) // 2)
        three_way_partition(nums, mid_val)
        nums[::2], nums[1::2] = nums[:(len(nums)+1)//2][::-1], nums[(len(nums)+1)//2:][::-1]




        

a = Solution2()
lst = [4,5,5,6]
a.wiggleSort(lst)
print(lst)