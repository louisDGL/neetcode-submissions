class Solution:
    def calculH (self, piles, k):
        h = 0
        for bananes in piles:
            if bananes%k == 0:
                h += bananes//k
            else:
                h += bananes//k + 1
        return h

    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = 1
        maxK = max(piles)
        res = 0


        while minK <= maxK:
            middle = (minK + maxK)//2
            hTheorique = self.calculH(piles, middle)
        
            if hTheorique <= h:
                maxK = middle - 1
                res = middle
            else:
                minK = middle + 1
                
        return res
        