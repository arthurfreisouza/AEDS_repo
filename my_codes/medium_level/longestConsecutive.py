from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq=0
        num_set=set(nums)
        sequence=0
        for num in num_set:
            if num-1 not in num_set:
                sequence=1
                while num+1 in num_set:
                    sequence+=1
                    num=num+1
            max_seq=max(max_seq,sequence)
        return max_seq

def main():
    nums=[]
    while True:
        num=int(input('Type here a value for num: '))
        if num==400:
            break
        nums.append(num)
    sol=Solution()
    result=sol.longestConsecutive(nums=nums)
    print(f"The result is: {result}")
if __name__=="__main__":
    main()