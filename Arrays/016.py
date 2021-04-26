#Best time to buy and Sell stock
def maxProfit(prices):
        profit=0
        i=1
        mini=prices[0]
        while i<len(prices):
            mini=min(prices[i],mini)
            profit=max(profit,prices[i]-mini)
            i+=1
        return profit