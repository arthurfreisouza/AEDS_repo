class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        final_=len(nums)
        for i in range(final_):
            if nums[i] != i:
                return i
            if i==(final_-1):
                return (i+1)

if __name__=="__main__":
    nums=str(input("Type a value: ")).strip("[]").split(",")
    nums=list(map(int,nums))
    sol=Solution()
    result=sol.missingNumber(nums)
    print(result)