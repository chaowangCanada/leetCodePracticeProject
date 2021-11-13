from typing import Optional


class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


def swap(llist, head, next):
    if (llist.head == head):
        llist.head = next
    head.next = next.next
    next.next = head


def swapPairs(llist, head):
    if head is not None and head.next is not None:
        swap(llist, head, head.next)
        swapPairs(llist, head.next)


llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.printList()

swapPairs(llist, llist.head)
llist.printList()
