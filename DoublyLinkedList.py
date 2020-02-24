# Create the node class
class Node:
	def __init__(self, data=None):
		self.data = data
		self.prev = None
		self.next = None

# Create the doubly linked list class
class DLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def __repr__(self):
		res = "["
		curr = self.head
		while curr:
			res += repr(curr.data)
			curr = curr.next
			if curr is None:
				break
			res += "->"
		res += "]"
		return res

	def prepend(self, data):
		newNode = Node(data)
		newNode.next = self.head
		if self.head:
			self.head.prev = newNode
		self.head = newNode
		self.size += 1

	def append(self, data):
		newNode = Node(data)
		if not self.head:
			newNode.prev = None
			self.head = newNode
			self.size += 1
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = newNode
		newNode.prev = last
		self.size += 1