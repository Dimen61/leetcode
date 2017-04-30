# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        
        fast = head
        slow = head
        found_cycle = False
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                found_cycle = True
                break
        
        if not found_cycle:
            return None
            
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow