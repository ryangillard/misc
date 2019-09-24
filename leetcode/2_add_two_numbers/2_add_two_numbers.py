# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        current = l3
        carry = 0
        while l1 and l2:
            current.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = 1 if l1.val + l2.val + carry > 9 else 0
            current = current.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            current.next = ListNode((l1.val + carry) % 10)
            carry = 1 if l1.val + carry > 9 else 0
            current = current.next
            l1 = l1.next

        while l2:
            current.next = ListNode((l2.val + carry) % 10)
            carry = 1 if l2.val + carry > 9 else 0
            current = current.next
            l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return l3.next