class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Quick exit
        if not prices:
            return 0

        # First transaction going forward
        min_price = sys.maxint
        max_profit = 0
        profits = []

        for i in range(len(prices)):
            # Update lowest point
            min_price = min(min_price, prices[i])

            # Update highest delta
            max_profit = max(max_profit, prices[i] - min_price)

            # Add max profit to list
            profits.append(max_profit)

        # Second transaction going backward
        max_profit = 0
        both_transaction_profit = 0
        current_max_profit = prices[-1]

        for i in range(len(prices) - 1, -1, -1):
            # Check if price going backward beats single forward profit max
            current_max_profit = max(current_max_profit, prices[i])

            # Update max profit, in case there was a better price above
            max_profit = max(max_profit, current_max_profit - prices[i])

            # Update profit of both transactions
            both_transaction_profit = max(both_transaction_profit, max_profit + profits[i])

        return both_transaction_profit