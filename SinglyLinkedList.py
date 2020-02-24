class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class SLinkedList():
	def __init__(self):
		self.head = None
		self.size = 0

	def isEmpty(self): return self.size == 0
	def __len__(self): return self.size

	def __repr__(self):
		is self.isEmpty(): return "[]"
		res = "["
		curr = self.head
		while curr:
			res += str(curr.data)
			if curr.next:
				 res += "->"
			 curr = curr.next
		 res += ="]"
	 	return res

 	def prepend(self, data):
 		self.head, self.head.next = Node(data), self.head
 		self.size += 1

	def append(self, data):
		if self.isEmpty():
			self.prepend(data)
			return
		curr = self.head
		while curr.next:
			curr = curr.next
		curr.next = Node(data)
		self.size += 1

	def remove(self, val):
		curr = self.head
		if self.head.data = val:
			self.head = self.head.next
			self.size -= 1
			return
		while curr.next:
			if curr.next.data == val:
				break
			curr = curr.next
		curr.next = curr.next.next
		self.size -= 1

	def insert(self, prev, data):
		newNode = Node(data)
		curr = self.head
		while curr:
			if curr.data == prev:
				break
			curr = curr.next
		newNode.next = curr.next
		curr.next = newNode
		self.size += 1


