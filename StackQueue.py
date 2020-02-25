class MyQueue:
	def __init__(self):
		"""
		Initialize your data structure here
		"""
		self.s1 = []
		self.s2 = []

	def push(self, x: int):
		"""
		Push element x to the back of queue
		"""
		self.s1.append(x)

	def peek(self):
		"""
		Get the front element
		"""
		if not self.s2:
			while self.s1:
				self.s2.append(self.s1.pop())
		return self.s2[-1]

	def pop(self):
		"""
		Removes the element from in front of queue and returns that elements
		"""
		self.peek()
		return self.s2.pop()

	def empty(self):
		"""
		Returns whether the queue is empty
		"""
		return not(self.s1 or self.s2)


# Your Myqueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(11)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

