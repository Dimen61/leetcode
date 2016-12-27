# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        DFS with recurrsion.

        :type root: TreeNode
        :rtype: int
        """
        path_lst = []
        
        def dfs(node, total):
            '''dfs the tree'''
            if not node:
                path_lst.append(total)
                return
            
            if node.left:
                dfs(node.left, 10*total+node.val)
            if node.right:
                dfs(node.right, 10*total+node.val)
            if not node.left and not node.right: # Leaf
                dfs(None, 10*total+node.val)
        
            
        dfs(root, 0)
        return sum(path_lst)

class Solution2(object):
    def sumNumbers(self, root):
        """
        DFS with stack.

        :type root: TreeNode
        :rtype: int
        """
        path_sum = 0
        stack = []
        current_val = 0

        while root or stack:
            if root:
                current_val = current_val * 10 + root.val
                stack.append((root, current_val))
                root = root.left
            else:
                root, current_val = stack.pop()
                root = root.right
                if not root.left and not root: # Leaf
                    path_sum += current_val
                    root = None

        return path_sum


class Solution3(object):
    def sumNumbers(self, root):
        """
        DFS with stack, implemented a little duplicate
        using stack.

        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        path_sum = 0
        current_val = 0
        stack = [(root, current_val)]

        while stack:
            root, current_val = stack.pop()
            if not root.left and not root.right:
                path_sum += current_val
            if root.left:
                stack.append((root.left, 10*current_val+root.left.val))
            if root.right:
                stack.append((root.right, 10*current_val+root.right.val))

        return path_sum













