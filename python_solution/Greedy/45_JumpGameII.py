# O(n^2) dp problem
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX_NUM = 100000000
        dp = [MAX_NUM] * (len(nums))
        dp[0] = 0
        for i in range(len(nums)):
            if dp[i] == MAX_NUM: continue
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                dp[j] = min(dp[j], dp[i]+1)
        return dp[len(nums)-1]
        

# Use BFS to implement greedy algorithm
class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        last = 0
        step = 0
        while last < len(nums) - 1:
            next_last = 0
            while index <= last:
                if index + nums[index] > next_last:
                    next_last = index + nums[index]
                index += 1
            step += 1
            last = next_last

            # print('last:', last)
            # print('next_last:', next_last)
            # print('index:', index)

        return step

a = Solution2()
print(a.jump([1, 2, 3]))