# Find the peak and low ebb.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        new_prices = []
        i = 0
        while i < len(prices):
            while i+1 < len(prices) and prices[i+1] == prices[i]:
                i += 1
            new_prices.append(prices[i])
            i += 1

        buy = sell = None
        total_profit = 0
        i = 0
        while i < len(new_prices):
            if i == 0 and i+1< len(new_prices) and new_prices[i+1] > new_prices[i]:
                buy = new_prices[i]
            elif i+1 < len(new_prices) and new_prices[i+1] > new_prices[i] and new_prices[i-1] > new_prices[i]:
                buy = new_prices[i]
            elif buy != None and i-1 >= 0 and new_prices[i] > new_prices[i-1] and i+1 < len(new_prices) and new_prices[i] > new_prices[i+1]:
                total_profit += (new_prices[i]-buy)
                buy = None
            elif buy != None and i-1 >= 0 and new_prices[i] > new_prices[i-1] and i == len(new_prices)-1:
                total_profit += (new_prices[i] - buy)
                buy = None
            i += 1
                
        return total_profit


# As long as there is a price gap, we gain a profit.
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]

        return total_profit


a = Solution()
print(a.maxProfit([2,1,2,1,0,0,1]))