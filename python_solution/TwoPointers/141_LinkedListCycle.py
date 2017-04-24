# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        
        left = head
        right = head
        
        while right.next and right.next.next:
            right = right.next.next
            left = left.next
            
            if right == left:
                return True
                
        return False
        