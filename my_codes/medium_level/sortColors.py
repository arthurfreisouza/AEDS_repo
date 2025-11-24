class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index in range(len(nums)):
            right=len(nums)-1
            # lowest_index=index
            # lowest_value=nums[index]
            while index<right:
                if nums[right]<nums[index]:
                    # lowest_index=right
                    # lowest_value=nums[right]
                    nums[index],nums[right]=nums[right],nums[index]
                right-=1
            # nums[index],nums[lowest_index]=nums[lowest_index],nums[index]
        return nums
if __name__=="__main__":
    num=0
    nums=[]
    while True:
        num=int(input("Type here a number: "))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.sortColors(nums=nums)
    print(f"The result is: {result}")