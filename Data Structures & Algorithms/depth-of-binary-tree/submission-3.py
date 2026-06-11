# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = []
        maxD = 1

        stack.append ((root, 1))

        while stack:
            curr, depth = stack.pop()

            if curr == None:
                continue

            if curr.right:
                stack.append((curr.right, depth + 1))
                maxD = max (maxD, depth + 1)

            if curr.left:
                stack.append((curr.left, depth + 1))
                maxD = max (maxD, depth + 1)

        
        return maxD