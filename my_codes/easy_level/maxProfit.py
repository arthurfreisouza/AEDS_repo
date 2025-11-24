class Solution:
    def maxProfit(self, prices) -> int:
        min_price=float("inf")
        max_=0
        for price in prices:
            min_price=min(price,min_price)
            max_=max(max_,price-min_price)
        return max_
if __name__=="__main__":
    prices=[]
    while True:
        price=int(input("Type here a value for the prices: "))
        if price==400:
            break
        prices.append(price)
    sol=Solution()
    result=sol.maxProfit(prices=prices)
    print(f"The result is: {result}")