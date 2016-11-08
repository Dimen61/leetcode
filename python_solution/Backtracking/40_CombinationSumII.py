class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        enable_lst = [False for i in range(target+1)]
        enable_lst[0] = True
        candidates.sort()
        
        for i in range(target):
            if enable_lst[i]:
                for num in candidates:
                    if i+num <= target:
                        enable_lst[i+num] = True
                        
        if not enable_lst[target]: return []
        
        tmp_result = []
        def search(total, index, combs):
            """
            :type total: int
            :type index: int
            :rtype: void
            """
            if total == 0:
                tmp_result.append(combs)
                return
            elif index >= len(candidates) or total < 0:
                return
            
            num = candidates[index]
            if total-num >= 0 and enable_lst[total-num]:
                search(total-num, index+1, combs+[num])
            search(total, index+1, combs)
            
        search(target, 0, [])

        tmp_result.sort()
        result = []
        last = None
        for item in tmp_result:
            if not last:
                last = item
                result.append(item)
            else:
                if last != item:
                    last = item
                    result.append(item)
                    
        return result