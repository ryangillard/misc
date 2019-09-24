# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        start = ListNode(-1)
        start.next = head
        current = start
        while current.next and current.next.next:
            # Get adjacent pair
            first = current.next
            second = first.next

            # Perform 3-way swap
            current.next = second
            first.next = second.next
            second.next = first
            
            # Increment by 2
            current = current.next.next

        return start.next