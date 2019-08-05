# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Quick return
        if not head or not head.next:
            return True
        
        # first_half = self.split(head)
        slow = head
        fast = head
        count = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
        count *= 2
        if fast:
            count += 1
            
        # Reverse second half
        second_half = self.reverse(slow)
        
        slow = head
        i = 0
        while i < count // 2 - 1:
            slow = slow.next
            i += 1
        slow.next = None
        
        # Compare two halves
        return self.compare(head, second_half, count // 2)
    
    def reverse(self, second_half):
        previous = None
        current = second_half
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous

    def compare(self, list1, list2, count):
        i = 0
        while i < count:
            if list1.val != list2.val:
                return False
            list1 = list1.next
            list2 = list2.next
            i += 1
        return True