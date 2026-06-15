# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        stack = []

        stack.append ((root, float("-inf"), float("inf")))

        while stack:
            curr, left, right = stack.pop()

            if not (left < curr.val < right):
                return False

            if curr.left :
                stack.append ((curr.left, left, curr.val))
            if curr.right :
                stack.append ((curr.right, curr.val, right))
        
        return True