# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        Recursion implement.

        :type root: TreeNode
        :rtype: List[int]
        """
        res_lst = []
        
        def helper(root):
            if not root: return
        
            helper(root.left)
            helper(root.right)
            res_lst.append(root.val)
            
        helper(root)
        return res_lst
        
        
class Solution2(object):
    def postorderTraversal(self, root):
        """
        Iterative implement.

        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []

        visited = set()
        stack = [root]
        path = []

        while stack:
            node = stack[-1]
            if node in visited:
                stack.pop()
                path.append(node)
            else:
                visited.add(node)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return path


