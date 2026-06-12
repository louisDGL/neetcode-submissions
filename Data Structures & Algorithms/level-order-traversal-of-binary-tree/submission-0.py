# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None or root == []:
            return []
        
        stack = []
        res = []

        stack.append ((0, root))

        while stack:
            nb, curr = stack.pop(0)

            if nb >= len(res):
                res.append([])
            
            res[nb].append(curr.val)

            if curr.left:
                stack.append((nb+1, curr.left))
            if curr.right:
                stack.append((nb+1, curr.right))
        
        return res