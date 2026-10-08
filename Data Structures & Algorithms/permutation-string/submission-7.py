class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Set = set(s1)
        s1Sorted = ''.join(sorted(s1))

        i = 0

        while i < len(s2):
            c = s2[i]

            if c in s1Set:
                s = s2[i:i+len(s1)]
                sSorted = ''.join(sorted(s))
                if sSorted == s1Sorted:
                    return True
            i += 1
        
        return False