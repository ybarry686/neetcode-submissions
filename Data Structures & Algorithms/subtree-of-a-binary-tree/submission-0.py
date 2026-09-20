# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
            1. iterate through root tree till you find subroot val
            2. determine if from that point the trees are equivalent
        '''
        stack = [root]

        # find subtree in original tree
        while stack:
            node = stack.pop()

            if not node:
                continue
                
            if node.val == subRoot.val and self._isSameTree(node, subRoot):
                    return True
            
            stack.append(node.right)
            stack.append(node.left)
        
        return False
        
    def _isSameTree(self, node1, node2):
        stack = [(node1, node2)]
        
        while stack:
            node1, node2 = stack.pop()
            
            # both nodes are null
            if not node1 and not node2:
                continue

            # only one node in null; node values are different
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True



