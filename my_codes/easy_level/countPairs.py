class Solution:
    # def countPairs(self, nums: List[int], target: int) -> int:
    def countPairs(self, nums: list, target: int) -> int:
        nums.sort()
        left,right=0,len(nums)-1
        count=0
        while left<right:
            if nums[left]+nums[right]<target:
                print(f"Combination: {nums[left:right+1]}")
                count+=(right-left)
                left+=1
            else:
                right-=1
        return count
if __name__=="__main__":
    nums=[]
    while True:
        num=int(input("Type here a number: "))
        if num==400:
            break
        nums.append(num)
    print(nums)
    target=int(input("Type here a number: "))
    sol=Solution()
    result=sol.countPairs(nums=nums,target=target)
    print(f"The result is: {result}")