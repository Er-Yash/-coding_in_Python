class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        r=1
        profit=0

        while r<len(prices):
          cp=prices[r]-prices[l]
          if prices[l]<prices[r]:
            profit=max(cp,profit)
          else:
            l=r
          r+=1
        return profit

        
