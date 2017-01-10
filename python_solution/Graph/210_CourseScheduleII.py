class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        Typical topological sorting.

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        next_courses = collections.defaultdict(list)
        in_degree = [0] * numCourses
        
        for next_c, prev_c in prerequisites:
            next_courses[prev_c].append(next_c)
            in_degree[next_c] += 1
        
        stack = [i for i, v in enumerate(in_degree) if v == 0]
        res = []
        while stack:
            c = stack.pop()
            res.append(c)
            for next_c in next_courses[c]:
                in_degree[next_c] -= 1
                if in_degree[next_c] == 0:
                    stack.append(next_c)
        return res if len(res) == numCourses else []
        