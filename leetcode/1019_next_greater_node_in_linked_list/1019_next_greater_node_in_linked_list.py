# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        array = []
        stack = []

        while head:
            array.append(0)

            # Keep going until we find a great value or the stack is empty
            while stack and stack[-1][1] < head.val:
                # Assign head's value to array at index from stack
                array[stack.pop()[0]] = head.val

            # Add index and head's value to end of stack
            stack.append((len(array) - 1, head.val))

            # Move forward in list
            head = head.next

        return array