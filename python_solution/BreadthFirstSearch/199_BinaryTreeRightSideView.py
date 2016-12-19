# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        BFS
        
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        right_view = []
        
        level_nodes = [root]
        
        while level_nodes:
            right_view.append(level_nodes[-1].val)
            new_level_nodes = []
            for node in level_nodes:
                if node.left:
                    new_level_nodes.append(node.left)
                if node.right:
                    new_level_nodes.append(node.right)
            level_nodes = new_level_nodes
        
        return right_view
        