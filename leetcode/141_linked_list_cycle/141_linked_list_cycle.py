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
        if not head or not head.next:
            return False

        slow = head
        fast = head.next
        
        while fast and fast.next and fast != slow:
            slow = slow.next
            fast = fast.next.next
            
        if fast == slow:  # cycle
            return True
        return False