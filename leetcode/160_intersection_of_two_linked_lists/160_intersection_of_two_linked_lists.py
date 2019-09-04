# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == headB:
            return headA

        headA_start = headA
        headB_start = headB
        len_A = 0
        len_B = 0
        
        while headA:
            headA = headA.next
            len_A += 1
            
        while headB:
            headB = headB.next
            len_B += 1
            
        headA = headA_start
        headB = headB_start
            
        if len_A > len_B:
            diff = len_A - len_B
            for i in range(diff):
                headA = headA.next
        else:
            diff = len_B - len_A
            for i in range(diff):
                headB = headB.next
                
        if headA == headB:
            return headA
                
        while headA != headB:
            if headA.next and headB.next and headA.next == headB.next:
                return headA.next
            elif headA == headB:
                return headA
            
            headA = headA.next
            headB = headB.next
            
        return None