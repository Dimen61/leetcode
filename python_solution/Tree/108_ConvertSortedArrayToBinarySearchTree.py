# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        The definition of binary search tree.
        1) Empty tree is BST.
        2) Left child's value is less than the value of current node
        3) Right child's value is more than the value of current node

        The definition of binary balanced tree.
        1) Empty tree is balanced.
        2) Left subtree is balanced.
        3) Right subtree is balanced.
        4) The difference between the height of left subtree and the height of right subtree 
           is no more than 1.

        The idea:
        1) The way to construct the tree which chooses the mid num as the
           root and regards the left part as the left subtree and the right part as 
           the right substree gives the tree the minimum height.
        2) Because left subtree and right subtree have the minimum height and 
           the difference between their node numbers is no more than 1, so the
           difference between the height of left subtree and right subtree is no more
           than 1.

        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        
        mid = len(nums) // 2
        new_node = TreeNode(nums[mid])
        new_node.left = self.sortedArrayToBST(nums[:mid])
        new_node.right = self.sortedArrayToBST(nums[mid+1:])
        
        return new_node
        