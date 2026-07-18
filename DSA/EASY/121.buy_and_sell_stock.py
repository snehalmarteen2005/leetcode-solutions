class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit=0
        for i in prices:
            if i < lowest:
                lowest =i
            current_profit = i-lowest
            if current_profit > profit :
                profit = current_profit 
        return profit 
