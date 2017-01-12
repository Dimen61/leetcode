# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        
        if not root.left and not root.right:
            return [[root.val]] if root.val == sum else []
        else:
            res_seqs = []
            if root.left:
                sub_seqs = self.pathSum(root.left, sum-root.val)
                if sub_seqs:
                    res_seqs.extend([[root.val] + seq for seq in sub_seqs])
            if root.right:
                sub_seqs = self.pathSum(root.right, sum-root.val)
                if sub_seqs:
                    res_seqs.extend([[root.val] + seq for seq in sub_seqs])
            return res_seqs
        