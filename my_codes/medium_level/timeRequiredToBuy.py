from typing import List
from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets=deque(tickets)
        counter=0
        while True:
            counter+=1
            val=tickets.popleft()
            val-=1
            # breakpoint()
            if val>0:
                tickets.append(val)
            if k==0:
                if val==0:
                    return counter
                else:
                    k=len(tickets)-1
            else:
                k-=1                
if __name__=="__main__":
    tickets=[]
    while True:
        ticket=int(input("Type here a value for the tiker: "))
        if ticket==400:
            break
        tickets.append(ticket)
    k=int(input('Type here a value for k: '))
    sol=Solution()
    result=sol.timeRequiredToBuy(tickets=tickets,k=k)
    print(f"The result is: {result}")