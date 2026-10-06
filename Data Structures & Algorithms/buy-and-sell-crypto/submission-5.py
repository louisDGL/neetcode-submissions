class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        bestDeal = 0
        
        while left <= len(prices) - 2:
            currDeal = prices[right] - prices[left]
            bestDeal = max(bestDeal, currDeal)

            if prices[left + 1] < prices[left]:
                left += 1
                right = left + 1
            elif right < len(prices) - 1:
                right += 1
            else:
                left += 1
                right = left + 1
        
        return bestDeal