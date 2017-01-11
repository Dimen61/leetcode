# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and  \
               abs(self.height(root.left) - self.height(root.right)) <= 1
        
    def height(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return max(self.height(root.left), self.height(root.right)) + 1
        