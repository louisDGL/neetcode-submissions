class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        left = 0
        right = 0

        bestLength = 0

        while right < len(s):
            c = s[right]
            while c in seen:
                seen.remove(s[left])
                left += 1
            seen.add(c)
            bestLength = max (bestLength, right - left + 1)
            right += 1
        
        return bestLength