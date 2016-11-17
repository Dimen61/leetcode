class Solution(object):
    def isPerfectSquare(self, num):
        """
        Binary search

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

    def isPerfectSquare(self, num):
        """
        The observation: the square number = 1+3+5+7+....
        time complexity: O(sqrt(n))

        :type num: int
        :rtype: bool
        """
        x = 1
        while num > 0:
            num -= x
            x += 2
        return num == 0
