# hash table
class hashTable:
	def __init__(self, size):
		self.data = [[] for _ in range(size)]

	def hashToIndex(self, keys):
		return hash(keys) % len(self.data)

	def add(self, key, value):
		index = self.hashToIndex(key)
		if self.data[index]:
			# update
			for pair in self.data[index]:
				if pair[0] == key: pair[1] = value
			else: self.data[index].append([key, value])
		else:
			self.data[index] = []
			self.data[index].append([key, value])

	def get(self, key):
		index = self.hashToIndex(key)
		if self.data[index] is None: raise ValueError
		for pair in self.data[index]:
			if pair[0] == key: return pair[1]

	def getKeys(self):
		ks = []
		for i in range(len(self.data)):
			if self.data[i]: ks.append(self.data[i][0][0])
		return ks

	def getValues(self):
		vs = []
		for i in range(len(self.data)):
			if self.data[i]: vs.append(self.data[i][0][1])
		return vs