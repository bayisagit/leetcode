class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        newnode = Node(val, self.head)
        self.head = newnode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        if not self.head:
            self.head = newnode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode  # ✅ fixed
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node = Node(val, current.next)
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
