class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left < right:
            mid = left + (right-left) // 2
            if mid*mid < x:
                left = mid + 1
            else:
                right = mid
        if left*left == x: return left
        else: return left-1

a = Solution()
print(a.mySqrt(2))
print(a.mySqrt(0))