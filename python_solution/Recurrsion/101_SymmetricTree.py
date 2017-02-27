# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        def is_symmetric_sub(root1, root2):
            if not root1 and not root2:
                return True
            elif (not root1 and root2) or (root1 and not root2):
                return False
            elif root1.val != root2.val:
                return False
            else:
                return is_symmetric_sub(root1.left, root2.right) and is_symmetric_sub(root1.right, root2.left)
                
        
        return is_symmetric_sub(root.left, root.right)
        