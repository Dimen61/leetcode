# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # traversal_vals = []
        
        # def in_order(root):
        #     if not root: return
        
        #     if root.left:
        #         in_order(root.left)
        #     traversal_vals.append(root.val)
        #     if root.right:
        #         in_order(root.right)
                
        # in_order(root)
        # for i in range(len(traversal_vals)-1):
        #     if traversal_vals[i] >= traversal_vals[i+1]:
        #         return False
        # return True

        traversal_vals = []

        def in_order(root):
            if not root: return
            if root.left:
                in_order(root.left)
            traversal_vals.append(root.val)
            if root.right:
                in_order(root.right)

        in_order(root)
        for i in range(len(traversal_vals)-1):
            if traversal_vals[i] >= traversal_vals[i+1]:
                return False
        return True

