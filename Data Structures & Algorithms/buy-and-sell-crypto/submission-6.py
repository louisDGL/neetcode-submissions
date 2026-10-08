class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1

        while left < len(prices):
            if right >= len(prices):
                left += 1
                right = left + 1
                continue
            
            deal = prices[right] - prices[left]
            profit = max(profit, deal)

            if prices[right] < prices[left]:
                left = right
            right += 1

        return profit    