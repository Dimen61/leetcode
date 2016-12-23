class Solution(object):
    def lengthOfLIS(self, nums):
        """
        Dynamic programming
        Time complexity: O(n*n)
        
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        max_len = 1
        f = [1] * (len(nums))
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and f[i] < f[j] + 1:
                    f[i] = f[j] + 1
                    max_len = max(max_len, f[i])
        
        return max_len

    def lengthOfLIS(self, nums):
        """
        Patience Sort
        Step by step explanation:
        http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        def s_binary_search(f, x):
            '''
            Special binary search for this problem.
            Return the index which value is just less
            than x.
            f is a sorted array in ascending.

            :type f: List[int]
            :type x: int
            :rtype: int
            '''
            left, right = 0, len(f)-1

            while left < right:
                mid = (left + right + 1) // 2
                if f[mid] > x:
                    right = mid - 1
                elif f[mid] < x:
                    left = mid
                elif f[mid] == x:
                    right -= 1

            return left if f[left] < x else -1


        f = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] < f[0]:
                f[0] = nums[i]
            elif nums[i] > f[-1]:
                f.append(nums[i])
            else:
                f[s_binary_search(f, nums[i])+1] = nums[i]


        return len(f)

a = Solution()
print(a.lengthOfLIS([1, 0, 3, 2, 5, 1, 2, 3, 4]))















