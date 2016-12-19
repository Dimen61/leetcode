class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        Intuition implement.

        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj_nodes = [[]for i in range(n)]
        for edge in edges:
            v0, v1 = edge
            adj_nodes[v0].append(v1)
            adj_nodes[v1].append(v0)
        
        def get_tree_height(root):
            """
            Return the height of the tree.
            
            :type root: int
            :rtype: int
            """
            height = -1
            
            level_nodes = [root]
            visited_nodes = []
            while level_nodes:
                tmp_lst = []
                for v0 in level_nodes:
                    visited_nodes.append(v0)
                    for v1 in adj_nodes[v0]:
                        if v1 not in visited_nodes:
                            tmp_lst.append(v1)
                height += 1
                level_nodes = tmp_lst
                
            return height
            
        min_height = 0x0FFFFFFF
        root_lst = []
        for v in range(n):
            height = get_tree_height(v)
            if height < min_height:
                min_height = height
                root_lst = [v]
            elif height == min_height:
                root_lst.append(v)
                
        return root_lst
                
    def findMinHeightTrees(self, n, edges):
        """
        Think leaves by leaves, delete leaves by leaves
        until reach the root or possible roots.

        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nodes = list(range(n))
        adj_nodes = [[]for i in range(n)]
        for edge in edges:
            v0, v1 = edge
            adj_nodes[v0].append(v1)
            adj_nodes[v1].append(v0)

        leaves = []
        for i in range(n):
            if len(adj_nodes[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for v0 in leaves:
                v1 = adj_nodes[v0][0] # Because of leaf
                adj_nodes[v1].remove(v0)
                if len(adj_nodes[v1]) == 1:
                    new_leaves.append(v1)
            leaves = new_leaves

        return leaves

a = Solution()
print(a.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))














