# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        my_stack = [(root, 0)]
        res = 0

        while my_stack:
            node, depth = my_stack.pop()
            res = max(res, depth)

            if node:
                my_stack.append((node.left, depth + 1))
                my_stack.append((node.right, depth + 1))
        
        return res