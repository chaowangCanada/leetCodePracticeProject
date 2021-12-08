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


def swap(head, headNext, headNextNext):
    headNext.next = headNextNext.next
    headNextNext.next = headNext
    head.next = headNextNext


def swapPairsWrapper(llist, head):
    fake_Node = Node(-1)
    fake_Node.next = head
    llist.head = fake_Node
    swapPairs(fake_Node)
    llist.head = fake_Node.next

def swapPairs(head):
    if head.next is not None and head.next.next is not None:
        swap(head, head.next, head.next.next)
        swapPairs(head.next.next)

llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.printList()

swapPairsWrapper(llist, llist.head)
llist.printList()
