from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors=list(colors)
        counter=0
        for it in range(1,len(colors)):
            if colors[it-1]==colors[it]:
                counter+=min(neededTime[it-1],neededTime[it])
                neededTime[it]=max(neededTime[it-1],neededTime[it])
        return counter
if __name__=="__main__":
    colors=str(input("Type here a string: "))
    neededTime=[]
    while True:
        time=int(input('Type here a time: '))
        if time==400:
            break
        neededTime.append(time)
    sol=Solution()
    result=sol.minCost(colors=colors,neededTime=neededTime)
print(f"The result is: {result}")