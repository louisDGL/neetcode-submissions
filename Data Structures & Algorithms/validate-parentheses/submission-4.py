class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        opener = {'(', '{', '['}
        closer = {')', '}', ']'}
        corresponding = {'[': ']', '(': ')', '{': '}'}

        for c in s:
            if c in opener:
                queue.append(c)
            if c in closer:
                if len(queue) == 0:
                    return False
                c2 = queue.pop()
                if corresponding[c2] != c:
                    return False

        if len(queue) != 0:
            return False

        return True