class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0

        countPal = 0

        for center in range (n):
            left, right = center, center
            while left >= 0 and right < n and s[left] == s[right]:
                countPal += 1
                left -= 1
                right += 1
            left, right = center, center + 1
            while left >= 0 and right < n and s[left] == s[right]:
                countPal += 1
                left -= 1
                right += 1
        
        return countPal