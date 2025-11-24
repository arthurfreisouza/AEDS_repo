from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_count=self.binary_search(nums=nums,target=0)
        positive_count=self.binary_search(nums=nums,target=1)
        pos_count=len(nums)-positive_count
        return max(neg_count, pos_count)
    def binary_search(nums: List, target: int):
        left=0
        right=len(nums)
        while left<right:
            mid=(left+right)//2
            if nums[mid]>=target:
                right=mid
            elif nums[mid]<target:
                left=mid+1
        return left
            

def main():
    nums=[]
    while True:
        num=int(input('Type here a num: '))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.maximumCount(nums=nums)
    print(f"The result is: {result}")

if __name__=="__main__":
    pass