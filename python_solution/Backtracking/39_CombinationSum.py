class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        enable_lst = [False for i in range(target+1)]
        enable_lst[0] = True
        for i in range(target):
            if not enable_lst[i]: continue
            for num in candidates:
                if i+num <= target: enable_lst[i+num] = True

        if not enable_lst[target]: return []
        
        result = []
        def search(total, index, combs):
            """
            :type total: int
            :type index: int
            :type combs: List[int]
            :rtype: void
            """
            if total == 0: 
                result.append(combs)
                return
            elif total < 0 or index >= len(candidates):
                return

            num = candidates[index]
            if total-num >= 0 and enable_lst[total-num]:
                search(total-num, index, combs+[num])

            search(total, index+1, combs)
    
        search(target, 0, [])
        return result
        
a = Solution()
print(a.combinationSum([10,1,2,7,6,1,5], 8))
