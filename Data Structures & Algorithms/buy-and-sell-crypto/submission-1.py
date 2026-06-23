class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        
        for left in range(len(prices)-1):
            buy = prices[left]
            for right in range(left, len(prices)):
                sell = prices[right] - buy
                profit = max(profit, sell)

        
        return profit