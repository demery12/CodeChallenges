arr = [4,16,9,2,1,54]
arr2 = [4,1,3,2,16,9,10,14,8,7]
def left(index):
	return 2*(index)
def right(index):
	return 2*(index) + 1
'''
def swap(heap,i1,i2):
	temp = heap[i1]
	heap[i1] = heap[i2]
	heap[i2] = temp

def max_heapify(heap,index):
	l = left(index)-1
	r = right(index)-1
	index = index - 1
	#print l,r,index
	try:
		print "Comparing", heap[index],"with",heap[l],heap[r]
	except:
		print "Out of Range"
		pass
	if l<len(heap) and heap[l]>heap[index]:
		largest = l
	else:
		largest = index
	if r<len(heap) and heap[r]>heap[largest]:
		largest = r
	if largest != index:
		print "Swap!"
		print "Old heap:",heap
		swap(heap,index,largest)
		print "New heap", heap,"\n"
		max_heapify(heap,largest+1)
	else:
		print "No swaps made \n"
def build_max_heap(arr):
	for i in range(len(arr)/2,0,-1):
		print "For Item:", i
		max_heapify(arr,i)
	print arr
#build_max_heap(arr2)
def get_max(heap):
	swap(heap,0,len(heap)-1)
def heap_sort(arr):
	build_max_heap(arr)
	l = []
'''

class Heap:
	def __init__(self,arr):
		self.heap_size = len(arr)
		self.heap = arr 
		self.build_max_heap()
	def build_max_heap(self):
		for i in range(self.heap_size/2,0,-1):
			self.max_heapify(i)
	#this index starts with 1
	#this is confusing
	def max_heapify(self,index):
		l = left(index)-1
		r = right(index)-1
		index = index - 1
		if l<self.heap_size and self.heap[l]>self.heap[index]:
			largest = l
		else:
			largest = index
		if r<self.heap_size  and self.heap[r]>self.heap[largest]:
			largest = r
		if largest != index:
			self.swap(index,largest)
			self.max_heapify(largest+1)
	def swap(self,i1,i2):
		temp = self.heap[i1]
		self.heap[i1] = self.heap[i2]
		self.heap[i2] = temp
	#This does destroy the heap
	def heap_sort(self):
		while self.heap_size>0:
			self.swap(0,self.heap_size-1)
			self.heap_size -= 1
			self.max_heapify(1)
		return self.heap
	def __repr__(self):
		return str(self.heap)
print Heap(arr2)
h = Heap(arr2)
print h
print h.heap_sort()
print h