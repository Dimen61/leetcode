class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1+nums2) == 1:
            return float(sum(nums1+nums2))

        index1 = index2 = 0
        n = (len(nums1) + len(nums2)) // 2
        is_odd = (len(nums1) + len(nums2)) % 2 == 1
        if is_odd: n += 1
        target = 0

        while index1 < len(nums1) and index2 < len(nums2) and index1+index2 < n:
            if (nums1[index1] < nums2[index2]):
                target = nums1[index1]
                index1 += 1
            else:
                target = nums2[index2]
                index2 += 1
        while index1 < len(nums1) and index1+index2 < n:
            target = nums1[index1]
            index1 += 1
        while index2 < len(nums2) and index1+index2 < n:
            target = nums2[index2]
            index2 += 1
        if is_odd:
            return float(target)
        else:
            target2 = 0
            if index1 < len(nums1) and index2 < len(nums2):
                target2 = min(nums1[index1], nums2[index2])
            elif index1 < len(nums1):
                target2 = nums1[index1]
            else:
                target2 = nums2[index2]
            return (target+target2) / 2.0

    def findMedianSortedArrays(self, nums1, nums2):
        """
        Using binary search with python array slice.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def find_kth_arrays(nums1, nums2, k):
            'Find the kth num in the two sorted int array.'
            if not nums1:
                return nums2[k-1]
            if not nums2:
                return nums1[k-1]

            mid1 = len(nums1) // 2
            mid2 = len(nums2) // 2

            if mid1+1+mid2+1 <= k:
                if nums1[mid1] < nums2[mid2]:
                    return find_kth_arrays(nums1[mid1+1:], nums2, k-mid1-1)
                else:
                    return find_kth_arrays(nums1, nums2[mid2+1:], k-mid2-1)
            elif mid1+1+mid2+1 > k:
                if nums1[mid1] < nums2[mid2]:
                    return find_kth_arrays(nums1, nums2[:mid2], k)
                else:
                    return find_kth_arrays(nums1[:mid1], nums2, k)

        n = len(nums1) + len(nums2)
        if (n % 2 == 1): 
            return find_kth_arrays(nums1, nums2, n // 2 + 1)
        else: 
            return (find_kth_arrays(nums1, nums2, n // 2) + 
                      find_kth_arrays(nums1, nums2, n // 2 + 1)) / 2.0


    def findMedianSortedArrays(self, nums1, nums2):
        """
        Using binary search with index points without slice.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def find_kth_arrays(left1, right1, left2, right2, k):
            'Find the kth num in the two sorted int array.'
            if left1 == right1:
                return nums2[left2+k-1]
            if left2 == right2:
                return nums1[left1+k-1]

            mid1 = (right1+left1) // 2
            mid2 = (right2+left2) // 2

            if mid1-left1+1+mid2-left2+1 <= k:
                if nums1[mid1] < nums2[mid2]:
                    return find_kth_arrays(mid1+1, right1, left2, right2, k-(mid1-left1+1))
                else:
                    return find_kth_arrays(left1, right1, mid2+1, right2, k-(mid2-left2+1))

            elif mid1-left1+1+mid2-left2+1 > k:
                if nums1[mid1] < nums2[mid2]:
                    return find_kth_arrays(left1, right1, left2, mid2, k)
                else:
                    return find_kth_arrays(left1, mid1, left2, right2, k)
                    
        n = len(nums1) + len(nums2)
        if (n % 2 == 1): 
            return find_kth_arrays(0, len(nums1), 0, len(nums2), n // 2 + 1)
        else: 
            return (find_kth_arrays(0, len(nums1), 0, len(nums2), n // 2) + 
                      find_kth_arrays(0, len(nums1), 0, len(nums2), n // 2 + 1)) / 2.0


                
a = Solution()
# print(a.findMedianSortedArrays([], [1]))
# print(a.findMedianSortedArrays([1, 3], [2]))
# print(a.findMedianSortedArrays([1, 2], [3, 4]))























