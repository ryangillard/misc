# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        start_odd = head
        previous_odd = start_odd

        if not head.next:
            return head
        start_even = head.next
        previous_even = start_even

        current = head.next.next
        if not current:
            return head

        i = 3
        while current.next:
            previous_odd, previous_even = self.odd_or_even(
                i, current, previous_odd, previous_even)

            current = current.next
            i += 1

        previous_odd, previous_even = self.odd_or_even(
            i, current, previous_odd, previous_even)
        
        if i % 2 == 1:
            previous_even.next = None
        else:
            previous_odd.next = None

        head = start_odd
        previous_odd.next = start_even

        return head
    
    def odd_or_even(self, i, current, previous_odd, previous_even):
        if i % 2 == 1:  # odd
            previous_odd.next = current
            previous_odd = previous_odd.next
        else:  # even
            previous_even.next = current
            previous_even = previous_even.next

        return previous_odd, previous_even