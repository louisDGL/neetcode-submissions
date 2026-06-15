# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        stack = []

        stack.append((root.val, root))

        while stack:
            maxN, curr = stack.pop()

            if curr.val >= maxN:
                res.append (curr)
            if curr.left:
                stack.append ((max(curr.val, maxN), curr.left))
            if curr.right:
                stack.append ((max(curr.val, maxN), curr.right))
                
        return len(res)