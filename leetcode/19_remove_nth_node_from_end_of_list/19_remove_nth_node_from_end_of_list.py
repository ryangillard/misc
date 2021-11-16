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
        slow = head
        fast = head.next
        
        if not fast:
            return None

        i = 0
        while fast:
            if i >= n:
                slow = slow.next
            fast = fast.next
            i += 1

        if i == n - 1:
            return head.next
        slow.next = slow.next.next
        return head