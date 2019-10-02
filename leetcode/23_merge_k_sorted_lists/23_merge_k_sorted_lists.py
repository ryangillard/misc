from Queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        return self.priorityQueueSort(lists)

    def naiveSort(self, lists):
        active_lists = []
        for l in lists:
            if l:
                active_lists.append(l)
        head = ListNode(-1)
        start = head

        while active_lists:
            min_val = sys.maxint
            min_list = None
            for i in range(len(active_lists)):
                if active_lists[i].val < min_val:
                    min_val = active_lists[i].val
                    min_list = i

            start.next = ListNode(active_lists[min_list].val)
            start = start.next

            active_lists[min_list] = active_lists[min_list].next
            if not active_lists[min_list]:
                del active_lists[min_list]

        return head.next

    def priorityQueueSort(self, lists):
        head = dummy = ListNode(-1)
        pq = PriorityQueue()

        for l in lists:
            if l:
                pq.put((l.val, l))

        while not pq.empty():
            val, node = pq.get()
            head.next = ListNode(val)
            head = head.next
            node = node.next

            if node:
                pq.put((node.val, node))

        return dummy.next