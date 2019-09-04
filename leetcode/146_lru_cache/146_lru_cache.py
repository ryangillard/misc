class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_head(self):
        self.head = self.head.next
        if self.head:
            self.head.prev = None

        return None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.current_capacity = 0
        self.max_capacity = capacity
        self.cache = {}  # key: Node
        self.queue = DoubleLinkedList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self._append_node(node)

            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # Just update node's value
            node = self.cache[key]
            node.value = value
        else:
            if self.current_capacity < self.max_capacity:
                # Just increment capacity
                self.current_capacity += 1
            else:
                # Remove head node from cache
                del self.cache[self.queue.head.key]

                # Remove head from queue
                self.queue.remove_head()

            # Create new node
            node = Node(key, value)

            # Add node to cache
            self.cache[key] = node

        # Add node to queue
        self._append_node(node)

        return None

    def _append_node(self, node):
        if self.queue.head and self.queue.head.key == node.key:
            # Node was at queue's head, so remove and update head
            self.queue.remove_head()

        if self.queue.tail and self.queue.tail.key != node.key:
            # There was a tail and it wasn't our node

            # Make sure there are prev and next and stitch them together to get rid of node in list
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

            # Reset node's next to None
            node.next = None

            # Set old tail's next to our node
            self.queue.tail.next = node

            # Set our node's prev to the old tail
            node.prev = self.queue.tail

        # Set tail now to our node
        self.queue.tail = node

        if not self.queue.head:
            # If head doesn't exist anymore (we only have our node in the queue), then set to our node
            self.queue.head = node

        return None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)