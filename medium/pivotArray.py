from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        if not nums:
            return None
        arr_higher=[]
        arr_lower=[]
        counter=0
        for i in nums:
            if i>pivot:
                arr_higher.append(i)
            elif i<pivot:
                arr_lower.append(i)
            else:
                counter+=1
        return arr_lower+counter*[pivot]+arr_higher
if __name__=="__main__":
    sol=Solution()
    nums=[]
    pivot=int(input('Type here a value for pivot'))
    while True:
        num=int(input('Type here a value for num'))
        if num==400:
            break
        nums.append(num)
    result=sol.pivotArray(nums=nums,pivot=pivot)
    print(result)