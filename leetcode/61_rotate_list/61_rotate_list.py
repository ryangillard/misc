# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Quick exit
        if not head or not head.next or k == 0:
            return head

        # Find length
        start = head
        length = 0
        while start:
            start = start.next
            length += 1

        # If length is 2, just reverse if k odd
        if length == 2:
            if k % 2 == 1:
                head.next.val, head.val = head.val, head.next.val
            return head

        # If we would do a full rotation cycle back to the starting state
        if length <= k and k % length == 0:
            return head

        # Update k if it is greater than length
        k = k if k < length else k % length

        # Find end segment
        end = head
        i = 0
        while i < length - k - 1:
            end = end.next
            i += 1

        # Find start of rotation
        start = end.next
        end.next = None

        # Find connection point
        end = start
        i = 0
        while i < k - 1:
            end = end.next
            i += 1

        # Make connection
        if end:
            end.next = head

        return start