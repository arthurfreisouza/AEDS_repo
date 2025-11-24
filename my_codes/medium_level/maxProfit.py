class Solution:
    def maxProfit(self, prices) -> int:
        interval1=0
        max_profit=0
        left1=0
        right1=1
        while right1<len(prices):# Iterating throughouly my array
            if prices[right1]>prices[left1]:
                interval1=prices[right1]-prices[left1]
                if right1!=len(prices)-2:
                    left2=right1+1
                    right2=right1+2
                    while right2<len(prices):
                        if prices[left2]>prices[right2]:
                            interval2=prices[right2]-prices[left2]
                            max_profit=max(max_profit, interval1+interval2)
                        else:
                            left2+=1
                        right2+=1
                else:
                    max_profit=max(max_profit, interval1+prices[right2-1]-prices[left2-2])
            else:
                left1=right1
            right1+=1
        return max_profit
if __name__=="__main__":
    prices=[]
    while True:
        price=int(input("Type here an initial value for price: "))
        if price==400:
            break
        prices.append(price)
    sol=Solution()
    result=sol.maxProfit(prices=prices)
    print(f"The result is: {result}")