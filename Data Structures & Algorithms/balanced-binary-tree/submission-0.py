# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        check = True

        def dfs(root, depth):
            nonlocal check 

            if not root:
                return depth
            
            leftDepth = dfs(root.right, depth + 1)
            rightDepth = dfs(root.left, depth + 1)

            if abs(leftDepth - rightDepth) > 1:
                check = False
            return max(leftDepth, rightDepth)
        
        dfs(root, 0)
        return check