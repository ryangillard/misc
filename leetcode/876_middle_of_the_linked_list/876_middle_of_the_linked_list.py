# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.one_pointer(head)

    def two_pointer(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def one_pointer(self, head):
        pointer = head
        count = 0
        while pointer:
            pointer = pointer.next
            count += 1
        pointer = head
        for _ in range(count // 2):
            pointer = pointer.next
        return pointer