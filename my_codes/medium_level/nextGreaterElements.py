from typing import List 
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # stack=[]# Will have my return values.
        # n=len(nums)
        # for index in range(n):
        #     found_before=False# Will control the break between loops.
        #     for j in range(index+1,n):
        #         if nums[index]<nums[j]:# Finding a greater value.
        #             stack.append(nums[j])
        #             found_before=True
        #             break
        #     if not found_before:
        #         for j in range(index):# Finding a greater value.
        #             if nums[index]<nums[j]:
        #                 stack.append(nums[j])
        #                 found_before=True
        #                 break
        #     if not found_before:
        #         stack.append(-1)
        # return stack
        n=len(nums)
        result=[-1]*n
        stack=[]
        breakpoint()
        for i in range(2*n):
            while stack and nums[i%n]>nums[stack[-1]]:
                index=stack.pop()
                result[index]=nums[i%n]
            if i<n: # Append the indexes to our stack
                stack.append(i)
        return result
    

if __name__=="__main__":
    nums=[]
    while True:
        num=int(input("Type here the value for num: "))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.nextGreaterElements(nums=nums)
    print(f"The result is: {result}")