# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def serialize(root):
            if not root:
                return "#"
            
            out = f"${root.val}"

            return out + serialize(root.left) + serialize(root.right)
        
        rstr = serialize(root)
        srstr = serialize(subRoot)
    
        return srstr in rstr