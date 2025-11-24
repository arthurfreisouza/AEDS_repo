from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        size_bin=len(nums[0])
        nums=set(nums)
        array_=[]
        for i in range(2**size_bin):
            array_.append(bin(i)[2:].zfill(size_bin))
        for num in array_:
            if num not in nums:
                return num
def main():
    nums=[]
    while True:
        num=str(input('Type here an integer: '))
        if num=='400':
            break
        nums.append(num)
    sol=Solution()
    result=sol.findDifferentBinaryString(nums=nums)
    print(f"The result is: {result}")
if __name__=="__main__":
    main()