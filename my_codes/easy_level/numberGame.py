class Solution:
    def numberGame(self, nums):
        nums.sort()
        it_=0
        while it_<len(nums):
            nums[it_],nums[it_+1]=nums[it_+1],nums[it_]
            it_+=2
        return nums
if __name__=="__main__":
    nums=[]
    while True:
        num=int(input("Type here a value to num"))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.numberGame(nums=nums)
    print(f"The result is: {result}")