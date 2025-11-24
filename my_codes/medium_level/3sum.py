class Solution:
    def threeSum(self, nums):
        nums.sort()
        arr_=[]
        length=len(nums)
        for i in range(length-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left,right=i+1,length-1
            while left<right:
                total_sum=nums[i]+nums[left]+nums[right]
                if total_sum<0:
                    left+=1
                elif total_sum>0:
                    right-=1
                else:
                    arr_.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return arr_
        
if __name__=="__main__":
    nums=[]
    while True:
        num=int(input("Type here a number: "))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.threeSum(nums=nums)
    print(f"The result is: {result}")