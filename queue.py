class Stack:
	def __init__(self, a):
		self.a = a
		self.next = None

class Queue:
	def __init__(self):
		self.node = None

	def enque(self, x):
		if self.node == None:
			new = Stack(x)
			self.node = new
		else:
			temp = self.node
			while temp.next != None:
				temp = temp.next
			new = Stack(x)
			temp.next = new
	def deque(self):
		if self.node == None:
			print("Empty")
			return 
		self.node = self.node.next

	def puts(self):
		temp = self.node
		while temp != None:
			print(temp.a)
			temp = temp.next

			
