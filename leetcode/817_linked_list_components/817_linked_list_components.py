# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)

        connected_components = 0

        carry = 0
        while head:
            if head.val in G:
                carry = 1
            else:
                if carry == 1:
                    connected_components += 1
                    carry = 0

            head = head.next

        if carry == 1:
            connected_components += 1

        return connected_components