class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                max_profit += prices[i + 1] - prices[i]

        return max_profit