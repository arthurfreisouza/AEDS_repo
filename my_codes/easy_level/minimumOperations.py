from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter=0
        for i in nums:
            if i%3!=0:
                counter+=1
        return counter


def main():
    nums=[]
    while True:
        num=int(input('Type here a number: '))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.minimumOperations(nums=nums)
    print(f"The result is: {result}")
if __name__=="__main__":
    main()