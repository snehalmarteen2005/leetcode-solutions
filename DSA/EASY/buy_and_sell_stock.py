class Solution(object):
    def maxProfit(self, prices):
        minnum = prices[0]
        maxprofit = 0

        for i in range(1, len(prices)):
            if prices[i] < minnum:
                minnum = prices[i]
            else:
                if prices[i] - minnum > maxprofit:
                    maxprofit = prices[i] - minnum

        return maxprofit