class MinHeap:
	def __init__(self):
		self.heap = []
		self.heap_size = 0
	def __len__(self):
		return len(self.heap)
	def append(self,key):
		self.heap.append(key)
		self.heap_size += 1
		self._append(key,self.heap_size-1)
	def _append(self,key,i):
		parent=i/2
		if key<self.heap[parent]:
			self.swap(i,parent)
			self._append(key,parent)

	def left(self,index):
		return 2*(index) + 1
	def right(self,index):
		return 2*index + 2
	def swap(self,i1,i2):
		self.heap[i1],self.heap[i2] = self.heap[i2],self.heap[i1]


	def min_heapify(self,i):
		l = self.left(i)
		r = self.right(i)
		if l<self.heap_size and self.heap[l]<self.heap[i]:
			smallest = l
		else:
			smallest = i
		if r<self.heap_size and self.heap[r]<self.heap[smallest]:
			smallest = r
		if smallest != i:
			self.swap(i,smallest)
			self.min_heapify(smallest)
	def build_min_heap(self,arr):
		self.heap=arr
		self.heap_size = len(arr)
		for i in range(self.heap_size/2,-1,-1):
			self.min_heapify(i)
	def min(self):
		return self.heap[0]
	def pop(self):
		if self.heap_size == 0:
			return None
		the_min = self.heap[0]
		self.heap_size -= 1
		self.swap(0,self.heap_size)
		self.min_heapify(0)
		return the_min

	def __repr__(self):
		return str(self.heap)
a = MinHeap()
a.build_min_heap([5,3,8,4,99,6,2])
print a
a.append(1)
print a
a.append(1000)
print a 
b = MinHeap()
b.append(50)
print b
