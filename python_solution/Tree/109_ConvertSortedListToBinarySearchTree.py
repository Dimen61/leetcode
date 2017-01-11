# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return None
        
        # Find mid ListNode
        left = right = head
        prev = None
        while right:
            right = right.next
            if not right: break
            right = right.next
            prev = left
            left = left.next
        if not prev:
            return TreeNode(left.val)
        else:
            prev.next = None
            new_node = TreeNode(left.val)
            new_node.left = self.sortedListToBST(head)
            new_node.right = self.sortedListToBST(left.next)
            
            return new_node
            
        
        