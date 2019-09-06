class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: 
            return 0
        # res = prices[1]-prices[0]
        res = 0
        cur_min = prices[0]
        
        for i in range(1, len(prices)):
            res = max(res, prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])
        return res