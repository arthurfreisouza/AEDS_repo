class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[count]=nums[i]
                count+=1
        return nums
        
if __name__=="__main__":
    nums=[3,2,2,3]
    val=int(input("Type here the values for the variable 'val': "))
    sol=Solution()
    result=sol.removeElement(nums=nums,val=val)
    print(f"The result is: {result}")