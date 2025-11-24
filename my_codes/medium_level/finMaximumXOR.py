class Solution:
    def findMaximumXOR(self, nums) -> int:
        max_sum=0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                max_sum=max(max_sum,nums[i]^nums[j])
        return max_sum
if __name__=="__main__":
    nums=[]
    while True:
        num=int(input('Type here a number n: '))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.findMaximumXOR(nums=nums)
    print(f"The result is: {result}")