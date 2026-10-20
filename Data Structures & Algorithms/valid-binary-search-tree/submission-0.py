# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, leftBoundry, rightBoundry):
            if not node:
                return True

            if not (node.val > leftBoundry and node.val < rightBoundry):
                return False

            return isValid(node.left,leftBoundry,node.val) and isValid(node.right,node.val, rightBoundry)

        return isValid(root,float("-inf"),float("inf"))
        