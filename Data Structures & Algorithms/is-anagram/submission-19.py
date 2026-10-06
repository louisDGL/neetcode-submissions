class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26

        for elt in s:
            count[ord(elt)-ord('a')] += 1
        
        for elt in t:
            count[ord(elt)-ord('a')] -= 1
        
        for elt in count:
            if elt != 0:
                return False
        
        return True