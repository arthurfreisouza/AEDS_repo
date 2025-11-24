class Solution:
    def countQuadruplets(self, nums) -> int:
        smaller=float('inf')
        second_smaller=float('inf')
        third_smaller=float('inf')
        count=0
        for val in nums:
            if val < smaller:
                third_smaller=second_smaller
                second_smaller=smaller
                smaller=val
            elif val < second_smaller:
                third_smaller=second_smaller
                second_smaller=val
            elif val < third_smaller:
                third_smaller=val
            if (third_smaller+second_smaller+smaller)==val:
                count+=1
        return count
if __name__=="__main__":
    nums=[]
    while True:
        num=int(input("Type here a number for num"))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.countQuadruplets(nums=nums)
    print(f"The result is: {result}")