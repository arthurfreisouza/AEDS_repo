class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        left_sum=0
        for i, num in enumerate(nums):
            right_sum=total_sum-num-left_sum
            if right_sum==left_sum:
                return i
            left_sum+=num
        return -1
    #     for i in range(len(nums)):
    #         is_equal=self.is_pivot(nums,i,i)
    #         if is_equal:
    #             return i
    #     return -1
    # def is_pivot(self,nums,left,right):
    #     sum_left,sum_right=0,0
    #     while left>=0:
    #         sum_left+=nums[left]
    #         left-=1
    #     while right<len(nums):
    #         sum_right+=nums[right]
    #         right+=1
    #     return sum_right==sum_left

if __name__=="__main__":
    nums=[]
    while True:
        num=str(input("Type here a num: "))
        if num=='400':
            break
        nums.append(num)
    sol=Solution()
    result=sol.pivotIndex(nums=nums)
    print(f"The result is: {result}")