# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = lambda node: (node.val < node.right.val and node.val > node.left.val)
        curr = root

        if root.left and root.right:
            if isValid(root):
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            else:
                return False
        else:
            return True
       