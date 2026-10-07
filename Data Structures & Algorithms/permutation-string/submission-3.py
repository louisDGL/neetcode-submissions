class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = set(s1)
        left = 0
        right = left
        refCount = [0] * 26

        for c in s1:
            refCount[ord(c)-ord('a')] += 1
        
        while left < len(s2):
            c = s2[left]
            count = [0] * 26
            right = left
            while (right - left + 1) <= len(s1) and right < len(s2) and c in target:
                c = s2[right]
                count[ord(c) - ord('a')] += 1   
                if count == refCount:
                    return True
                right += 1

            left += 1

        return False