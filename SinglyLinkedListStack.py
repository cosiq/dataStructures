class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self): return self.size == 0

    def __repr__(self):
        if self.isEmpty(): return "[]"
        res = "["
        curr = self.head
        while curr:
            res += str(curr.data)
            if curr.next:
                res += ", "
            curr = curr.next
        res += "]"
        return res

    def peek(self): return None if self.isEmpty() else self.head.data

    def push(self, data):
        newNode = Node(data)
        self.head, self.head.next = newNode, self.head
        self.size += 1

    def pop(self):
        if self.isEmpty(): return None
        curr = self.head
        self.head = curr.next
        self.size -= 1
        return curr.data