# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkSub (tree, subTree):
            if tree == None and subTree == None:
                return True
            if tree == None or subTree == None:
                return False
            
            if tree.val == subTree.val:
                return checkSub(tree.left, subTree.left) and checkSub(tree.right, subTree.right)
            
            return False

        if root == None and subRoot == None:
            return True

        if root == None or subRoot == None:
            return False

        stack = []
        stack.append (root)

        while stack:
            curr = stack.pop()
            if checkSub (curr, subRoot):
                return True
            if curr.right is not None:
                stack.append (curr.right)
            if curr.left is not None:
                stack.append (curr.left)
        return False