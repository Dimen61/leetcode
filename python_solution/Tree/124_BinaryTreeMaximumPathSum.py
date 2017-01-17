# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        Memorized search
        
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.max_num = -1000000000000
        f = {}
        
        def memorized_search(root):
            if not root: return 0
            if root in f: return f[root]
            
            f[root] = root.val + max(memorized_search(root.left), memorized_search(root.right), 0)
            return f[root]
            
        def dfs(root):
            if not root: return
            self.max_num = max(self.max_num, root.val)
            self.max_num = max(self.max_num, memorized_search(root))
            self.max_num = max(self.max_num, memorized_search(root.left) + root.val + memorized_search(root.right))
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        
        return self.max_num
        
        
        