from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        size_=len(nums)
        counter=0
        for index in range(size_-2):
            if nums[index]==0:
                nums[index],nums[index+1],nums[index+2]=self.invert_values(nums[index:index+3])
                counter+=1
        if nums[-1]==0 or nums[-2]==0:
            return -1
        return counter
    def invert_values(self,arr)->List[int]:
        for i in range(3):
            arr[i]=1-arr[i]
        return arr
if __name__=="__main__":
    nums=[]
    while True:
        num=int(input('Type here a number: '))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.invert_values(nums=nums)
    print(f"The results is: {result}")