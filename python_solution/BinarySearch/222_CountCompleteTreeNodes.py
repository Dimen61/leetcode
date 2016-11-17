# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        Using binary search to search the number of nodes in the last level of the
        complete binary tree.

        :type root: TreeNode
        :rtype: int
        """
        tmp_node = root
        depth = 0
        while tmp_node:
            depth += 1
            tmp_node = tmp_node.right
        total = 2**depth - 1
        
        def is_in_last_level(n):
            """
            In the last level of complete tree, whether nth node exist.
            
            :type n: int
            :rtype: bool
            """
            if n == 0: return True
            
            tmp_node = root
            last_num = (total + 1) // 2
            for i in range(depth):
                if n <= last_num:
                    tmp_node = tmp_node.left
                else:
                    tmp_node = tmp_node.right
                    n -= last_num
                last_num = last_num // 2
            return tmp_node != None
        
        left, right = 0, total + 1
        while left < right:
            mid = left + (right-left+1) // 2
            if is_in_last_level(mid):
                left = mid
            else:
                right = mid - 1
        return total + left

    def countNodes(self, root):
        """
        Basing on the structure of the complete binary tree, count the nodes
        level by level.

        :type root: TreeNode
        :rtype: int
        """
        def get_height(root):
            """Return the height of the complete binary tree."""
            height = 0
            while root:
                height += 1
                root = root.left
            return height

        nodes_num = 0
        while root:
            now_height = get_height(root)
            if get_height(root.right) == now_height - 1:
                nodes_num += 1 << (now_height-1)
                root = root.right
            else:
                nodes_num += 1 << (now_height-2)
                root = root.left
        return nodes_num



