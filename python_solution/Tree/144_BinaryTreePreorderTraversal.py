# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        Recursion implment.

        :type root: TreeNode
        :rtype: List[int]
        """
        res_lst = []
        
        def helper(root):
            if not root: return
            
            res_lst.append(root.val)
            helper(root.left)
            helper(root.right)
            
        helper(root)
        return res_lst


class Solution2(object):
    def preorderTraversal(self, root):
        """
        Iterative implment.

        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []

        res_lst = []
        stack = [root]

        while stack:
            node = stack.pop()
            res_lst.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res_lst















