class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        for elt in s:
            count[ord(elt) - ord('a')] += 1
        for elt in t:
            count[ord(elt) - ord('a')] -= 1
        
        return count == [0] * 26