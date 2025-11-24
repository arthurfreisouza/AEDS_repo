from typing import List
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        # 1- create an array with the position of each number 1.
        ones_pos=[]
        for index,value in enumerate(nums):
            if value==1:
                ones_pos.append(index)
        if len(ones_pos)<=1:
            return False
        delayed=0
        ahead=delayed+1
        # breakpoint()
        while ahead<len(ones_pos):
            if ones_pos[ahead]-ones_pos[delayed]-1<k:
                return False
            delayed+=1
            ahead+=1
        return True
def main():
    nums=[]
    while True:
        num=int(input('Type here 1 or 0: '))
        if num==400:
            break
        nums.append(num)
    k=int(input('Type here a value for k: '))
    sol=Solution()
    result=sol.kLengthApart(nums=nums,k=k)
    print(f"The result is: {result}")
    
if __name__=="__main__":
    main()