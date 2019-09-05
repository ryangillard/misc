class Node(object):

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.head = None
        self.tail = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.length == 0 or index < 0 or index + 1 > self.length:
            return -1

        node = self.getNode(index)
        return node.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        if not self.head:
            self.tail = node
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        self.length += 1

        return None

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        if not self.tail:
            self.head = node
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        self.tail = node
        self.length += 1

        return None

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index <= 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif 0 < index < self.length:
            node = self.getNode(index - 1)
            new_node = Node(val)
            new_node.prev = node
            new_node.next = node.next
            new_node.next.prev = new_node
            node.next = new_node
            self.length += 1

        return None

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if 0 <= index < self.length:
            node = self.getNode(index)
            node_prev = node.prev
            node_next = node.next

            if node == self.head:
                self.head = self.head.next

            if node == self.tail:
                self.tail = self.tail.prev

            if node.prev:
                node.prev.next = node_next
            if node.next:
                node.next.prev = node_prev

            self.length -= 1

        return None

    def getNode(self, index):
        if index < self.length // 2:
            node = self.getNodeFromHead(index)
        else:
            node = self.getNodeFromTail(index)

        return node

    def getNodeFromHead(self, index):
        ptr = self.head

        for i in range(index):
            ptr = ptr.next

        return ptr
    
    def getNodeFromTail(self, index):
        ptr = self.tail
        
        for i in range(self.length - index - 1):
            ptr = ptr.prev

        return ptr

    def printListForward(self):
        ptr = self.head
        res = []
        while ptr:
            # print(ptr.val)
            res.append(ptr.val)
            ptr = ptr.next

        return res

    def printListBackward(self):
        ptr = self.tail
        res = []
        while ptr:
            res.append(ptr.val)
            ptr = ptr.prev

        return res


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)