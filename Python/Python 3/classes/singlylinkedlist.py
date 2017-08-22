class SinglyLinkedList:

	class _Node:
		def __init__(self,val):
			self.data=val
			self.next=None

	def __init__(self):
		self.head=None
		self.tail=None
		self.count=0

	def isEmpty(self):
		return self.count==0

	def length(self):
		return self.count

	def firstElement(self):
		if not self.isEmpty():
			return self.head.data

	def lastElement(self):
		if not self.isEmpty():
			return self.tail.data

	def addFirst(self,val):
		new_node=self._Node(val)
		if not self.isEmpty():
			new_node.next=self.head
			self.head=new_node
		else:
			self.head=self.tail=new_node
		self.count+=1

	def addLast(self,val):
		new_node=self._Node(val)
		if not self.isEmpty():
			self.tail.next=new_node
			self.tail=new_node
		else:
			self.head=self.tail=new_node
		self.count+=1

	def deleteFirst(self):
		if not self.isEmpty():
			val=self.head.data
			self.head=self.head.next
			if self.head is None:
				self.tail=None
			self.count-=1
			return val

	def deleteLast(self):
		if not self.isEmpty():
			val=self.tail.data
			if self.count==1:
				self.head=self.tail=None
			else:
				curr=self.head
				while curr.next is not self.tail:
					curr=curr.next
				self.tail=curr
				self.tail.next=None
			self.count-=1
			return val

	def isMember(self,key):
		flag=False
		if not self.isEmpty():
			curr=self.head
			while curr is not None:
				if curr.data == key:
					flag=True
					break
				else:
					curr=curr.next
		return flag

	def displayList(self):
		if not self.isEmpty():
			curr=self.head
			while curr is not None:
				print curr.data," ",
				curr=curr.next
		print ""

	def getHead(self):
		return self.head.data

	def getTail(self):
		return self.tail.data

	def getMin(self):
		if not self.isEmpty():
			curr=self.head
			min=curr.data
			curr=curr.next
			while curr is not None:
				if min>curr.data:
					min=curr.data
				curr=curr.next
			return min

	def getMax(self):
		if not self.isEmpty():
			curr=self.head
			max=curr.data
			curr=curr.next
			while curr is not None:
				if max<curr.data:
					max=curr.data
				curr=curr.next
			return max
		

	def addAfterElement(self,val,key):
		if not self.isEmpty() and self.isMember(key):
			new_node=self._Node(val)
			if self.head.data==key:
				new_node.next=self.head
				self.head=new_node
			else:
				curr=self.head
				while curr.next.data!=key:
					curr=curr.next
				new_node.next=curr.next
				curr.next=new_node
			self.count+=1

	def deleteElement(self,key):
		if not self.isEmpty() and self.isMember(key):
			if self.head.data==key:
				if self.count==1:
					self.head=self.tail=None
				else:
					self.head=self.head.next
			else:
				curr=self.head
				while curr.next.data!=key:
					curr=curr.next
				curr.next=curr.next.next
			self.count-=1

	def reverseList(self):
		if not self.isEmpty():
			prev=None
			curr=self.head
			after=self.head.next
			while after is not None:
				curr.next=prev
				prev=curr
				curr=after
				after=after.next
			curr.next=prev
			self.tail=self.head
			self.head=curr
				




