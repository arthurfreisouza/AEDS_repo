class Solution:
    def differenceOfSum(self, nums) -> int:
        element_sum=0
        digit_sum=0
        for i in range(len(nums)):
            element_sum+=nums[i]
            if len(str(nums[i]))>1:
                for i in str(nums[i]):
                    digit_sum+=int(i)
            else:
                digit_sum+=nums[i]
        diff=digit_sum-element_sum
        diff=abs(diff)
        return diff
if __name__=="__main__":
    nums=[]
    while True:
        num=int(input("Type here a num: "))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.differenceOfSum(nums=nums)
    print(f"The result is: {result}")