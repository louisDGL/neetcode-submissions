class Solution:
    def checkCharacter (self, c: str):
        return (
            ('a' <= c <= 'z') or
            ('A' <= c <= 'Z') or
            ('0' <= c <= '9')
        )

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if self.checkCharacter(s[left]) == False:
                left += 1
                continue
            if self.checkCharacter(s[right]) == False:
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
