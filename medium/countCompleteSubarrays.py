from collections import deque
from typing import List
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        set_nums=set(nums)
        # my_queue=deque()
        counter=0
        my_dict={}
        left=0
        for end in range(len(nums)):
            if end not in my_dict:
                my_dict[end]=1
            else:
                my_dict[end]+=1
            while len(set_nums)==len(my_dict):
                my_dict[end]-=1
                if my_dict[end]==0:
                    del my_dict[end]
                left=
                counter+=left
        return counter

def main():
    nums=[]
    while True:
        num=int(input('Type here the value of num: '))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.countCompleteSubarrays(nums=nums)
    print(f"The result is: {result}")


if __name__=="__main__":
    main()