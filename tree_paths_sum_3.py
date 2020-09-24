# Python3 Program to print sum of all 
# the elements of a binary tree 

# Binary Tree Node 

""" utility that allocates a new Node 
with the given key """
class newNode: 

	# Construct to create a new node 
	def __init__(self, value): 
		self.val = x 
		self.left = None
		self.right = None
		
# Function to find sum of all the element 
def addBT(self,root): 
	if (root == None): 
		return 0
	return (root.val + addBT(root.left) + addBT(root.right)) 


# possible syntax
# sum = root.val + addBT(root.left) + addBt(rootrigh)
# return 

# Driver Code 
if __name__ == '__main__': 
	root = newNode(5) 
	root.left = newNode(4) 
	root.right = newNode(8) 
	root.left.left = newNode(11) 
	root.left.right = newNode(13) 
	root.right.left = newNode(4) 
	root.right.right = newNode(7) 
	root.right.left.right = newNode(3) 

	sum = addBT(root) 

	print("Sum of all the nodes is:", sum) 

# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10) 
