class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        def search(num, count, combs):
            """
            :type num: int
            :type combs: List[int]
            :rtype: void
            """
            rest = n - sum(combs)
            if rest == 0:
                if count == k: result.append(combs)
                return
            elif num > rest or num >9:
                return
            elif count > k:
                return
            
            search(num+1, count+1, combs+[num])
            search(num+1, count, combs)
            
        search(1, 0, [])
        return result
            
        