# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         dict_={}
#         for index,value in enumerate(nums):
#             exists=dict_.get(value,None)
#             if exists!=None:
#                 dict_[value]=None
#             else:
#                 dict_[value]=index
#         for i in dict_.values():
#             if i!=None:
#                 return nums[i]
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict={}
        for val in nums:
            if val not in my_dict:
                my_dict[val]=1
            else:
                my_dict[val]+=1
        # breakpoint()
        for index,value in my_dict.items():
            if value==1:
                return index

if __name__=="__main__":
    nums=str(input("Type a value: ")).strip("[]").split(",")
    nums=list(map(int,nums))
    sol=Solution()
    result=sol.singleNumber(nums)
    print(result)