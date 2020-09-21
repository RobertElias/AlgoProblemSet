#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def tree_paths_sum(self, root):
    if root is None:
        return []
        
    stack = [root]
    result = []
        
    while len(stack)>0:     # use while to do iteration
            
        cur_node = stack.pop()
        result.append(cur_node.value)   # pop out the node of the root and append its value
            
        if cur_node.right is not None:
            stack.append(cur_node.right)
        if cur_node.left is not None:
            stack.append(cur_node.left)
                
        return result
    

#####
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        
        if root is None:
            return []
        
        stack = [root]
        result = []
        
        while len(stack)>0:     # use while to do iteration
            
            cur_node = stack.pop()
            result.append(cur_node.val)   # pop out the node of the root and append its value
            
            if cur_node.right is not None:
                stack.append(cur_node.right)
            if cur_node.left is not None:
                stack.append(cur_node.left)
                
        return result
