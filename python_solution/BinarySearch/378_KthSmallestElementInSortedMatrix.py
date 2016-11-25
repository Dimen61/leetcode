class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        Time complexity: O(nlog(k))

        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        def merge_sorted_array(nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: int
            """
            res_nums = []
            index1 = index2 = 0
            while index1 < len(nums1) and index2 < len(nums2):
                if nums1[index1] < nums2[index2]:
                    res_nums.append(nums1[index1])
                    index1 += 1
                else:
                    res_nums.append(nums2[index2])
                    index2 += 1
            
            while index1 < len(nums1):
                res_nums.append(nums1[index1])
                index1 += 1
            while index2 < len(nums2):
                res_nums.append(nums2[index2])
                index2 += 1
            return res_nums
            
        nums = []
        for lst in matrix:
            nums = merge_sorted_array(nums, lst)[:k]
        return nums[k-1]

    def kthSmallest(self, matrix, k):
        """
        Use heap
        Time complexity: O(klog(n)+nlog(n))

        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """        
        import heapq
        # (value, y, x)
        # value means item in the matrix
        # y means the y coordinate of the item
        # x means the x coordinate of the item
        h =  [(matrix[0][x], 0, x) for x in range(len(matrix[0]))] 
        heapq.heapify(h)
        for i in range(k):
            val, y, x = heapq.heappop(h)
            if y + 1 < len(matrix):
                heapq.heappush(h, (matrix[y+1][x], y+1, x))

        return val

    def kthSmallest(self, matrix, k):
        """
        Use binary search.
        Time complexity: O(log(N)nlog(n))

        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        def count_less_eq(lst, x):
            """
            Use binary search find the how many items in sorted array are less than
            or equal to x.
            """
            left, right = 0, len(lst)-1
            while left < right:
                mid = left + (right-left+1) // 2
                if lst[mid] < x:
                    left = mid + 1
                elif lst[mid] > x:
                    right = mid - 1 
                else:
                    left = mid
            if left >= len(lst): return len(lst)
            elif lst[left] <= x: return left+1
            else: return left

        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]
        while left < right:
            mid = left + (right-left) // 2
            count = 0
            for i in range(n):
                count += count_less_eq(matrix[i], mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left