class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, num
        while left < right:
            mid = (left + right) // 2
            if mid*mid < num:
                left = mid + 1
            else:
                right = mid
        return left*left == num