class Solution:
    # Go from left to right and keep track of min price and max profit
    # Update the min price if the current price is lower than it.
    # Calculate the profit for the current price (price - min_price)
    # If profit is larger than max profit, update it.
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = float("-inf")

        # For every price, see if it is a minimum
        # Calculate current profit
        # Update max profit if profit is larger
        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        
        return max_profit

# T: O(N) - Must go through array once
# S: O(1) - We only use 2 vars to keep track of min price and max profit