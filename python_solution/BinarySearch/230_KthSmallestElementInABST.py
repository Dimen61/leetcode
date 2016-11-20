# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_node_num(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.get_node_num(root.left) + self.get_node_num(root.right) + 1
    
    def kthSmallest(self, root, k):
        """
        The main idea is binary search.

        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        left_num = self.get_node_num(root.left)
        if k <= left_num:
            return self.kthSmallest(root.left, k)
        elif k == left_num + 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k-left_num-1)

    def kthSmallest(self, root, k):
        """
        Use python generator to implement a binary tree in-order traversal.

        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def helper(root):
            if root.left:
                for val in helper(root.left):
                    yield val
            yield root.val
            if root.right:
                for val in helper(root.right):
                    yield val

        i = 0
        for val in helper(root):
            i += 1
            if i == k:
                return val

    def kthSmallest(self, root, k):
        """
        Use iteration to implement binary tree in-order traversal.

        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        i = 0
        node_stack = []
        while root or node_stack:
            if root:
                node_stack.append(root)
                root = root.left
            else:
                root = node_stack.pop()
                i += 1
                if i == k:
                    return root.val
                root = root.right
















