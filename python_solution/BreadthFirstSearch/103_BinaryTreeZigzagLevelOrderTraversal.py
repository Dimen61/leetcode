# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        count = 0
        total_tral = []
        level_tral = [root]
        
        while level_tral:
            if count % 2 == 1:
                total_tral.append(list(reversed([node.val for node in level_tral])))
            else:
                total_tral.append([node.val for node in level_tral])
            level_tral = [item for node in level_tral
                               for item in (node.left, node.right) 
                               if item]
            count += 1
        return total_tral
        