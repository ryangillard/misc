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
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # found cycle
                slow = head  # reset slow to beginning

                while slow:
                    if slow == fast:
                        return slow

                    slow = slow.next
                    fast = fast.next

        return None