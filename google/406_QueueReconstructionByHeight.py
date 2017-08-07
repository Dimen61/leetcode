# Average Time complexity: O(n^2)
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_people = []
        n = len(people)
        tmp_people = [item[:] for item in people]
        
        for i in range(n):
            min_index = None
            min_height = 1000000
            for j in range(n):
                height, count = tmp_people[j]
                if count == 0 and height < min_height:
                    min_index = j
                    min_height = height

            tmp_people[min_index][1] -= 1
            sorted_people.append(people[min_index])
            for k in range(n):
                if tmp_people[k][1] > 0 and tmp_people[min_index][0] >= tmp_people[k][0]:
                    tmp_people[k][1] -= 1
                    
        return sorted_people

# Average Time complexity: O(n^2/2)
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        tmp_people = sorted(people, key=lambda (x, y): (-x, y))
        sorted_people = []
        
        for p in tmp_people:
            sorted_people.insert(p[1], p)
            
        return sorted_people
        
                               
                                                   
        
if __name__ == '__main__':
    s = Solution()
    print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))