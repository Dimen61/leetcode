# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        
        # Contains q or q.
        if root.val == p.val:
            return root
        elif root.val == q.val:
            return root
        # p or q on the right chil and left chil of the root.
        elif q.val < root.val < p.val or p.val < root.val < q.val:
            return root
        # p and q on the left chil
        elif q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
            
# More elegant solution
class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        max_val = max(p.val, q.val)
        min_val = min(p.val, q.val)

        while root:
            if min_val <= root.val <= max_val:
                return root
            elif max_val < root.val:
                root = root.left
            else:
                root = root.right

        return root


# The more more elegant solution
class Solution3(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while (root.val-p.val)*(root.val-q.val) > 0:
            root = (root.left, root.right)[root.val < p.val]
        return root
        















            
        



