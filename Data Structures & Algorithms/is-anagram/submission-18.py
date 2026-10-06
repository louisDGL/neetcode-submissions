class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for index in range(len(s)):
            count[ord (t[index]) - ord('a')] += 1
            count[ord (s[index]) - ord('a')] -= 1
            
        for elt in count:
            if elt != 0:
                return False
        return True