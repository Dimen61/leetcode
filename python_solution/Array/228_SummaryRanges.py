class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        
        res_lst = []
        left_num = right_num = None
        for i in range(len(nums)):
            if i == 0:
                left_num = nums[i]
            elif nums[i] == nums[i-1]+1:
                right_num = nums[i]
            else:
                if not right_num:
                    res_lst.append(str(left_num))
                else:
                    res_lst.append(str(left_num) + '->' + str(right_num))                    
                left_num, right_num = nums[i], None

        if not right_num:
            res_lst.append(str(left_num))
        else:
            res_lst.append(str(left_num) + '->' + str(right_num))
            
        return res_lst

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []                

        res_lst = []
        nums.append('#') # Guard
        start = end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == end:
                    res_lst.append(str(start))
                else:
                    res_lst.append(str(start) + '->' + str(end))
                start = end = nums[i]
            else:
                end = nums[i]
        return res_lst


a = Solution()
print(a.summaryRanges([0, 1]))