# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def gcd(num1, num2):
            while num2:
                num1, num2 = num2, num1 % num2
            return num1
            
        max_point_num = 0
        for i in range(len(points)):
            duplicate = 1
            slops = {}
            for j in range(i+1, len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicate += 1
                elif points[i].x == points[j].x:
                    slops[(0, 1)] = slops.get((0, 1), 0) + 1
                elif points[i].y == points[j].y:
                    slops[(1, 0)] = slops.get((1, 0), 0) + 1
                else:
                    dy = points[j].y - points[i].y
                    dx = points[j].x - points[i].x
                    g = gcd(abs(dy), abs(dx))
                    dy //= g
                    dx //= g
                    if dy * dx > 0:
                        dy, dx = abs(dy), abs(dx)
                    else:
                        dy, dx = -abs(dy), abs(dx)
                    slops[(dx, dy)] = slops.get((dx, dy), 0) + 1
            point_num = duplicate
            if max_point_num < point_num:
                max_point_num = point_num
            for val in slops.values():
                if point_num+val > max_point_num:
                    max_point_num = point_num + val
                    
        return max_point_num
        
            
        