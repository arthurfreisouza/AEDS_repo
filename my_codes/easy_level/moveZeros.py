class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_zero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[last_zero]=nums[i]
                last_zero+=1
        for i in range(last_zero, len(nums)):
            nums[i]=0

if __name__=="__main__":
    nums=str(input("Type the value of your list: ")).strip("[]").split(",")
    nums=list(map(int,nums))
    sol=Solution()
    result=sol.moveZeroes(nums)
    print(f"The result is {result}")