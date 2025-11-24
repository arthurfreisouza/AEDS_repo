from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        my_dict={}
        for val in nums:
            if val in my_dict:
                my_dict[val]+=1
            else:
                my_dict[val]=1
        breakpoint()
        return_lst=[]
        for val in my_dict.items():
            if val[1]>1:
                return_lst.append(val[0])
        return return_lst
if __name__=="__main__":
    sol=Solution()
    nums=[]
    while True:
        num=int(input('Type here a number: '))
        if num==400:
            break
        nums.append(num)
    result=sol.getSneakyNumbers(nums=nums)
    print(f"The result is: {result}")