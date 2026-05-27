class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = prices[0]

        maxP = 0

        for right in prices:
            gain = right - left
            if gain > maxP:
                maxP = gain
            if right < left:
                left = right
        
        return maxP