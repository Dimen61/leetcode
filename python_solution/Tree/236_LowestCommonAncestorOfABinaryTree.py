# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.order_in_seq = self.get_inorder_traversal(root)
        
        min_pos = min(self.order_in_seq[p], self.order_in_seq[q])
        max_pos = max(self.order_in_seq[p], self.order_in_seq[q])
        
        while root:
            pos = self.order_in_seq[root]
            if min_pos <= pos <= max_pos:
                return root
            elif max_pos < pos:
                root = root.left
            else:
                root = root.right
        return root
            
    
    def get_inorder_traversal(self, root):
        order_in_seq = dict()
        seq = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                seq.append(root)
                root = root.right
        for index, node in enumerate(seq):
            order_in_seq[node] = index
        return order_in_seq
        

# Use lowestCommonAncestor to represent more meaning.
class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
            
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        return left or right
