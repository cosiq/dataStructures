class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Stack:
    def __init__(self): self.data = []
    def __len__(self): return len(self.data)
    def isEmpty(self): return len(self) == 0
    def push(self, item): self.data.append(item)
    def peek(self): return self.data[-1]
    def pop(self): return self.data.pop()

class Queue:
    def __init__(self): self.data = []
    def __len__(self): return len(self.data)
    def isEmpty(self): return len(self) == 0
    def enqueue(self, item): self.data.insert(0, item)
    def dequeue(self): return self.data.pop()
    def peek(self): return self.data[-1]

class binaryTree:
    def __init__(self, item): self.root = Node(item)

    def preOrder(self, start):
        res = []
        if start:
            res.append(start.val)
            res.extend(self.preOrder(start.left))
            res += self.preOrder(start.right)
        return res
    
    def inOrder(self, start):
        res = []
        if start:
            res = self.inOrder(start.left)
            res.append(start.val)
            res += self.inOrder(start.right)
        return res
    
    def postOrder(self, start):
        res = []
        if start:
            res = self.postOrder(start.left)
            res += self.postOrder(start.right)
            res.append(start.val)
        return res
    
    def levelOrder(self):
        start = self.root
        queue, res = Queue(), []
        queue.enqueue(start)
        if start:
            while len(queue):
                item = queue.dequeue()
                res.append(item.val)
                if item.left: queue.enqueue(item.left)
                if item.right: queue.enqueue(item.right)
        return res
    
    def reverseLevelOrder(self):
        start = self.root
        stack, queue, res = Stack(), Queue(), []
        queue.enqueue(start)
        if start:
            while len(queue):
                item = queue.dequeue()
                stack.push(item)
                if item.right: queue.enqueue(item.right)
                if item.left: queue.enqueue(item.left)
                
            while len(stack):
                res.append(stack.pop().val)
        return res
    
    def height(self, start):
        return 1 + max(self.height(start.left), self.height(start.right)) if start else -1

    def iterSize(self):
        start, size, stack = self.root, 0, Stack()
        stack.push(start)
        if start:
            while len(stack):
                size += 1
                item = stack.pop()
                if item.left: stack.push(item.left)
                if item.right: stack.push(item.right)
        return size
    
    def recSize(self, start):
        if not start: return 0
        return 1 + self.recSize(start.left) + self.recSize(start.right)        

#          3
#        /   \ 
#       2     1
#      / \    /
#    90   1  5
#        /
#      13

ex = binaryTree(3) 
ex.root.left = Node(2)
ex.root.left.left = Node(90) 
ex.root.left.right = Node(1) 
ex.root.left.right.left = Node(13) 
ex.root.right = Node(1) 
ex.root.right.left = Node(5) 

# print(n.preorder(n.root, ""))
print("Pre-order: ", ex.preOrder(ex.root))
print("In-order: ", ex.inOrder(ex.root))
print("Post-order: ", ex.postOrder(ex.root))
print("Level-order: ", ex.levelOrder())
print("Reverse Level-order: ", ex.reverseLevelOrder())
print("Height: ", ex.height(ex.root))
print("Size: ", ex.iterSize())
print("Size: ", ex.recSize(ex.root))