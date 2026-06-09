class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        res = right

        while left <= right:
            middle = (right - left)//2 + left

            timeToEatMiddle = 0
            timeToEatRight = 0
            timeToEatLeft = 0

            for bananas in piles : 
                timeToEatMiddle += math.ceil(float(bananas) / middle)
            
            if timeToEatMiddle <= h:
                res = middle
                right = middle - 1
            else:
                left = middle + 1
        return res