class Solution:
    def subarraySum(self, nums, k: int) -> int:
        # counter=0
        # for i in range(len(nums)):
        #     curr_sum=0
        #     for j in range(i,len(nums)):
        #         curr_sum+=nums[j]
        #         if curr_sum==k:
        #             counter+=1
        # return counter

    #     counter=0
    #     for i in range(len(nums)):
    #         counter+=self.count_subarrays(nums=nums,left=i,right=i,k=k)
    #         counter+=self.count_subarrays(nums=nums,left=i,right=i+1,k=k)
    #     return counter
    # def count_subarrays(self,nums,left,right,k):
    #     counter=0
    #     while left>=0 and right>=0:
    #         if sum(nums[left:right])==k:
    #             print(nums[left:right], sum(nums[left:right]))
    #             counter+=1
    #         left-=1
    #         right+=1
    #     return counter

if __name__=="__main__":
    nums=[]
    while True:
        num=int(input("Type here a number for num: "))
        if num==400:
            break
        nums.append(num)
    k=int(input("Type here a value for k: "))
    sol=Solution()
    result=sol.subarraySum(nums=nums,k=k)
    print(f"The result is: {result}")