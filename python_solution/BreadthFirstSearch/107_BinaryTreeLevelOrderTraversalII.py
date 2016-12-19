# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        res_trals = []
        level_tral = [root]
        
        while level_tral:
            res_trals.insert(0, [node.val for node in level_tral])
            level_tral = [item for node in level_tral
                               for item in (node.left, node.right)
                               if item]
        return res_trals
        