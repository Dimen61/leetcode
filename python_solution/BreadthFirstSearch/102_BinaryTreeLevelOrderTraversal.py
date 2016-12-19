# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        res_lst = []
        level_lst = []
        queue = [root, '#']
        while queue:
            node = queue.pop(0)
            if node == '#':
                res_lst.append(level_lst)
                level_lst = []
                if not queue: break
                queue.append('#')
            else:
                level_lst.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return res_lst
        
    def levelOrder(self, root):
        """
        More concise implement by thinking in level
        by level.

        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []

        total_tral = []
        level_tral = [root]
        while level_tral:
            total_tral.append([node.val for node in level_tral if node])
            level_tral = [item for node in level_tral
                           for item in (node.left, node.right)
                           if item]
        return total_tral


















