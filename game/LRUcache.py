class Node:
    def __init__(self, next=None, prev=None, key=None, val=None):
        self.next = next  # reference to next node in DLL
        self.prev = prev  # reference to previous node in DLL
        self.key = key
        self.val = val


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addLast(self, new_node):
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def getHead(self):
        return self.head.next

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None


class LRUCache:
    def __init__(self, cap):
        self.capacity = cap
        self.map = {}
        self.list = DoublyLinkedList()

    def get(self, key):
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            self.list.addLast(node)
            return node.val
        else:
            return -1

    def put(self, key, val):
        if key in self.map:
            node = self.map[key]
            self.list.remove(node)
            self.list.addLast(node)
            return

        if len(self.map) >= self.capacity:
            old_node = self.list.getHead()
            self.map.pop(old_node.key)
            self.list.remove(old_node)

        new_node = Node(None, None, key, val)
        self.map[key] = new_node
        self.list.addLast(new_node)


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # returns 1
cache.put(3, 3)    # evicts key 2
print(cache.get(2))       # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4
