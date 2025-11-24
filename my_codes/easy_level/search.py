class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right=0,len(nums)-1
        breakpoint()
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                left=mid+1
            else:
                right=mid-1
        return -1
        
if __name__=="__main__":
    nums=list(str(input("Type here the numbers of your list: ")).strip("[]").split(","))
    nums=list(map(int,nums))
    target=int(input("Type here the numbers of your list: "))
    sol=Solution()
    result=sol.search(nums, target)
    print(f"The result is: {result}")