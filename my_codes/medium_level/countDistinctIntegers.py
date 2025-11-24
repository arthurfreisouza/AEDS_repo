from typing import List
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reversed_arr=[]
        iterator=0
        while iterator<len(nums):
            array_aux=[]
            num_str=list(str(nums[iterator]))
            size_before=len(num_str)
            aux_iterator=size_before-1
            while aux_iterator>=0:
                array_aux.append(num_str[aux_iterator])
                aux_iterator-=1
            reversed_arr.append(int(''.join(array_aux)))
            iterator+=1
        return_val=len(set(nums+reversed_arr))
        breakpoint()
        return return_val


def main():
    nums=[]
    while True:
        num=int(input('Type here a num: '))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.countDistinctIntegers(nums=nums)
    print(f"The result is: {result}")

if __name__=="__main__":
    main()