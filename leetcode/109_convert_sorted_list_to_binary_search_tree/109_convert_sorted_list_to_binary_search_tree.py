# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.recursivePointers(head)

    def recursiveArray(self, head):
        array = []
        while head:
            array.append(head.val)
            head = head.next

        return self.sortedArrayToBST(array)

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node

    def recursivePointers(self, head):
        if not head:
            return None

        mid = self.findMid(head)

        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.recursivePointers(head)
        node.right = self.recursivePointers(mid.next)

        return node

    def findMid(self, head):
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        return slow