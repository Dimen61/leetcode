import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        Use map to implement topological sorting.

        However, this is a bad implement which time complexity
        is O(N*N+E)

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        next_courses = collections.defaultdict(list)
        prev_courses = collections.defaultdict(list)
        taken_courses = set()

        for next_c, prev_c in prerequisites:
            next_courses[prev_c].append(next_c)
            prev_courses[next_c].append(prev_c)
            
        for i in range(numCourses):
            tmp_c = -1
            for c in range(numCourses):
                if c not in taken_courses and not prev_courses[c]:
                    tmp_c = c
                    taken_courses.add(c)
                    break
            if tmp_c < 0:      # Some courses are still not taken.
                return False
            else:
                for c in next_courses[tmp_c]:
                    prev_courses[c].remove(tmp_c)
            
        return True
        

class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        """
        Steps of topological sorting.
        1. Find the node with zero in-degree.
        2. Delete the node and the relationship with the rest nodes.
        3. Repeat 1-2 until all nodes have been deleted.

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        next_courses = collections.defaultdict(list)
        in_degree = [0] * numCourses

        for next_c, prev_c in prerequisites:
            next_courses[prev_c].append(next_c)
            in_degree[next_c] += 1
        
        available = [i for i, v in enumerate(in_degree) if v == 0]
        count = 0
        while available:
            c = available.pop()
            count += 1
            for next_c in next_courses[c]:
                in_degree[next_c] -= 1
                if in_degree[next_c] == 0:
                    available.append(next_c)

        return count == numCourses


a = Solution2()
print(a.canFinish(2, [[1, 0]]))





