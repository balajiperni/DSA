class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_number = prices[0]
        result = 0   

        for i in range(1, len(prices)):
            if prices[i] < min_number:
                min_number = prices[i]
            else:
                profit = prices[i] - min_number
                result = max(profit, result)

        return result
