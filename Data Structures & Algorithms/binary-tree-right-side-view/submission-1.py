# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        seen = set()

        stack = []
        stack.append ((0, root))

        while stack:
            i, curr = stack.pop()

            if curr == None:
                continue
            stack.append ((i+1, curr.left))
            stack.append ((i+1, curr.right))

            if i not in seen:
                seen.add(i)
                res.append(curr.val)

        return res