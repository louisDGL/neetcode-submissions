class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLength = 0
        left = 0
        right = left
        
        for right, c in enumerate (s):
            while c in seen:
                seen.remove(s[left])
                left += 1
            maxLength = max(maxLength, right-left+1)
            seen.add(c)
            

        return maxLength