# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightView = []
        dummy = root
        while dummy.right != None:
            rightView.append(dummy.val)
            dummy = dummy.right
        rightView.append(dummy.val)
        return rightView