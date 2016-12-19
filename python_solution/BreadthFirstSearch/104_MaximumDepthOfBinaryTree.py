# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        Recursion implement.

        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        depth = 0
        level_tral = [root]

        while level_tral:
            depth += 1
            level_tral = [item for node in level_tral
                           for item in (node.left, node.right)
                           if item]

        return depth