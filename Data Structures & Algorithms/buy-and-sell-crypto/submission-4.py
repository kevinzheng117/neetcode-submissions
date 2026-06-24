class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = prices[0]

        for i in range(1, len(prices)):
            res = max(res, prices[i] - low)
            low = min(low, prices[i])
        
        return res