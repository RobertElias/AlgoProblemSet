# Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     # Function to find sum of all the element in binary tree
#     def tree_paths_sum(root):
# 	    if (root == None):
# 		    return 0
# 	    return (root.val + addBT(root.left) +
# 		    			addBT(root.right))
        

# Solution 2
def tree_paths_sum(root):
    global sum
    #Notes if root is empty return none
    if root is None:
        return
    #Notes sum of root.data or root.val
    sum += root.data
    # NOTES go in left and right direction
    tree_paths_sum(root.left)
    tree_paths_sum(root.right)
#
# self, root, sum):
#         """
#         :type root: TreeNode
#         :type sum: int
#         :rtype: bool
#         """
#         if not root:
#             return False

#         sum -= root.val
#         if not root.left and not root.right:  # if reach a leaf
#             return sum == 0
#         return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


####3RD SOLUTION####
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

