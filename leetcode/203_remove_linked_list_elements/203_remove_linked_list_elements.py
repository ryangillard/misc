# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head

        ptr = head
        ptr_next = head.next

        # Iterate over ptr_next instead of ptr, otherwise will not be able to change tail
        while ptr_next:
            if ptr_next.val == val:
                # Overwrite node
                ptr_next = ptr_next.next
                ptr.next = ptr_next
            else:
                # No need to remove anything, just move both ptrs forward 1
                ptr = ptr_next
                ptr_next = ptr_next.next

        # Don't forget to check head
        if head.val == val:
            head = head.next

        return head