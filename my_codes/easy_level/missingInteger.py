class Solution:
    def missingInteger(self, nums) -> int:
        total = nums[0] # Taking the first value
        end=1
        while end<len(nums) and nums[end]==nums[end-1]+1: # Iterating while i have a sequence
            total+=nums[end]
            end+=1
        set_=set(nums)
        while longest_subarray in set_:
            longest_subarray+=1
        return longest_subarray


if __name__=="__main__":
    nums=[]
    while True:
        num=int(input("Type here a value for my input: "))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.missingInteger(nums=nums)
    print(f"THe result is: {result}")