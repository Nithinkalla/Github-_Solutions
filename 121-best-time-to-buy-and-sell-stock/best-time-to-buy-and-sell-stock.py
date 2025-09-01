class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        pr = 0
        for i in prices[1:]:
            if buy > i:
                buy = i
            pr = max(pr,i - buy)
        return pr