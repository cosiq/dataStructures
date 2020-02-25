class Stack:
	def __init__(self):
		self.array = []
		self.size = len(self.array)

	def peek(self): return self.array[-1] if self.size > 0 else None

	def push(self, item):
		self.array.append(item)
		self.size += 1

	def pop(self):
		self.size -= 1
		return self.array.pop()

	def __repr__(self):
		res = "["
		length = self.size
		for i in range(length):
			res += str(self.array[i])
			if i != length - 1: res += ", "
		res += "]"
		return res