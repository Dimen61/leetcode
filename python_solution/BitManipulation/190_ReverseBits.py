class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            if n & 1 > 0:
                res = (res << 1) + 1
            else:
                res = res << 1
            n >>= 1
        return res
            
                
a = Solution()
print(a.reverseBits(43261596))