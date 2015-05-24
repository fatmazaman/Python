print "************** Singly Liked List operation ***********************"
print "******************************************************************"
#SIMPLE IMPLEMENTATION OF THE NODE

class Node(object):
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		return self.next_node == new_next

#The Head of Linked List

class linkedlist(object):
	def __init__(self, head = None):
		return self.heah == head

#insert a node (complexit O(1) because its time is constatnt)

def insert(self, data):
	new_node = Node(data)
	new_node.set_next(self.head)
	self.head = new_node
#Size : Counts number of nodes until (complexity is O(n))

def size(self):
	current = self.head
	count = 0
	while current:
		count +=  1
		current = current.get_next()
	return count
		
#Search : search the node (complexity is O(n)--> worst case)

def search(self,data):
	current = self.head
	Found = False
	while current and Found is False:
		if current.get_data() == data:
			Found = True
		else:
		    current = current. get_next()
	if current is None:
	   raise ValueError ("Data Not Found")
	return current
	
#Delete: Delete the node (Complexity O(n) --> worst case)

def delete(self, data):
	current = self.head
	previous = None
	Found = False
	while current and Found is False:
		if current.get_data == data:
			Found == True
		else:
			previous = current
			current = current.get_next() 
	if current is None:	 
	    raise ValueError ("Data Not Found")

	if Previous is None:
		self.head = current.get_next()
	else:
		previous.set_next(current.get_next())




	     	









	 


