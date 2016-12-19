class Solution(object):
    def coinChange(self, coins, amount):
        """
        Dynamic programming

        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX_INT = 0x1FFFFFFF
        f = [MAX_INT] * (amount + 1)
        f[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0 and f[i-coin] < MAX_INT:
                    f[i] = min(f[i], f[i-coin] + 1)

        return f[amount] if f[amount] < MAX_INT else -1


    def coinChange(self, coins, amount):
        """
        BFS with pruning.
        
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        depth = 0

        level_nodes = [amount]
        visited = [False] * (amount+1)
        visited[amount] = True
        coins.sort(reverse=True)

        while level_nodes:
            new_level_nodes = []
            for node in level_nodes:
                if node == 0: return depth
                elif node < 0: continue
                for coin in coins:
                    if node-coin >= 0 and not visited[node-coin]:
                        new_level_nodes.append(node - coin)
                        visited[node-coin] = True
            depth += 1
            level_nodes = new_level_nodes
    
        return -1


            
a = Solution()
# print(a.coinChange([1, 2, 5], 100))
print(a.coinChange([1], 0))















