class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: return
    
        flag = False
        for i in range(len(nums)-1)[::-1]:
            if nums[i] < nums[i+1]:
                lst = sorted(nums[i:])
                for j in range(len(lst)):
                    if lst[j] > nums[i]: break
                nums[i] = lst[j]
                nums[i+1:] = lst[:j] + lst[j+1:]
                
                flag = True
                break
        
        if not flag:
            nums.sort()

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: return

        length = len(nums)
        index = length - 2
        while index >= 0:
            if nums[index] < nums[index+1]:
                for i in range(index+1, length)[::-1]:
                    if nums[index] < nums[i]:
                        nums[index], nums[i] = nums[i], nums[index]
                        nums[index+1:] = sorted(nums[index+1:])
                        return
            else:
                index -= 1

        nums.reverse()


a = Solution()
lst = [1, 2]
a.nextPermutation(lst)
print('lst:', lst)