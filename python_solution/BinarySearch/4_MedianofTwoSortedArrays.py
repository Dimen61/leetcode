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
                
a = Solution()
# print(a.findMedianSortedArrays([], [1]))
# print(a.findMedianSortedArrays([1, 3], [2]))
print(a.findMedianSortedArrays([1, 2], [3, 4]))