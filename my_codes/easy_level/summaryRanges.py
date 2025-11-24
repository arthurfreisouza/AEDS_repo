from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        iterator=0
        final_arr=[]
        while iterator<len(nums):
            saving_actual=iterator
            while iterator<len(nums)-1 and nums[iterator+1]==nums[iterator]+1:
                iterator+=1
            if saving_actual==iterator:
                final_arr.append(str(nums[iterator]))
            else:
                final_arr.append(f'{nums[saving_actual]}->{nums[iterator]}')
            iterator+=1
        return final_arr
            
            

def main():
    nums=[]
    while True:
        num=int(input('Type here a number: '))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.summaryRanges(nums=nums)
    print(f"The result is: {result}")
if __name__=="__main__":
    main()