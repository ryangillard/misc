# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # Early exits
        if not head:
            return None

        i = 0
        current = head
        previous = None

        # Move to m
        while i < m - 1:
            previous = current
            current = current.next
            i += 1

        tail = current
        head_glue_nth_node = previous  # connects head to nth node

        # Reverse from m to n
        while i < n:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            i += 1

        # Fix tail
        if head_glue_nth_node:
            head_glue_nth_node.next = previous
        else:
            head = previous

        tail.next = current

        return head