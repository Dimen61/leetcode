# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        The exercise for pre-order traversal.
        
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
    
        def pre_order(root):
            """
            Return the last TreeNode in the traversal beginning with root.
            
            :type root: TreeNode
            :rtype: TreeNode
            """
            if not root.left and not root.right:
                return root
            elif root.left and root.right:
                left_node, right_node = root.left, root.right
                root.left = None
                root.right = left_node
                node = pre_order(left_node)
                node.right = right_node
                return pre_order(right_node)
            elif root.left:
                root.right = root.left
                root.left = None
                return pre_order(root.right)
            elif root.right:
                root.right = root.right
                root.left = None
                return pre_order(root.right)
                
        pre_order(root)
                
        
        