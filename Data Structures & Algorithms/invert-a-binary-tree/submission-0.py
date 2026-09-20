# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # essentially for every node in the tree, recursively swap its children

        # base case
        if not root:
            return 
        
        # swap children
        temp = root.left
        root.left = root.right
        root.right = temp

        # repeat
        self.invertTree(root.left) # for all left subtrees
        self.invertTree(root.right) # for all right subtrees

        return root