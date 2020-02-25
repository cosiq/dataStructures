class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class Queue:
	def __init__(self):
		self.head = None
		self.size = 0

	def isEmpty(self): return self.size == 0
	def __len__(self): return self.size

	def __repr__(self):
		if self.isEmpty(): return None
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

	def enqueue(self, data):
		newNode = Node(data)
		if self.isEmpty():
			self.head = newNode
			self.size += 1
			return
		curr = self.head
		while curr.next:
			if curr.next is None:
				break
			curr = curr.next
		curr.next = newNode
		self.size += 1

	def dequeue(self):
		item = self.head.data
		self.head = self.head.next
		return item



