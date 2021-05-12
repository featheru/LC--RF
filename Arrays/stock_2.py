class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for day in range(len(prices)-1):
            diff = prices[day+1] - prices[day]
            if diff > 0:
                profit += diff

        return profit

    def maxProfit_2(self, prices: list[int]) -> int:
        """not as efficient"""
        return sum([prices[day+1] - prices[day] for day in range(len(prices)-1) if prices[day+1] - prices[day] > 0])

prices = [7,1,5,3,6,4]
print(Solution().maxProfit_2(prices))