class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = max(heights + [0])
        left = 0
        right = len(heights) -1 
        while left < right:
            area = min(heights[left], heights[right]) * (right - left + 1)
            max_area = max(area, max_area)

            print('area: {0}; left: {1}; right: {2}'.format(area, left, right))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
        

a = Solution()
print(a.largestRectangleArea([2,1,5,6,2,3]))
