# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # conflict_one = conflict_two = None
    # pre_node = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return None

        self.conflict_one = self.conflict_two = None
        self.pre_node = None

        self.find_conflict(root)

        self.conflict_one.val, self.conflict_two.val = self.conflict_two.val, self.conflict_one.val

    def find_conflict(self, root):
        if root.left:
            self.find_conflict(root.left)

        if self.pre_node and self.pre_node.val > root.val:
            if not self.conflict_one:
                self.conflict_one = self.pre_node
            self.conflict_two = root

        self.pre_node = root

        if root.right:
            self.find_conflict(root.right)

            
                
        
        