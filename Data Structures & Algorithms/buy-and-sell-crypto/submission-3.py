class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        profit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            
            elif prices[right] - prices[left] > profit:
                profit = prices[right] - prices[left]
                print(profit)
            
            right += 1
        
        return profit


        