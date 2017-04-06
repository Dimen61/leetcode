# Straightforward implement
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        length = 0
        while node:
            node = node.next
            length += 1
        node = head
        
        if length == n:
            return head.next
            
        while length > n+1:
            node = node.next
            length -= 1
        node.next = node.next.next
        return head
        

# Use two pointers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first_p = head
        while first_p and n > 1:
            first_p = first_p.next
            n -= 1
        
        # Remove the first node    
        if not first_p.next:
            return head.next
            
        second_p = head
        last_p = head
        while first_p.next:
            first_p = first_p.next
            last_p = second_p
            second_p = second_p.next
        last_p.next = last_p.next.next
        return head
        
        