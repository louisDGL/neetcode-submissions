# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []

        h = []

        stack.append (root)

        while stack:
            curr = stack.pop()

            heapq.heappush (h, -curr.val)

            if len(h) > k:
                heapq.heappop(h)

            if curr.left:
                stack.append (curr.left)
            if curr.right:
                stack.append (curr.right)

        return -h[0]