# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        assert len(inorder) == len(postorder)
        if not inorder: return None
        n = len(inorder)
        
        def helper(in_left, in_right, po_left, po_right):
            if in_left > in_right: return None
            if po_left > po_right: return None
            
            mid_index = inorder.index(postorder[po_right])
            left_tree_len = mid_index - in_left
            new_node = TreeNode(postorder[po_right])
            new_node.left = helper(in_left, mid_index-1, po_left, po_left+left_tree_len-1)
            new_node.right = helper(mid_index+1, in_right, po_left+left_tree_len, po_right-1)
            
            return new_node
        
        return helper(0, n-1, 0, n-1)
        