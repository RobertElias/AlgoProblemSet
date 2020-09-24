# A linked list node
class Node:
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next
# Helper function to print given linked list
def printList(node):
	ptr = node
	while ptr:
		print(ptr.value, end=" -> ")
		ptr = ptr.next
	print("None")
# ******Function to remove duplicates from a sorted list********
def removeDuplicates(node):
	previous = None
	current = node
	# take an empty set to store linked list nodes for future reference
	s = set()
	# do till linked list is not empty
	while current:
		# if current node is seen before, ignore it
		if current.value in s:
			previous.next = current.next
		# insert current node into the set and proceed to next node
		else:
			s.add(current.value)
			previous = current
		current = previous.next
	return node
#*****************************************************************

if __name__ == '__main__':

	# input keys
	keys = [3,4,3,2,6,1,2,6]

	# construct linked list
	head = None
	for i in reversed(range(len(keys))):
		head = Node(keys[i], head)

	removeDuplicates(head)

	# print linked list
	printList(head)
