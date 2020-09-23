# Given a binary tree, return the zigzag level order traversal of its nodes def func():
# value form left to right and then right to left
# for the next level and alternate between

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #-> List[List[int]]
    def zigzagLevelOrder(self, root: TreeNode):
        