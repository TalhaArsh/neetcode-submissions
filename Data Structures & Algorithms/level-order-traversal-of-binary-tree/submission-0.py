# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = deque()
        solution = []
        curr = root
        solution.append([curr.val])
        q.append(curr)

        while q:
            levelList = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left != None:
                    q.append(curr.left)
                    levelList.append(curr.left.val)
                if curr.right != None:
                    q.append(curr.right)
                    levelList.append(curr.right.val)
            if levelList:
                solution.append(levelList)
            
        return solution   
        
        